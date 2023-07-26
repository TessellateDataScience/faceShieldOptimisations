# README: ParticleTracking
## Summary
This OpenFOAM case is to be executed after you have solved your fluid field. Once you have time directories, copy all of them into this directory (i.e the folder structure is the same as other cases). Then execute `particleFoam`, which writes particle data to these folders (while using the velocities at these times). Note that `particleFoam` is only part of CFD Direct's OpenFOAM releases (e.g. version 11) not OpenCFD's versions (e.g. version 2306).

## Further information
While particleFoam executes in an independent manner (particle equations are solved independently and after fluid equations have been solved), OpenCFD's particle tracking solvers appear to be tied together with the fluid solvers (thus a full computation of the fluid field is required to get any new particle tracking data). We opted for CFD Direct's releases to allow faster iteration of overall particle tracking development.

## Further development
1. Random placement of particles upon injection.
2. Time-step sensitivity studies.
3. Numerical parameters optimisation.