#! /bin/bash

cd ../partPerson
bash caseSetup.sh

cd ../partDownstrComb
bash caseSetup.sh 

cd ../combined
rm -r ./constant/polyMesh/
rm -r ./constant/fvMesh/
cp -r ../partUpstr/constant/polyMesh/ ./constant/
mergeMeshes -overwrite -addCases '("../partDownstrComb")'

# https://cfd.direct/openfoam/free-software/using-non-conformal-coupling/
createNonConformalCouples -overwrite iFaceUpstr iFaceDownstream

#foamRun