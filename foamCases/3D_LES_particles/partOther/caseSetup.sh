#! /bin/bash

# GMSH: install then launch IPython

# Create geometry/mesh of most of domain (not including region surrounding shield/head/body)
%run ./geoMesh/mesh3d_nonConform_shieldBox.py

# Import mesh to OpenFOAM format
#rm -rf ./constant/polyMesh  
gmshToFoam mesh3d_nonConform_shieldBox.msh 
checkMesh