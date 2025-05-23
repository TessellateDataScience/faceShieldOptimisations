#! /bin/bash

# GMSH: install then launch IPython

# Create geometry/mesh of most of domain (not including region surrounding shield/head/body)
#%run ./geoMesh/mesh_cyl_downstream.py

# Import mesh to OpenFOAM format
rm -rf ./constant/polyMesh  
gmshToFoam mesh_cyl_downstream.msh 
transformPoints scale="(0.001 0.001 0.001)"
checkMesh