#! /bin/bash

# Convert mesh to native format
rm -rf ./constant/polyMesh  
gmshToFoam mesh3d_shieldComplex_noHead.msh  
transformPoints scale="(0.001 0.001 0.001)"  

# remove 'bad', namely negative-volumed, cells from mesh (adapted from): 
#	https://www.youtube.com/watch?v=yKNAr8Lh4-M
#	https://github.com/OpenFOAM/OpenFOAM-10/blob/master/etc/caseDicts/annotated/topoSetDict
#topoSet
#subsetMesh c1 -overwrite

# Replace 'internal' with 'patch' in /boundary/oldInternalFaces/, then 
# replace 'internal' with semi-appropriate conditions in 0/*/oldInternalFaces/