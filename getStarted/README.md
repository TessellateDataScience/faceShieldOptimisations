# Predicting bioaerosols motion during speaking using _computational fluid dynamics_
## Health inequity
Health is a fundamental right of everyone on this planet, according to the World Health Organization:
- Vaccines for COVID-19 went mostly to rich countries, leaving poorer people last-in-queue:
  - 'Big Pharma' are some of the most-profitable companies in existance.

We think (tentatively) we can imagine some health-related innovations [-1] more equitably, let's state our broad assertion & some factors we thought of:
- A single face-shield ~ 20 times cheaper than a single vaccine dose, yet might have potential to provide protection against numerous viruses & diseases:
  - Less commercialisation hurdles. _Intellectual property_ involved in plastic manufacturing is less unique than in vaccine manufacturing.
  - More responsibility on people. Vaccines are more set-and-forget, whereas any PPE implies (human) behaviour change, and for the longer term.
  - More competition in the health 'industry'. Generally good for everyday people (end users):
    - Big Pharma has less power to influence and dictate the 'game'.

## Can we protect people from airborne-viruses using _personal protective equipment_?
At the least, PPE that is effective against airborne-virus transmission could benefit poorer folks, as a stop-gap measure until vaccines reach them. At the most, PPE could act as a disrupting technology to Big Pharma:
>   Can we demonstrate the efficacy of modified designs of face-shields against the transmission of airborne bioaerosols?  

Pandemics spread via both contact & non-contact routes. We're concentrating on airborne (non-contact) transmission, assuming contact transmission prevention will be achieved via cleaning (and other lower-cost methods).

## Innovating using a computational approach
We've developed a 'turnkey' application (software) that allows anyone with a computer to do fluid-dynamic research in an accessible way (without being a computational-science expert from the start). 

We view computational modelling as having the ability to advance the fundemental understanding of speech-driven airflow, while also providing the ability to compare differing PPE designs rapidly.

Our computational modelling predicts the motion of bioaerosols out of someone's mouth when speaking, while another person is listening to the speaker and breathing thru their nose.
- **_We're focussing on innovation that we hope could make larger progress for humanity as a whole_**:
    - Typical research grants are biased towards national issues of the funding country instead of 'global' issues - that far exceed rich countries' problems in scale and cost terms, usually.

_Do you value that everyone have access to healthcare as easily as we do in Western countries?_
 - You can do computational-based research to advance this cause (without the credentialism [0]):
   - Less impact on your ability to go to other 'work'.
   - Flexibility to research when you're more in your _flow_ state.
   - Ability to complement R&D with other more provocative endeavours [1].

We have the younger generation in mind, but we realise everyone can decide what's important to them at any age & stage.

### Getting started
Start the Docker Desktop app [2] and start the Terminal app [3], then copy/paste each line that follows to the 'terminal' then hit Enter (i.e. execute that 'command'):
```
mkdir foamDockEnv
cd ./foamDockEnv
docker run -it --mount "type=bind,src=$pwd,target=/home/foam" nchowlett/foam-tds:U22.1.1 sh
``` 

You're now able to launch computational investigations via the freely-available OpenFOAM software. First enable the pre-configured environment by executing:
```
su foam
. /opt/openfoam12/etc/bashrc
cd ..
ipython
```
You'll need to get `caseInput.py` from our [online repository](https://github.com/TessellateDataScience/faceShieldOptimisations/tree/main/getStarted) and save it in the `./foamDockEnv` directory. Then make a copy of OpenFOAM's case (input) directory to ensure reproducibility via `cp -r /home/foamFiles/combined /home/foam/case0`. This `case0` directory should now be viewable, and moreover modifiable without risk of messing up the computations more permanently, within your `foamDockEnv` directory.

### Running computations
Conduct a computational investigation by executing `%run ./caseInput.py`, after which you'll see overall indication of the computation's status. Allow the computation to complete, which should take ~ 2 minutes. 

If you have more than 4 cores available in your CPU, you can change the number to be allocated to the next computation. You'll need to modify `caseInput.py`, changing the relevant parameter's value:
```
...
numbCores = 4
...
```
Save the file then run the computation. After the computation is complete you can 
stop the platform by executing `exit` then `exit` again. Nice work, you've entered the digital realm of computational fluid dynamics! 

### Deeper intentions
Before you get carried away with excitement, realise you've simulated T = 0.003 seconds of the fluid dynamics. To have an adequate picture of what's happening overall for our scenario you'll probably need to simulate T ~ 45 [secs], which most likely take ~ 12 hours for a single computation. 

More positively, we're leveraging a server with loads of cores to run numerous computations simultaneously, with intention to increase confidence (reliability) such investigations, like yours above, are adequately accurate.

But, you might want to explore this recommended OpenFOAM reference [4] to more fully understand what is computing under-the-hood, if you're interested in further investigations of the fluid dynanics & differing PPE designs.

### Footnotes
[-1] CFD Online (Wiki) | CFD Application: Health & Medicine: https://www.cfd-online.com/Wiki/CFD_Application:_Health_and_Medicine  
[0] Saving you 3+ years of time due to not having to complete usually non-essential 'requirements' as part of research degree prerequisites).  
[1] Coursera | What Is Social Entrepreneurship? A Guide: https://www.coursera.org/articles/social-entrepreneurship  
[2] Docker | Installation: https://docs.docker.com/get-started/get-docker/  
[3] Terminal | Installation: https://learn.microsoft.com/en-us/windows/terminal/install  
[4] OpenFOAM Technology Primer: http://dx.doi.org/10.13140/2.1.2532.9600  
