#! /bin/bash

# OpenFOAM v2312: install then activate environment

# Shield geometry then mesh using cfMesh: https://cfd-training.com/2020/04/29/how-to-use-cfmesh-a-first-tutorial-based-on-the-ahmed-body/
cd ./geoMesh
rm ./shield.stl
openscad -o shield.stl shieldHeadBody.scad 	# OpenSCAD: install first
rm combined.stl
cat back.stl front.stl sideL.stl sideR.stl top.stl bottom.stl shield.stl >> combined.stl

# cfMesh commands: https://cfmesh.com/wp-content/uploads/2015/09/User_Guide-cfMesh_v1.1.pdf
surfaceFeatureEdges -angle 5 combined.stl combined.fms
cd ..
cp ./geoMesh/combined.fms ./
sed -i -e 's/OpenSCAD_Model/shield/g' ./combined.fms

cartesianMesh
# checkMesh					# ensure no negative-volumed cells (see 'meshing.md')
# improveMeshQuality 		# cfMesh utility (sometimes doesn't improve mesh according to checkMesh)
