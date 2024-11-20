#! /bin/bash

# geometry creation for cfMesh: https://cfd-training.com/2020/04/29/how-to-use-cfmesh-a-first-tutorial-based-on-the-ahmed-body/
cd ./geometry
rm ./person.stl
openscad -o person.stl person.scad 	# OpenSCAD: install first
python nostrilsExtract.py
rm combinedNoNostrils.stl
cat box.stl personNoNostrils.stl >> combinedNoNostrils.stl
sed -i -e 's/OpenSCAD_Model/person/g' ./combinedNoNostrils.stl
rm combined.stl
cat combinedNoNostrils.stl nostrils.stl >> combined.stl
cd ..
rm combined.stl
cp ./geometry/combined.stl ./

# cfMesh commands: https://cfmesh.com/wp-content/uploads/2015/09/User_Guide-cfMesh_v1.1.pdf
openfoam2312 cartesianMesh
transformPoints scale="(0.001 0.001 0.001)"
checkMesh							# ensure no negative-volumed cells (see 'meshing.md')
# openfoam2312 improveMeshQuality 	# cfMesh utility (sometimes doesn't improve mesh)