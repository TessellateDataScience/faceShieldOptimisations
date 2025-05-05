# Getting started with computational modelling of speech-driven airflow between two people
We've developed a 'turnkey' application (software) that allows anyone with a computer to do some fluid-dynamic research in an accessible way, without being a computational-science expert from the start. 

## Motivation: is their life good enough?
_Do you value that everyone have access to healthcare as easily as we do in Western countries?_
 - You can do computational-based research to advance this cause (without the credentialism [0]):
   - Less impact on your ability to go to other 'work'.
   - Flexibility to research when you're more in your _flow_ state.
   - Ability to complement R&D with other more provocative endeavours [1].

We have the younger generation in mind, but we realise everyone can decide what's important to them at any age & stage.

## Getting started
Start the Docker Desktop app [2] and start the Terminal app [3], then copy/paste each line that follows to the 'terminal' then hit Enter (i.e. execute that 'command'):
```
mkdir foamDockEnv
cd ./foamDockEnv
docker run -it --mount "type=bind,src=$pwd,target=/home/foam" nchowlett/foam-tds:U22.1.5 sh
``` 

You're now able to launch computational investigations via the freely-available OpenFOAM software. First enable the pre-configured environment by executing:
```
su foam
. /opt/openfoam12/etc/bashrc
cd ..
ipython
```
You'll need to get `caseInput.py` from our [online repository](https://github.com/TessellateDataScience/faceShieldOptimisations/tree/main/getStarted) and save it in the `./foamDockEnv` directory. Then make a copy of OpenFOAM's case (input) directory to ensure reproducibility via `cp -r /home/foamFiles/combined /home/foam/case0`. This `case0` directory should now be viewable, and moreover modifiable without risk of messing up the computations more permanently, within your `foamDockEnv` directory.

## Running computations
Conduct a computational investigation by executing `%run ./caseInput.py`, during which you'll get an indication of the computation's progress. Allow the computation to complete, which should take ~ 1 hour. 

If you have more than 4 cores available in your CPU, you can change the number to be allocated to the next computation. You'll need to modify `caseInput.py`, changing the relevant parameter's value:
```
...
numbCores = 8
...
```
Save the file then run the computation. After the computation is complete you can stop our computatinal platform ('env') by executing `exit` then `exit` again. Nice work, you've entered the digital realm of computational fluid dynamics! 

## Longer computations
Before you get carried away with excitement, realise you've simulated 1.0 seconds of the fluid dynamics, yet to have an adequate picture of what's happening overall for our scenario you'll probably need to simulate T ~ 45 [secs]. To increase the time simulated modify `caseInput.py` again, this time changing the `endTime` parameter to	= 45.0. Then run a computational investigation after saving that file.

As an aside, we're leveraging a server with loads of cores to run numerous computations simultaneously, with intention to increase confidence (reliability) such investigations, like yours above, are adequately accurate. But, you might want to explore a recommended OpenFOAM reference [4] to more fully understand what is computing under-the-hood, if you're interested in further investigations of the fluid dynamics & changing PPE designs.

## Novel design of face shield
The computation above simulates flow around a 'normal' face shield. We've also provided a 'novel' design where surfaces cover the bottom and sides (with a gap near the wearer's face). Salient differences between these designs are shown below:

<img src="shieldNormalMod.png" width="500" height="450"/> <img src="shieldEnclosedMod.png" width="500" height="450"/> 
<p align="center"><i>
  Computer-aided design representation of 2 differing face-shield designs: 'normal' status-quo product (left), and 'novel' commercially-unavailable product (right). Both products are thinner than they are represented by this CAD (with a real thickness similar to currently-available face-shields).
</i></p>

To run identical computations across these differing designs (effectively a perfect A/B Test), you need to load the enclosed face-shield 'geometry' data. To do this, `cd ../../foamFiles` to go to the source files, then `git log` to show the differing geometry data available. To make the enclosed face-shield geometry active, `git checkout 9988d9` (the first 6 digits of the commit number).

You'll then need to rebuild the case. First `cd ./combined` then `bash caseSetup.sh`. Let the environment do it's thing, and if all is well you'll see 'Mesh OK' after `checkMesh`. Save your previous 'case0' as another name, then copy the new case to your working directory via `cp -r /home/foamFiles/combined /home/foam/caseNovel`. Finally run a computation of airflow around the novel shield. 

## Analysis of designs
We've developed code that uses [pyVista](https://pyvista.org/) within a [Jupyter](https://jupyter.org/) environment. To enable this 'post-processing' environment, exit the computational env. then execute `docker run -it -v "$(pwd):/home/jovyan/work" -p 8888:8888 ghcr.io/pyvista/pyvista:latest`. Once the environment is loaded, copy then paste the URL (similar to 'http://127.0.0.1:8888/lab?token=139...') into your web browser (Chrome, Firefox, etc). 

Select 'Python' under 'Notebook', then click on the `work` directory (on left side). To run our analysis on your computations, download `dataAnalysis.ipynb` into your 'working' directory (`foamDockEnv`) then open that notebook (visible within `work` directory). Run that notebook using the 'double play' button. You show see bioaerosols' trajectories appear below the last 'cell'. If you get an error (shown in red), you will probably have to change the 'path' to your case data, or comment out some lines in each `0/*` file via `//#includeEtc "caseDicts/setConstraintTypes"`.

## Footnotes
[0] Saving you 3+ years of time due to not having to complete usually non-essential 'requirements' as part of research degree prerequisites).  
[1] Coursera | What Is Social Entrepreneurship? A Guide: https://www.coursera.org/articles/social-entrepreneurship  
[2] Docker | Installation: https://docs.docker.com/get-started/get-docker/  
[3] Terminal | Installation: https://learn.microsoft.com/en-us/windows/terminal/install  
[4] OpenFOAM Technology Primer: http://dx.doi.org/10.13140/2.1.2532.9600  
