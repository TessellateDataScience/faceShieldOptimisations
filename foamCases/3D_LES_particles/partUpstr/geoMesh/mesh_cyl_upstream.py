# File created and owned by Tessellate Data Science (www.tessellate.science). You can 
# re-use this file as long as you abide by own licencing. We're aiming to encourage 
# innovation, so any activity that hinders this goes against our intentions.
#
# This template can be used to specify domain and mesh resolution. The 3D domain is a
# cylinder shape which is meshed using an axisymmetric mesh, incorporating a circular 
# mouth surface.

# Requirements
import gmsh
import os
import numpy as np
import math
gmsh.initialize()
gmsh.clear()


# Definitions
nameModel = 'mesh_cyl_upstream'
gmsh.model.add(nameModel)
geoMod = gmsh.model.geo


# MODIFY: major parameters [mm]
meshSize = 5
meshDensityLong = 50
meshDensityShort = 10


# Cylinder: cross-section
p1 = geoMod.addPoint(0, 0, 0, meshSize)
p2 = geoMod.addPoint(0, 400, 0, meshSize)
p3 = geoMod.addPoint(10, 400, 0, meshSize)
p4 = geoMod.addPoint(300, 400, 0, meshSize)
p5 = geoMod.addPoint(300, 0, 0, meshSize)
p6 = geoMod.addPoint(10, 0, 0, meshSize)
geoMod.synchronize()

# Bug: OF's checkMesh doesn't like translations > 1000
gmsh.model.geo.translate([(0, 1), (0, 2), (0, 3), (0, 4), 
						  (0, 5), (0, 6)], 0, -900, 0)
geoMod.synchronize()

line1 = geoMod.addLine(p1, p2, 101)
line2 = geoMod.addLine(p2, p3, 102)
line3 = geoMod.addLine(p3, p6, 103)
line4 = geoMod.addLine(p6, p1, 104)

line5 = geoMod.addLine(p3, p4, 105)
line6 = geoMod.addLine(p4, p5, 106)
line7 = geoMod.addLine(p5, p6, 107)
line8 = geoMod.addLine(p6, p1, 108)
geoMod.synchronize()


# Mesh: density + structured
geoMod.mesh.setTransfiniteCurve(line3, 81)
geoMod.mesh.setTransfiniteCurve(line2, 6)
geoMod.mesh.setTransfiniteCurve(line7, 59)
geoMod.mesh.setTransfiniteCurve(line4, 6)

blockInner = geoMod.addCurveLoop([line1, line2, line3, line4])
surfInner = geoMod.addPlaneSurface([blockInner], 201)
geoMod.synchronize()
geoMod.mesh.setTransfiniteSurface(surfInner, "Left")
geoMod.mesh.setRecombine(2, surfInner)
geoMod.synchronize()

blockOuter = geoMod.addCurveLoop([line5, line6, line7, -line3])
surfOuter = geoMod.addPlaneSurface([blockOuter], 202)
geoMod.synchronize()
geoMod.mesh.setTransfiniteSurface(surfOuter, "Left")
geoMod.mesh.setRecombine(2, surfOuter)
geoMod.synchronize()


# Cylinder: full
geoMod.revolve([(2, 201), (2, 202)], 0, 0, 0, 0, 1, 0, math.pi / 2, [5], recombine = True)
geoMod.revolve([(2, 219), (2, 241)], 0, 0, 0, 0, 1, 0, math.pi / 2, [5], recombine = True)
geoMod.revolve([(2, 258), (2, 280)], 0, 0, 0, 0, 1, 0, math.pi / 2, [5], recombine = True)
geoMod.revolve([(2, 297), (2, 319)], 0, 0, 0, 0, 1, 0, math.pi / 2, [5], recombine = True)
geoMod.synchronize()


# Specify domain where you want fluid dynamics predicted
entities = gmsh.model.getEntities(3)
entitiesInt = []
for entity in entities:
	entitiesInt.append(entity[1])
gmsh.model.addPhysicalGroup(3, entitiesInt)


# Specify surfaces for 'boundary conditions'
cylEnd1 = [211, 228, 250, 267, 289, 306, 328, 344]
cylEnd2 = [236, 275, 314, 352]
cylEndSmall = [218, 257, 296, 335]
curved = [232, 271, 310, 348]
wall = curved + cylEnd2
gmsh.model.addPhysicalGroup(2, cylEndSmall, name = "mouth")
gmsh.model.addPhysicalGroup(2, wall, name = "wall")
gmsh.model.addPhysicalGroup(2, cylEnd1, name = 'iFaceUpstr')


# Mesh domain then save mesh
gmsh.option.setNumber("Mesh.Algorithm", 6)
gmsh.model.mesh.generate(3)

gmsh.option.setNumber("Mesh.MshFileVersion",2.0)
#gmsh.fltk.run() 
gmsh.write(nameModel + ".msh")
gmsh.finalize()