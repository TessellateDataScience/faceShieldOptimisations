# README: LES 2D
## Summary
This model (case) is simplified for efficient development/testing via a 2-dimensional flow representation (you can use our geom/mesh file: mesh2dJet_rotationShield_nose.py). Briefly, we have included modelling of both a 'shield' & person's head objects in domain. This geometry allows a boundary condition to be applied at the person's nose. 

## Modelling
Our model is based on a Large Eddy Simulation method where subgrid-sized turbulence is modelled using the 'dynamicKEqn' approach [1] (larger-sized turbulence is resolved by the computation). 

## Meshing
You need to create the domain of interest then mesh this domain, before simulating this domain using OpenFOAM. We did this using _Gmsh_, open-source software that has extensive functionality that can be more exploited via it's command-line interface (as compared to it's graphical interface). We used Gmsh's Python interface to interact with Gmsh's core functionality, within the IPython environment.
```
%run ./mesh2dJet_rotationShield_nose.py  
```

## Quality
Once the mesh is created, convert it into OpenFOAM's native formatting. Then run an OpenFOAM Utility program that checks the mesh quality.

```
rm -rf ./constant/polyMesh  
gmshToFoam mesh.msh  
transformPoints scale="(0.001 0.001 0.001)"   
checkMesh  
```
Your 'constant/polyMesh/boundary' file needs manual modification after mesh creation, changing patch type of all solid boundaries to 'wall' and specifying 'empty' for the _empty_ patch. If `checkMesh` flags errors of high 'Aspect Ratio' cells, you can visually inspect their location via writing the cells data via `foamToVTK -cellSet highAspectRatioCells` [2] then viewing them in _ParaView_. You first need to load 'case.foam' in ParaView, then load the '<name>.vtk' to see these cells.

## Solving 
You can start the solver using the name of the solver. Once started, the solver will iterate and solve fluid-dynamic equations over each time-step (until your defined end-time is reached).

```
pimpleFoam  
ps  
kill -9 <PID>  
```
To stop (interrupt) the solving process find the solver process ID then 'kill' this process ID. We are running Version 10 of OpenFOAM.

## Further reading
[1] OpenFOAM's source-code: turbulence models available: https://cpp.openfoam.org/v11/namespaceFoam_1_1LESModels.html  
[2] OpenFOAM's documentation (_User Guide_): https://doc.cfd.direct/openfoam/user-guide-v10/