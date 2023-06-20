## General advice/process
general:
	- run 'caseSetup' from start each time (to remove errors)
meshing:
	- view the geometry/mesh before debugging.
	- common issues: syntax: using combination of geo/occ module: results in successful execution but no mesh elements.
internal surfaces:
	- create using Foam utilities (no entity in boundary file on mesh creation):
		- see /system/topoSetDict & /system/createBafflesDict
	- https://github.com/OpenFOAM/OpenFOAM-10/tree/master/tutorials/incompressible/pimpleFoam/RAS/TJunctionFan
	- https://github.com/OpenFOAM/OpenFOAM-4.x/tree/master/applications/utilities/mesh/manipulation/createBaffles
DES:
	- https://www.youtube.com/watch?v=q_lWmfgkZsU

## caseSetup
ipython: %run ./mesh2dJetWithoutBall.py
gmshToFoam mesh3dJet_withShield_noHeads.msh 
rm -rf ./constant/polyMesh
transformPoints scale="(0.001 0.001 0.001)"
topoSet
createBaffles -overwrite
checkMesh
pisoFoam
ps
kill -9 <PID>