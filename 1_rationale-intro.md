## Rationale
Some researchers argue that face masks likely don't have the level of protection they claim [1] in real-world scenarios [^1]. Thus, we propose face shields may be a suitable alternative with more protection stability, even when worn improperly, as compared to masks. We consider this particularly important when virus transmission is dominated by the airborne route, such as COVID-19 [2].

To assess the protective ability of shields requires we understand and quantify the airflow dynamics around them. We limit ourselves to investigating the fluid dynamics of an interaction between two people in a common settings such as when speaking in no-velocity (surrounding) airflow environments which could represent places such as hospitals, schools/universities, and offices.

## Introduction
The fluid dynamics of speech-driven airflow comprises a combination of likely turbulent jet flow and potentially two-phase flow [3]. A turbulent jet normally appears emanating from the person speaking, which is carried forwards. Droplets containing the virus, also present in speaking, tend to fall towards the ground at increasingly shorter distances for higher sizes, while increasingly smaller-sized ones tend to follow the airflow pattern more closely. Using imaging methods, researchers have filmed the movement of tiny droplets from a person speaking different phrases.

[<img src="https://img.youtube.com/vi/yij0M-w32_g/hqdefault.jpg" width="800" height="600"
/>](https://www.youtube.com/embed/yij0M-w32_g)
<p align = "center">
Video introducing the fluid dynamics of speech-driven flow [4].
</p>
 
>"When you ask what is speech, it's these individual sounds that you're making, all of which add up if you're continually speaking. And in that sense, it's a packet of puffs or puff packets.
>
>We found that phrases that use sounds with a 'p' or 'b' make and scatter droplets at a greater rate than other phrases.
>
>Now if you say that 'Peter Piper picked a peck,' which we did, and you say that a few times, after 20 seconds of speaking, all the exhalations that have been created have easily propagated 2 meters, if not more, in 20 to 30 seconds of speaking. 
>
>In this case I think he's saying, 'sing a song of six pence.' Again, the upper image is what we see with a camera that's looking at the laser sheet. And then the big end of the sentence -- the 'sing a song,' you don't see much -- the end of the sentence, 'pence,' you see this big vortex come flying out."
>
> Prof. Howard A. Stone

Interestingly, plosive sounds (e.g. 'k' & 'p' sounds) that could be expected to affect the flow downstream (due their relatively higher momentum as compared to non-plosive speech) have been modelled as relatively insignificantly affecting the flow [5], thus steady-state boundary conditions may suffice for more macro flow qualities. However, the modelling assumption of no change in mouth size during production of such plosives is questionable at an instantaneous flow level.

If a face mask is worn by the infected person while speaking the overall jet momentum may be reduced significantly, however the breakup of droplets may cause the other person to inhale more of the virus, due to the smaller droplet sizes (which reach further than droplets). If a face shield is worn by the infected person the transmission of particles (representing a virus) to the other person has been shown to be decreased [6].

## Further details
The scope of the scenario under investigation & and the numerical-based methodology used in the investigation can be found in the [next section](https://github.com/TessellateDataScience/faceShieldOptimisations/blob/main/2_scope-methodology.md).

## References
1. Analytical and numerical investigation of the airflow in face masks used for protection against COVID-19 virus - implications for mask design and usage: https://arxiv.org/abs/2005.08800  
2. Wikipedia: Transmission of COVID-19: https://en.wikipedia.org/wiki/Transmission_of_COVID-19
3. The Fluid Dynamics of Disease Transmission: https://www.annualreviews.org/doi/10.1146/annurev-fluid-060220-113712
4. Inside Science: Speaking Spreads Exhaled Droplets: https://www.insidescience.org/video/speaking-spreads-exhaled-droplets  
5. Speech can produce jet-like transport relevant to asymptomatic spreading of virus: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7568291/  
6.  a) Experimental Investigation of the Flow Structure on a Face Mannequin With / Without a Face Shield: https://dergipark.org.tr/en/download/article-file/1675241  
    b) Experimental Efficacy of the Face Shield and the Mask against Emitted and Potentially Received Particles: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7922468/  
    
[^1]: We note that the researchers (Peric & Peric) didn't provide any real-world validation to show their calculations empirically agreed, casting some doubt on their conclusions.
