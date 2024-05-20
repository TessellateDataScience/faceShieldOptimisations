#! /bin/bash

# OpenFOAM v2312: install then activate environment: `openfoam2312`

# Shield geometry then mesh using cfMesh: https://cfd-training.com/2020/04/29/how-to-use-cfmesh-a-first-tutorial-based-on-the-ahmed-body/
cd ./geoMesh
#rm ./shield.stl
openscad -o shield.stl shieldHeadBody.scad 	# OpenSCAD: install first
rm combined.stl
cat back.stl front.stl sideL.stl sideR.stl top.stl bottom.stl shield.stl >> combined.stl
#surfaceFeatureEdges -angle 5 combined.stl combined.fms
cd ..
cp ./geoMesh/combined.stl ./
sed -i -e 's/OpenSCAD_Model/shield/g' ./combined.stl

cartesianMesh
# checkMesh					# ensure no negative-volumed cells (see 'meshing.md')
# improveMeshQuality 		# cfMesh utility (inconsistent improvement)
