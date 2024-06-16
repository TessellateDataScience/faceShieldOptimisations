#! /bin/bash

# OpenFOAM v2312: install then activate environment

# Shield geometry then mesh using cfMesh: https://cfd-training.com/2020/04/29/how-to-use-cfmesh-a-first-tutorial-based-on-the-ahmed-body/
cd ./geoMesh
rm ./shield.stl
openscad -o person.stl person.scad 	# OpenSCAD: install first
rm combined.stl
# put nostrils facets in own STL file: search for 'facet normal 0 0 -1': vertices at Z=20
cat back.stl front.stl sideL.stl sideR.stl top.stl bottom.stl person.stl nostrils.stl >> combined.stl
sed -i -e 's/OpenSCAD_Model/person/g' ./combined.stl
cd ..
cp ./geoMesh/combined.stl ./

# cfMesh commands: https://cfmesh.com/wp-content/uploads/2015/09/User_Guide-cfMesh_v1.1.pdf
cartesianMesh
checkMesh					# ensure no negative-volumed cells (see 'meshing.md')
transformPoints scale="(0.001 0.001 0.001)"
# improveMeshQuality 		# cfMesh utility (sometimes doesn't improve mesh according to checkMesh)
