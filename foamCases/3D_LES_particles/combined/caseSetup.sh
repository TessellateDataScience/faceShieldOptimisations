#! /bin/bash

# Activate OpenFOAM v2312: 'openfoam2312'

# Combine meshes to make full domain
rm -r ./partOther/1e-06/
mergeMeshes ./partOther ./partShield

# Deactivate OpenFOAM v2312: 'exit'

rm -r ./combined/constant/polyMesh
cp -r ./partOther/1e-06/polyMesh/ ./combined/constant/
cd ./combined

# Deactivate OpenFOAM v2312: 'exit'

# https://cfd.direct/openfoam/free-software/using-non-conformal-coupling/
createNonConformalCouples -overwrite interface interfaceShield

foamRun