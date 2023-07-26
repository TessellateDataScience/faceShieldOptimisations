# README: ParticleTracking
## Summary
This OpenFOAM case is to be executed after you have solved your fluid field. Once you have time directories, copy all of them into this directory (i.e the folder structure is the same as other cases). Then execute `particleFoam`, which writes particle data to these folders (while using the velocities at these times). Note that `particleFoam` is only part of CFD Direct's OpenFOAM releases (e.g. version 11) not OpenCFD's versions (e.g. version 2306).

## Further information
While particleFoam executes in an independent manner (particle equations are solved independently and after fluid equations have been solved), OpenCFD's particle tracking solvers appear to be tied together with the fluid solvers (thus a full computation of the fluid field is required to get any new particle tracking data). We opted for CFD Direct's releases to allow faster iteration of overall particle tracking development.

## Technical details
OpenFOAM has implmented particle tracking (using Discrete Element Method) since version 2 [1]. As part of this, from version 4 the software injects a particle at a random point adjacent to the patch faces (when using patchInjection [2] within the injectionModels dictionary), suggesting a stochastic-driven process.

Such a random-like generation is not inconsistent with our lack of understanding of the fluid dynamics of air being breathed out from the mouth, and in particular the airborne virus distribution throughout the volume. Similarly, the actual size distribution of the virus 'particles' are perhaps more appropriately modelled using a more random function (and not a single size). 

However, the forces acting upon the virus-laiden particles perhaps cannot be simplified to a rigid sphere without significant deviation of position downstream at the shield.

## Further development
1. Conversion of particle's position data from Barycentric to Cartesian.
2. Time-step sensitivity studies.
3. Numerical parameters' validation & optimisation.

## Further reading
[1] https://openfoam.org/release/2-0-0/particle-tracking
[2] https://cpp.openfoam.org/v4/patchInjectionBase_8H_source.html