# Modifiable parameters
numbCores 		= 2 			# number of CPU cores allocated to each computation
endTime 		= 0.003 		# total flow time to compute
writeInterval 	= 0.003			# save data every interval
deltaT 			= 0.0005		# time-step for most of computation (main)


# Don't modify below (just yet)
startupDeltaT 	= 0.0002 		# time-step for inital startup
startupEndTime 	= 0.001 		# time to switch to main time-step size

from foamlib import FoamCase, FoamFile, AsyncFoamCase
import os, asyncio

# prevent decomposition errors
case = FoamCase("../combined")
case.clean()
decParDict = FoamFile("../combined/system/decomposeParDict")
decParDict["numberOfSubdomains"] = numbCores
print("-> computation pre-processing...")
case.decompose_par()
replaceNaN = "sed -i -e 's/nan/0/g' ../combined/processor*/0/U"
os.system(replaceNaN)

# run startup with relaxed values
case.control_dict["deltaT"] 		= startupDeltaT
case.control_dict["endTime"] 		= startupEndTime
case.control_dict["writeInterval"] 	= startupEndTime
case.run()

# change parameters to intended values
case.control_dict["deltaT"] 		= deltaT
case.control_dict["endTime"] 		= endTime
case.control_dict["writeInterval"]	= writeInterval

# bug: can't change time-step values as processor* dirs create duplicate startup timestep values
cmd0 = "sed -i -e 's/deltaT          0.0002/deltaT          "
cmd1 = "/g' ../combined/processor*/0.001/uniform/time"
os.system(cmd0 + str(deltaT) + cmd1)

# show progress check of computation
import time
from multiprocessing import Process
from rich.progress import Progress

def latestTimeLog(fname, numbLines):
    with open(fname) as file:
        for line in (file.readlines() [-numbLines:]):
            if line[:4] == "Time":
                return line[7:].strip('s\n')

def printWhile():
	timeD = 0
	fname = '../combined/log.foamRun'
	numbLines = 70
	timeLatestF = float(0.0)
	with Progress() as progress:
		task1 = progress.add_task("-> computation processing", total=endTime)
		while not progress.finished:
			timePreviousF = timeLatestF
			timeLatest = latestTimeLog(fname, numbLines)
			timeLatestF = float(timeLatest)
			deltaTF = timeLatestF - timePreviousF
			progress.update(task1, advance=deltaTF)
			time.sleep(15)
	return 0

def caseRun():
	case.run()

# execute computation & progress check in parallel
pCase = Process(target=caseRun)
pPrint = Process(target=printWhile)
pCase.start()
time.sleep(0.1)
pPrint.start()
pCase.join()
pPrint.join()

# cleanup
print("-> computation post-processing...")
case.reconstruct_par()
os.system("sudo cp -r ../combined/log.foamRun ./caseOutput.log")
print("-> computation completed!")