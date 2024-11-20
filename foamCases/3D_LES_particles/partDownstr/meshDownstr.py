# File created and owned by Tessellate Data Science (www.tessellate.science). You can 
# re-use this file as long as you abide by own licencing. We're aiming to encourage 
# innovation, so any activity that hinders this goes against our intentions.
# 
# This template can be used to specify domain and mesh resolution. The 3D domain is a
# cylinder shape with a cube volume removed from inside this domain, meshed using
# unstructured (tetrahedral) elements.


def mesh(meshSize):

	# Requirements
	import gmsh
	import os
	import numpy as np
	import math
	gmsh.initialize()
	#gmsh.clear()
	#gmsh.option.setNumber("General.Terminal", 0);


	# MODIFY: major parameters [mm]
	#meshSize = 18.0
	speechLength = 1000
	cubeLength = 400
	yCubeLength = 700
	r = 300


	# Definitions
	nameModel = 'mesh_cyl_downstream'
	gmsh.model.add(nameModel)
	occMod = gmsh.model.occ


	# Cylinder - cube
	occMod.addCylinder(0, -500, 0, 0, 1000, 0, r)
	occMod.addBox(-cubeLength / 2, -400, -cubeLength / 2, 
				  cubeLength, yCubeLength, cubeLength)
	occMod.synchronize()

	occMod.cut([(3, 1)], [(3, 2)])
	occMod.synchronize()


	# Specify domain where you want fluid dynamics predicted
	entities = gmsh.model.getEntities(3)
	entitiesInt = []
	for entity in entities:
		entitiesInt.append(entity[1])
	gmsh.model.addPhysicalGroup(3, entitiesInt)


	# Specify surfaces for boundary-conditions & non-conformal interfaces
	gmsh.model.addPhysicalGroup(2, [1], name = "atmos")
	gmsh.model.addPhysicalGroup(2, [2], name = "atmosEnd")
	gmsh.model.addPhysicalGroup(2, [3], name = 'iFaceDownstream')
	gmsh.model.addPhysicalGroup(2, [4, 5, 6, 7, 8, 9], name = 'iFaceDownCube')


	# Mesh domain then save mesh
	# 1: Delaunay, 3: Initial mesh only, 4: Frontal, 7: MMG3D, 9: R-tree, 10: HXT
	gmsh.option.setNumber("Mesh.Algorithm3D", 10)
	#gmsh.option.setNumber("Mesh.AnisoMax", 2)
	#gmsh.option.setNumber("Mesh.Optimize", 1)
	gmsh.model.mesh.setSize(gmsh.model.getEntities(0), meshSize)
	gmsh.model.mesh.generate(3)

	gmsh.option.setNumber("Mesh.MshFileVersion", 2.0)
	#gmsh.fltk.run() 
	gmsh.write(nameModel + ".msh")
	gmsh.finalize()