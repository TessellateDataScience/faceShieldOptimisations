# README: OpenFOAM simulations
## Summary
Our cases (simulation configuration files) are developed/testing in OpenFOAM version 10. Prior to running OpenFOAM, our mesh (and geometry) was developed using GMSH 4.11. Below is some advice for getting your computations functioning.

## GMSH
- View the geometry/mesh before debugging.  
- Using combination of geo/occ module: results in successful execution but no meshed elements.  
- Sometimes GMSH complains it's 'too busy', simply reload IPython and try again.

### Mesh
Using checkMesh often resulted in excessive 'Aspect Ratio' of some cells that caused the utility to flag errors (and thus crash the solver when executed). This was usually due to triangular grids having poor topology, which could be overcome by changing triangular mesh sizes.

## OpenFOAM
OpenFOAM's software is designed where errors leave a 'trace' of bad code it finds (usually syntax-related). In particular 'Boundary Conditions' (BCs) have scarce documentation online, but there are other means to get more information, including: 
- Finding all available BCs available using `<solverName -listScalarBCs -listVectorBCs`, then getting more details of a particular BC using `foamInfo <nameOfBC>`.
- Using 'banana' trick of inserting this dummy value to gain more details via OpenFOAM's error message. 