# OpenFOAM simulation setup
## General advice
General:  
- run 'caseSetup' from start each time (to remove errors)  

Meshing:  
- view the geometry/mesh before debugging.  
- common issues: syntax: using combination of geo/occ module: results in successful execution but no mesh elements.  

Internal surfaces:  
- create using Foam utilities (no entity in boundary file on mesh creation):  
	- see /system/topoSetDict & /system/createBafflesDict.  
- https://github.com/OpenFOAM/OpenFOAM-10/tree/master/tutorials/incompressible/pimpleFoam/RAS/TJunctionFan  
- https://github.com/OpenFOAM/OpenFOAM-4.x/tree/master/applications/utilities/mesh/manipulation/createBaffles  

DES:  
- https://www.youtube.com/watch?v=q_lWmfgkZsU  

## caseSetup
```
[ipython] %run ./mesh.py  
rm -rf ./constant/polyMesh  
gmshToFoam mesh.msh  
transformPoints scale="(0.001 0.001 0.001)"  
topoSet  
createBaffles -overwrite  
checkMesh  
pisoFoam  
ps  
kill -9 <PID>  
```

## Further development
1. Mesh refinement adjacent the shield.  
2. Numerical parameters adjustment.  
3. Grid sensitivity study.
4. Turbulence parameters optimisation.