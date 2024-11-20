#! /bin/bash
#
# Merge meshes: cube & cylinder (downstream)

rm -r ./constant/polyMesh/
rm -r ./coonstant/fvMesh/
cp -r ../partDownstr/constant/polyMesh/ ./constant/
mergeMeshes -overwrite -addCases '("../partPerson")'
createNonConformalCouples -overwrite iFaceCube iFaceDownCube