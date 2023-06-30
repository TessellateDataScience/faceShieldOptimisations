# SpecifiedVel-2D
## Summary
This case is a simplier 2-dimensional simulation to allow easier debugging of technical OpenFOAM issues. Also could provide quicker assessment of appropriate modelling choices (such as particular 'boundary conditions').

## Notes
- velocity specified at mouth (unlike IDDES-SpalAll that specifies pressure).
- no internal surfaces created (unlike 'IDDES-SpalAll' case).
- geometry/meshing done using Salome 9.8.0 software (not GMSH).

## Case setup
```
# using base mesh file
ideasUnvToFoam meshFile.unv  
transformPoints scale="(0.01 0.01 0.01)"  

# using pre-existing polyMesh
checkMesh  
pisoFoam  
ps  
kill -9 <PID>  
```