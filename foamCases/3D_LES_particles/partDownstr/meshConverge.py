from meshDownstr import mesh

# badCells from 19.0-17.0
# TODO: 
# - 1. range from 25.0-15.0: Mesh OK: 21.908, 22.159
# - 2. cfmesh: cylindrical boundary

for x in range(0, 6000):

	# mesh with new parameter
	meshSize_i = 21.9
	meshSize = meshSize_i + (0.001) * x
	mesh(meshSize)

	# convert mesh to native format
	!rm -rf ./constant/polyMesh
	converted = !gmshToFoam mesh_cyl_downstream.msh
	transformed = !transformPoints scale="(0.001 0.001 0.001)"

	# check for bad cells:
	checkMesh = !checkMesh
	checkMeshLine = checkMesh[-12]
	if checkMeshLine.startswith(' ***Zero or negative cell volume detected'):
		badCells = checkMeshLine
	meshCheck = checkMesh[-4]
	if meshCheck.startswith('Mesh OK.'):
		print("Mesh OK: " + str(meshSize))
		break
	else:
		print("Mesh bad:" + " meshSize=" + str(meshSize) + ", badCells=" + str(badCells[-2:]))
		continue