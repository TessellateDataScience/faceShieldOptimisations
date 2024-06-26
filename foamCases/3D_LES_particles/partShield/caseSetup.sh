#! /bin/bash

# OpenFOAM v2312: install then activate environment (CMD): openfoam2312

# Shield geometry then mesh using cfMesh: https://cfd-training.com/2020/04/29/how-to-use-cfmesh-a-first-tutorial-based-on-the-ahmed-body/
cd ./geometry
rm ./shield.stl
openscad -o person.stl person.scad 	# OpenSCAD: install first
# put nostrils facets in own STL file: search for 'facet normal 0 0 ~(-1)' at vertex ~ Z = 20
rm combined.stl
cat back.stl front.stl sideL.stl sideR.stl top.stl bottom.stl person.stl >> combinedNoNostrils.stl
sed -i -e 's/OpenSCAD_Model/person/g' ./combinedNoNostrils.stl

# Thanks foamF for guidance on contraining edges of only part of geometry: https://www.cfd-online.com/Forums/openfoam-community-contributions/218983-openfoam-cfmesh-how-delete-edge-features-fms-file.html
rm nostrils.ftr
rm combined.ftr
surfaceFeatureEdges -angle 10 nostrils.stl nostrils.ftr
surfaceAdd combinedNoNostrils.ftr nostrils.ftr combined.ftr
cd ..
cp ./geoMesh/combined.ftr ./

# cfMesh commands: https://cfmesh.com/wp-content/uploads/2015/09/User_Guide-cfMesh_v1.1.pdf
cartesianMesh
checkMesh					# ensure no negative-volumed cells (see 'meshing.md')
# improveMeshQuality 		# cfMesh utility (sometimes doesn't improve mesh according to checkMesh)

# OpenFOAM v2312 close CMD: exit
transformPoints scale="(0.001 0.001 0.001)"