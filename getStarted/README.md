# Predicting bioaerosols motion during speaking: leveraging computational & citizen science
## Towards equitable health
Health is a fundamental right of everyone on this planet, according to the World Health Organization:
- Vaccines for COVID-19 went mostly to rich countries, leaving poorer people last-in-queue:
  - 'Big Pharma' are some of the most-profitable companies in existance.

We perhaps can do 'health innovation' more equitably, let's state our broad assertion & some factors we thought of:
- A single face-shield ~ 20 times cheaper than a single vaccine dose, yet might have potential to provide protection against numerous viruses & diseases:
  - Less commercialisation hurdles. _Intellectual property_ involved in plastic manufacturing is less unique than vaccine manufacturing.
  - More responsibility on people. Vaccines are relatively set-and-forget, whereas any PPE implies more (human) behaviour change, and for the longer term.
  - More competition in the health 'industry'. Generally good for everyday people:
    - Big Pharma has less power to influence and dictate.

## _Personal protective equipment_: airborne-virus protection?
At the least, PPE that is effective against airborne-virus transmission could benefit poorer folks, as a stop-gap measure until vaccines reach them. At the most, PPE could act as a disrupting technology to the pharmaceutical industry:
>   Can we demonstrate the efficacy of modified designs of face-shields against the transmission of airborne bioaerosols?  

Pandemics spread via both contact & non-contact routes. We're concentrating on non-contact airborne transmission, assuming contact transmission prevention will be effective via cleaning (and other lower-cost methods).

## Collaborative innovation: blending computational & citizen science
We've developed a 'turnkey' application (software) that allows anyone with a computer to do fluid dynamics research, relatively-easily. 

> - Want in do computational-science research (without the university credential fluff) [0]?
>   - Keep your work situation unchanged.
>   - Research when you're more in your 'flow' state.
>   - Complement your research with other activities, concurrently.

Our research predicts the motion of bioaerosols out of someone's mouth when speaking, while another person is listening to the speaker and breathing thru their nose (using 'computational fluid dynamics').
>- _We're focussing on paradigm-shifting innovation that we hope could make larger progress for humanity as a whole_. Instead of being primarily concerned with publication record & getting research grants (that are biased towards primarily national issues of the funding country). But this means we're each running without any financial assistance.

### Getting started
Start the Docker Desktop app [1] and start the Terminal app [2], then copy/paste each line that follows to the 'terminal' then hit Enter (i.e. execute that 'command'):
```
mkdir foamDockEnv
cd ./foamDockEnv
docker run -it --mount "type=bind,src=$pwd,target=/home/foam/files" nchowlett/foam-tds:1.4 sh
``` 

You're now able to launch computational investigations via the freely-available OpenFOAM software. First enable the pre-configured environment by executing:
```
. /.venv/bin/activate
cd ./files
ipython
```

### Running computations
Conduct a computational investigation by executing `%run ./caseInput.py`, after which you'll see overall indication of the computation's status. Allow the computation to complete, which should take ~ 2 minutes. 

If you don't have 4 cores available in your CPU, you can change the number to be used during the next computation. You'll need to modify `caseInput.py`, changing the relevant parameter's value:
```
...
numbCores = 4
...
```
Save the file then run the computation. After the computation is complete you can 
stop the platform by executing `exit` then `exit` again. Nice work, you've entered the digital realm of computational science! 

### Deeper intentions
But before you get carried away with excitement, realise you've simulated only 0.003 seconds of the 'fluid dynamics', yet to have a reasonable picture of what's happening overall for our scenario you'll probably need to simulate for 45 [secs] (which most likely take ~ 12 hours to complete). 

Note, we're leveraging a server with loads of cores to run numerous computations simultaneously. Hopefully increasing confidence (reliability) such investigations, like yours above, are accurate enough for our intention.

### Footnotes
[0] Saving you atlest 3+ years of time due to not having to complete usually non-essential 'requirements' as part of degree prerequisites).  
[1] Docker installation: https://docs.docker.com/get-started/get-docker/  
[2] Terminal installation: https://learn.microsoft.com/en-us/windows/terminal/install  
