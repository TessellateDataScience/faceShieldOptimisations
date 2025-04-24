# Getting started with computational modelling of speech-driven airflow between two people
We've developed a 'turnkey' application (software) that allows anyone with a computer to do some fluid-dynamic research in an accessible way, without being a computational-science expert from the start. 

## Motivated enough?
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
Conduct a computational investigation by executing `%run ./caseInput.py`, after which you'll see overall indication of the computation's status. Allow the computation to complete, which should take ~ 2 minutes. 

If you have more than 4 cores available in your CPU, you can change the number to be allocated to the next computation. You'll need to modify `caseInput.py`, changing the relevant parameter's value:
```
...
numbCores = 4
...
```
Save the file then run the computation. After the computation is complete you can stop our computatinal platform ('env') by executing `exit` then `exit` again. Nice work, you've entered the digital realm of computational fluid dynamics! 

## Longer computations
Before you get carried away with excitement, realise you've simulated T = 0.003 seconds of the fluid dynamics, yet to have an adequate picture of what's happening overall for our scenario you'll probably need to simulate T ~ 45 [secs], which most likely take ~ 48 hours for a single computation. To increase the time simulated modify `caseInput.py` again, this time changing the `endTime` parameter to	= 45.0 (while changing `writeInterval` to ~ 5.0). Then run a computational investigation after saving that file.

As an aside, we're leveraging a server with loads of cores to run numerous computations simultaneously, with intention to increase confidence (reliability) such investigations, like yours above, are adequately accurate. But, you might want to explore a recommended OpenFOAM reference [4] to more fully understand what is computing under-the-hood, if you're interested in further investigations of the fluid dynamics & changing PPE designs.

## Footnotes
[0] Saving you 3+ years of time due to not having to complete usually non-essential 'requirements' as part of research degree prerequisites).  
[1] Coursera | What Is Social Entrepreneurship? A Guide: https://www.coursera.org/articles/social-entrepreneurship  
[2] Docker | Installation: https://docs.docker.com/get-started/get-docker/  
[3] Terminal | Installation: https://learn.microsoft.com/en-us/windows/terminal/install  
[4] OpenFOAM Technology Primer: http://dx.doi.org/10.13140/2.1.2532.9600  
