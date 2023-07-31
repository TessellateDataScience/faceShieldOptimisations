# README: LES dynK
## Summary
This model (case) is simplified for efficient development/testing via a 2-dimensional flow representation (you can use our geom/mesh file: mesh2dJet_withShield_noHeads.py). But we have included modelling of the 'shield' object in domain via using OpenFoam's baffles creation (see below for implementation code). 

## Technical details
Our model is based on a Large Eddy Simulation method where subgrid-sized turbulence is modelled using the 'dynamicKEqn' approach [1] (larger-sized turbulence is resolved by the computation). Wall functions have also been used to allow grid size relaxation towards solid boundaries. Note we have access to significant computing hardware performance (also known as High-Performance Computing), permitting us reasonable compute times for such compute-heavy LES modelling (as compared to faster RANS modelling).

## Case setup
```
[ipython] %run ./mesh.py  
rm -rf ./constant/polyMesh  
gmshToFoam mesh.msh  
transformPoints scale="(0.001 0.001 0.001)"  
topoSet  
createBaffles -overwrite  
checkMesh  
pimpleFoam  
ps  
kill -9 <PID>  
```
Your 'constant/polyMesh/boundary' file needs manual modification after mesh creation, changing patch type of all solid boundaries to 'wall' and specifying 'empty' for the _empty_ patch. If you wish to change the boundary conditions at the 'shield', modify /system/createBafflesDict not /0/* files.

## Further development 
1. Grid/time sensitivity analysis.
2. Turbulence parameters optimisation.  

## Further reading
[1] See the current OpenFOAM version's source code for more info on turbulence models available: https://cpp.openfoam.org/v11/namespaceFoam_1_1LESModels.html  