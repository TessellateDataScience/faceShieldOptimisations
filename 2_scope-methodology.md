## Scope
Although the inhalation of droplets may be reduced significantly if a face shield is worn by the virus-free person [5], we assert this effectivness may still be improved if we redesign this shield to reduce even more the proportion of smaller-sized droplets into the nose. 

To do this we first aim to check the effectiveness of face shields that are currently commercially available. Then we will investigate the effectiveness of a proposed novel face shield, and compare the results.

Our investigation will focus on varying particular variables, including:
- 'viral load' of person speaking,
- source velocity (momentum), 
- depth of face shield relative from it's front to the wearer's face, and
- non-conventional design modifications of the shield itself.

These scenarios will both be investigated with the assumption that the person not speaking will be inhaling at their maximum volumetric rate, and inhaling fully thru their nose. The speaking person's jet characteristics will be idealised, based on experimental data [6] where available, and assumed to point directly towards the wearer of the shield. The environment near the jet will also be assumed to have zero flow. The face shield's dimensional characteristics will be averaged from common, commercially-available products [^1].

## Methodology
Computational Fluid Dynamics (CFD) will be used to conduct a number of numerical experiments where various parameters are varied. To achieve this the [OpenFOAM](https://openfoam.org/) software will be used to run numerous CFD simulations on self-owned infrastructure.

This finite-volume CFD approach may include both lower computational-cost (Unsteady Reynolds Averaged Navier-Stokes) and higher-cost (Large Eddy Simulations) turbulence modelling of the airflow created due to speaking. Due to the speaker's volume variation, transition modelling may also be required. The person inhaling will be represented as a simplified geometry based upon [NIOSH](https://www.cdc.gov/niosh/data/datasets/rd-10130-2020-0/default.html).

Due to our non-empirical experimental method, certain activities such as validation and verification should be also undertaken to provide confidence our numerical experiments are accurate reflections of the 'real-world', while also ensuring error introduced by the numerical methods are non-significant. A selection of turbulence models (that are pre-judged as applicable yet have significantly different computational requirements) will be used and their modelling results assessed. Specifically our numerical results will be validated against experimental results, similar to some already experimentally investigated [7, 8]. We will also verify the insensitivity of numerical results to numerically-based parameters used to generate these results, focussing especially on turbulence-related methods and parameters (but also including geometry). 

## References
5.  a) Experimental Investigation of the Flow Structure on a Face Mannequin With / Without a Face Shield: https://dergipark.org.tr/en/download/article-file/1675241  
    b) Experimental Efficacy of the Face Shield and the Mask against Emitted and Potentially Received Particles: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7922468/
6. Characterizing exhaled airflow from breathing and talking: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1600-0668.2009.00623.x
7. Experimental and computational study of a high-Reynolds jet flow: https://tspace.library.utoronto.ca/bitstream/1807/77669/1/cjce-2016-0433.pdf
8. Breathing, virus transmission, and social distancing — An experimental visualization study: https://aip.scitation.org/doi/full/10.1063/5.0045582 

[^1]: Product A: https://www.medcart.com.au/a/face-shields-surgical-visors/werkomed/face-shield-with-clear-visor/100041747?variant_id=114178, product B: https://www.medcart.com.au/a/face-shields-surgical-visors/hlp-medical-supplies/act/kaleen/double-side-anti-fog-coated-face-shield-face-protection-1-shield/100043782?variant_id=117564, product C: https://www.medcart.com.au/a/face-shields-surgical-visors/ethical-pharmacy-supplies/nsw/yagoona/disposable-full-face-shield/100042218?variant_id=115725.
