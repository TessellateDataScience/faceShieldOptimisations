# README: OpenFOAM simulations
## Summary
Our cases (simulation configuration files) are developed/testing in OpenFOAM version 10. Prior to running OpenFOAM, our mesh (and geometry) was developed using GMSH 4.11. Below is some advice for getting your computations functioning:

## Meshing 
- view the geometry/mesh before debugging.  
- using combination of geo/occ module: results in successful execution but no meshed elements.  
- sometimes GMSH complains it's 'too busy', simply reload IPython and try again.

## Checking mesh
- when using checkMesh utility: 
	- ensure the 'shield' patches have been created properly.
	- ensure you receive 'OK' for your mesh.

## OpenFOAM
- Software design of errors leaving 'trace' of code issues (usually syntax-related, especially lacking definitions due to scarce documentation).
- use 'banana trick' of inserting this dummy value to gain more details from OpenFOAM of exact syntax to use. 