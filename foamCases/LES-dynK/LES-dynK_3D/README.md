# README: LES dynK 3D
## Summary
This model (case) is a 3-dimensional flow representation. Briefly, we have included modelling of a 'shield' but no person's head in domain (you can use our geom/mesh file that is also within this repository). We envision this case can be developed upon concentrating upon research of jet flow around a bluff body (i.e. of a more fundamental research nature).

## Modelling
Our model is based on a Large Eddy Simulation method where subgrid-sized turbulence is modelled using the 'dynamicKEqn' approach [1] (larger-sized turbulence is resolved by the computation). Note we have access to significantly larger computing performance compared to a standard computer (also known as High-Performance Computing), permitting us more tractable compute times for such compute-heavy LES modelling (as compared to lighter RANS modelling).

## Meshing
You need to create the domain of interest then mesh this domain, before simulating this domain using OpenFOAM. We did this using _Gmsh_, open-source software that has extensive functionality that can be more exploited via it's command-line interface (as compared to it's graphical interface). We used Gmsh's Python interface to interact with Gmsh's core functionality, within the IPython environment.
```
%run ./geoMesh/mesh3d_shieldComplex_noHead.py  
```

## Quality
Once the mesh is created, convert it into OpenFOAM's native formatting. Then run an OpenFOAM Utility program that checks the mesh quality.

```
bash caseSetup.sh  
checkMesh  
```

Ensure no negative-volumed cells are seen, as they can cause 'segmentation faults' when your solver is executed. Our mesh quality was very sensitive to changes in meshSize (changing by deltaMeshSize ~ 0.000001 resulted in our solver's time improving from deltaT ~ 1e-20 to deltaT ~ 1e-6). Qualitatively the chosen mesh achieved significantly better checkMesh results, specifically the 'geometry' checks were mostly passed (see 'checkMesh_output' for more details). 

## Solving
You can start the solver using the name of the solver. Once started, the solver will iterate and solve fluid-dynamic equations over each time-step (until your defined end-time is reached).

```
pimpleFoam  
```

Your deltaT ~ 1e-06 (if using our mesh, as is), if not you likely have mesh quality issues (perhaps due to differences in your OpenFOAM version to our version). To stop (interrupt) the solving process find the solver process ID then 'kill' this process ID. We are running Version 10 of OpenFOAM.
```
ps  
kill -9 <PID>  
```

## Further reading
[1] OpenFOAM's source-code: turbulence models available: https://cpp.openfoam.org/v11/namespaceFoam_1_1LESModels.html  
[2] OpenFOAM's documentation (_User Guide_): https://doc.cfd.direct/openfoam/user-guide-v10/