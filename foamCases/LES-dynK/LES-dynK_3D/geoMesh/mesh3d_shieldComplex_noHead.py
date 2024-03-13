# File created and owned by Tessellate Data Science (www.tessellate.science). You can 
# re-use this file as long as you abide by own licencing. We're aiming to encourage 
# innovation, so any activity that hinders this goes against our intentions.
#
# This file creates a domain of a 3D rectangle including a blunt body (representing
# a shield). The flow originates from a jet (mouth) upstream, which is flowing
# around the shield. 
# 
# This template can be used to specify domain size and mesh resolution. The 3D domain 
# is meshed using an O-grid surface grid topology that is extruded in the 3rd direction 
# with a structured grid.
#
# Thanks to Martin Einarsve for openly sharing his code for 'flow around a cylinder', 
# which has been adapted within this file: 
# https://github.com/meinarsve/CFDwOpenFoam/tree/master/LaminarVortexShedding

# Requirements
import gmsh
import os
import numpy as np
gmsh.initialize()
gmsh.clear()


# Definitions
nameModel = 'mesh3d_shieldComplex_noHead'
gmsh.model.add(nameModel)
geoMod = gmsh.model.geo


# MODIFY: major parameters [mm]
meshSizeMouth 			= 10.0   	# tets' size within mouth
meshSize                = 17.500001 # tets' size surrounding shield
meshCircleEdge 			= 17 		# mesh density (number) on circle region's circumference
meshMouthPerp 			= 16 		# mesh density perpendicular to mouth's circumference
meshOuterPerp 			= 28 		# mesh density (perpendicular) of outer blocks 

shieldWidth             = 300   	# *linear* distance from shield's ends (near ears)
shieldHeight            = 140
mouthToShield           = 1500
mouthZ                  = 75


# Mouth lines
Y = 295
centre = geoMod.addPoint(0, Y, mouthZ, meshSizeMouth)
xPlus = geoMod.addPoint(40, Y, mouthZ, meshSizeMouth)
zPlus = geoMod.addPoint(0, Y, mouthZ + 20, meshSizeMouth)
xMinus = geoMod.addPoint(-40, Y, mouthZ, meshSizeMouth)
zMinus = geoMod.addPoint(0, Y, mouthZ - 20, meshSizeMouth)
geoMod.synchronize()

majorAxis = 2 # y-axis
lineMouth1 = geoMod.addEllipseArc(xPlus, centre, majorAxis, zPlus, 101)
lineMouth2 = geoMod.addEllipseArc(zPlus, centre, majorAxis, xMinus, 102)
lineMouth3 = geoMod.addEllipseArc(xMinus, centre, majorAxis, zMinus, 103)
lineMouth4 = geoMod.addEllipseArc(zMinus, centre, majorAxis, xPlus, 104)
geoMod.synchronize()


# Circle around mouth lines
circleP1 = geoMod.addPoint(100, Y, mouthZ + 100, meshSize)
circleP2 = geoMod.addPoint(-100, Y, mouthZ + 100, meshSize)
circleP3 = geoMod.addPoint(-100, Y, mouthZ - 100, meshSize)
circleP4 = geoMod.addPoint(100, Y, mouthZ - 100, meshSize)
geoMod.synchronize()

lineCircle1 = geoMod.addCircleArc(circleP1, centre, circleP2, 301)
lineCircle2 = geoMod.addCircleArc(circleP2, centre, circleP3, 302)
lineCircle3 = geoMod.addCircleArc(circleP3, centre, circleP4, 303)
lineCircle4 = geoMod.addCircleArc(circleP4, centre, circleP1, 304)

mouthCurve = geoMod.addCurveLoop([lineMouth1, lineMouth2, 
                                  lineMouth3, lineMouth4], 101)
mouthSurf = geoMod.addPlaneSurface([mouthCurve], 101)

circleCurve = geoMod.addCurveLoop([lineCircle1, lineCircle2, 
                                   lineCircle3, lineCircle4], 301)
circleSurf = geoMod.addPlaneSurface([circleCurve, mouthCurve], 301)
geoMod.synchronize()
gmsh.model.mesh.generate(2)


# Rectangle around circle
## lines
rectSize = Y
rectP1 = geoMod.addPoint(rectSize, Y, rectSize + mouthZ)
rectP2 = geoMod.addPoint(-rectSize, Y, rectSize + mouthZ)
rectP3 = geoMod.addPoint(-rectSize, Y, -rectSize + mouthZ)
rectP4 = geoMod.addPoint(rectSize, Y, -rectSize + mouthZ)

lineRect1 = geoMod.addLine(rectP1, rectP2, 201)
lineRect2 = geoMod.addLine(rectP2, rectP3, 202)
lineRect3 = geoMod.addLine(rectP3, rectP4, 203)
lineRect4 = geoMod.addLine(rectP4, rectP1, 204)
geoMod.synchronize()

## multi-block lines
lineBlock1 = geoMod.addLine(circleP1, rectP1)
lineBlock2 = geoMod.addLine(circleP2, rectP2)
lineBlock3 = geoMod.addLine(circleP3, rectP3)
lineBlock4 = geoMod.addLine(circleP4, rectP4)
geoMod.synchronize()

## Multi-block surfaces
blockCurve1 = geoMod.addCurveLoop([-lineCircle1, lineBlock1, lineRect1, -lineBlock2])
blockCurve2 = geoMod.addCurveLoop([-lineCircle2, lineBlock2, lineRect2, -lineBlock3])
blockCurve3 = geoMod.addCurveLoop([-lineCircle3, lineBlock3, lineRect3, -lineBlock4])
blockCurve4 = geoMod.addCurveLoop([-lineCircle4, lineBlock4, lineRect4, -lineBlock1])

blockSurf1 = geoMod.addPlaneSurface([blockCurve1], 355)
blockSurf2 = geoMod.addPlaneSurface([blockCurve2], 356)
blockSurf3 = geoMod.addPlaneSurface([blockCurve3], 357)
blockSurf4 = geoMod.addPlaneSurface([blockCurve4], 358)
geoMod.synchronize()

## Hex-mesh density
geoMod.mesh.setTransfiniteCurve(lineCircle1, meshCircleEdge)
geoMod.mesh.setTransfiniteCurve(lineCircle2, meshCircleEdge - 1)
geoMod.mesh.setTransfiniteCurve(lineCircle3, meshCircleEdge - 1)
geoMod.mesh.setTransfiniteCurve(lineCircle4, meshCircleEdge - 2)

geoMod.mesh.setTransfiniteCurve(lineRect1, meshCircleEdge)
geoMod.mesh.setTransfiniteCurve(lineRect2, meshCircleEdge - 1)
geoMod.mesh.setTransfiniteCurve(lineRect3, meshCircleEdge - 1)
geoMod.mesh.setTransfiniteCurve(lineRect4, meshCircleEdge - 2)

geoMod.mesh.setTransfiniteCurve(lineBlock1, meshMouthPerp)
geoMod.mesh.setTransfiniteCurve(lineBlock2, meshMouthPerp)
geoMod.mesh.setTransfiniteCurve(lineBlock3, meshMouthPerp)
geoMod.mesh.setTransfiniteCurve(lineBlock4, meshMouthPerp)

geoMod.mesh.setTransfiniteSurface(blockSurf1, "Left")
geoMod.mesh.setTransfiniteSurface(blockSurf2, "Left")
geoMod.mesh.setTransfiniteSurface(blockSurf3, "Left")
geoMod.mesh.setTransfiniteSurface(blockSurf4, "Left")

geoMod.mesh.setRecombine(2, blockSurf1)
geoMod.mesh.setRecombine(2, blockSurf2)
geoMod.mesh.setRecombine(2, blockSurf3)
geoMod.mesh.setRecombine(2, blockSurf4)
geoMod.synchronize()


# Larger rectangle around rectangle
## Lines
rectSize = 600
rectOutP1 = geoMod.addPoint(rectSize, Y, rectSize + mouthZ)
rectOutP2 = geoMod.addPoint(-rectSize, Y, rectSize + mouthZ)
rectOutP3 = geoMod.addPoint(-rectSize, Y, -rectSize + mouthZ)
rectOutP4 = geoMod.addPoint(rectSize, Y, -rectSize + mouthZ)

lineRectOut1 = geoMod.addLine(rectOutP1, rectOutP2, 211)
lineRectOut2 = geoMod.addLine(rectOutP2, rectOutP3, 212)
lineRectOut3 = geoMod.addLine(rectOutP3, rectOutP4, 213)
lineRectOut4 = geoMod.addLine(rectOutP4, rectOutP1, 214)
geoMod.synchronize()

## Multi-block lines
lineBlockOut1 = geoMod.addLine(rectP1, rectOutP1)
lineBlockOut2 = geoMod.addLine(rectP2, rectOutP2)
lineBlockOut3 = geoMod.addLine(rectP3, rectOutP3)
lineBlockOut4 = geoMod.addLine(rectP4, rectOutP4)
geoMod.synchronize()

## Multi-block surfaces
blockOutCurve1 = geoMod.addCurveLoop([-lineRect1, lineBlockOut1, lineRectOut1, -lineBlockOut2])
blockOutCurve2 = geoMod.addCurveLoop([-lineRect2, lineBlockOut2, lineRectOut2, -lineBlockOut3])
blockOutCurve3 = geoMod.addCurveLoop([-lineRect3, lineBlockOut3, lineRectOut3, -lineBlockOut4])
blockOutCurve4 = geoMod.addCurveLoop([-lineRect4, lineBlockOut4, lineRectOut4, -lineBlockOut1])

blockOutSurf1 = geoMod.addPlaneSurface([blockOutCurve1], 455)
blockOutSurf2 = geoMod.addPlaneSurface([blockOutCurve2], 456)
blockOutSurf3 = geoMod.addPlaneSurface([blockOutCurve3], 457)
blockOutSurf4 = geoMod.addPlaneSurface([blockOutCurve4], 458)
geoMod.synchronize()

## Hex-mesh density then mesh surface
geoMod.mesh.setTransfiniteCurve(lineRectOut1, meshCircleEdge)
geoMod.mesh.setTransfiniteCurve(lineRectOut2, meshCircleEdge - 1)
geoMod.mesh.setTransfiniteCurve(lineRectOut3, meshCircleEdge - 1)
geoMod.mesh.setTransfiniteCurve(lineRectOut4, meshCircleEdge - 2)

geoMod.mesh.setTransfiniteCurve(lineBlockOut1, meshOuterPerp)
geoMod.mesh.setTransfiniteCurve(lineBlockOut2, meshOuterPerp)
geoMod.mesh.setTransfiniteCurve(lineBlockOut3, meshOuterPerp)
geoMod.mesh.setTransfiniteCurve(lineBlockOut4, meshOuterPerp)

geoMod.mesh.setTransfiniteSurface(blockOutSurf1, "Left")
geoMod.mesh.setTransfiniteSurface(blockOutSurf2, "Left")
geoMod.mesh.setTransfiniteSurface(blockOutSurf3, "Left")
geoMod.mesh.setTransfiniteSurface(blockOutSurf4, "Left")

geoMod.mesh.setRecombine(2, blockOutSurf1)
geoMod.mesh.setRecombine(2, blockOutSurf2)
geoMod.mesh.setRecombine(2, blockOutSurf3)
geoMod.mesh.setRecombine(2, blockOutSurf4)
geoMod.synchronize()


# Define mesh of most regions (besides region surrounding shield)
surfsExtAll = gmsh.model.getEntities(2)
surfsExtOut = surfsExtAll[-4:]

## mesh density: mouth to shield (approximately)
N = int(1500 / meshSize)

## mesh density: behind shield (approximately)
N2 = int(700 / meshSize)

ext1 = geoMod.extrude(surfsExtAll, 
					  0, 1500, 0,
 					  numElements = [1] * N, 
					  #heights = h_norm,
 					  recombine = True)
ext2 = geoMod.extrude(surfsExtOut, 
					  0, -700, 0,
 					  numElements = [1] * N2, 
 					  recombine = True)
geoMod.synchronize()


# Shield
r = shieldWidth / 2
meshSizeRef = meshSize / 1
C1 = geoMod.addPoint(0, 0, 0, meshSizeRef, 151)
P1 = geoMod.addPoint(r, 0, 0, meshSizeRef, 152)
P2 = geoMod.addPoint(0, r, 0, meshSizeRef, 153)
P3 = geoMod.addPoint(-r, 0, 0, meshSizeRef, 154)
P4 = geoMod.addPoint(-r + meshSizeRef, 0, 0, meshSizeRef, 155)
P5 = geoMod.addPoint(0, r - meshSizeRef, 0, meshSizeRef, 156)
P6 = geoMod.addPoint(r - meshSizeRef, 0, 0, meshSizeRef, 157)
geoMod.synchronize()

lineShield1 = geoMod.addCircleArc(P1, C1, P2, 151)
lineShield2 = geoMod.addCircleArc(P2, C1, P3, 152)
lineShield3 = geoMod.addLine(P3, P4, 153)
lineShield4 = geoMod.addCircleArc(P4, C1, P5, 154)
lineShield5 = geoMod.addCircleArc(P5, C1, P6, 155)
lineShield6 = geoMod.addLine(P6, P1, 156)
geoMod.synchronize()

shieldCurve = geoMod.addCurveLoop([lineShield1, lineShield2, lineShield3, 
                                  lineShield4, lineShield5, lineShield6], 151)
shieldSurf = geoMod.addPlaneSurface([shieldCurve], 151)
surfsShield = geoMod.extrude([(2, shieldSurf)], 0, 0, shieldHeight)
surfsShield.append((2, shieldSurf))
surfsShield.pop(1)
geoMod.synchronize()


# Renumber points to allow importing of head geometry without error 
ptsAll = gmsh.model.getEntities(0)
i = 1
for ptBox in ptsAll:
    ptBoxInt = ptBox[1]
    gmsh.model.setTag(0, ptBoxInt, 200 + i)
    i = i + 1


# Import pre-made head geometry (then renumber entities to remove meshing error)
gmsh.merge('./geoMesh/geom3d_headPolygon.step')
surfsAll = gmsh.model.getEntities(2)
j = 1
for surfBox in surfsAll[:16]:
	surfBoxInt = surfBox[1]
	gmsh.model.setTag(2, surfBoxInt, 1000 + j)
	j = j + 1

linesAll = gmsh.model.getEntities(1)
k = 1
for lineBox in linesAll[:41]:
	lineBoxInt = lineBox[1]
	gmsh.model.setTag(1, lineBoxInt, 1000 + k)
	k = k + 1

ptsAll = gmsh.model.getEntities(0)
l = 1
for ptBox in ptsAll[:30]:
	ptBoxInt = ptBox[1]
	gmsh.model.setTag(0, ptBoxInt, 1000 + l)
	l = l + 1


# Make remaining region surrounding shield (ignoring head geometry)
linesBoxBack = [700, 722, 744, 766]
loopBack = geoMod.addCurveLoop(linesBoxBack, reorient = True)
surfBack = geoMod.addPlaneSurface([loopBack])
surfsBox = [mouthSurf, circleSurf, blockSurf1, blockSurf2, blockSurf3, blockSurf4, 
			773, 751, 729, 707, surfBack]
surfLoopBox = geoMod.addSurfaceLoop(surfsBox)
geoMod.synchronize()

surfsShieldInt = []
for surf in surfsShield:
	surfsShieldInt.append(surf[1])
surfLoopShield = geoMod.addSurfaceLoop(surfsShieldInt)

surfsHead = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 
			1008, 1009, 1010, 1011, 1012, 1013, 1014]
surfsNostrils = [1015, 1016]
surfsHeadAll = surfsHead + surfsNostrils
surfLoopHead = geoMod.addSurfaceLoop(surfsHeadAll)

box = geoMod.addVolume([surfLoopBox, surfLoopShield]) 
geoMod.synchronize()


# Specify domain where you want fluid dynamics predicted
gmsh.model.removeEntities([(3, 15)]) # shield
entities = gmsh.model.getEntities(3)
entitiesInt = []
for entity in entities:
	entitiesInt.append(entity[1])
gmsh.model.addPhysicalGroup(3, entitiesInt)
#geoMod.synchronize()


# Specify surfaces for 'boundary conditions'
gmsh.model.addPhysicalGroup(2, [480], name = "mouth")
gmsh.model.addPhysicalGroup(2, [522, 544, 566, 588, 610, 632, 654, 676, 698], 
							name = "wall")
gmsh.model.addPhysicalGroup(2, surfsShieldInt, name = "shield")
#gmsh.model.addPhysicalGroup(2, surfsHead, name = "head")
#gmsh.model.addPhysicalGroup(2, surfsNostrils, name = "nostrils")
gmsh.model.addPhysicalGroup(2, [627, 649, 671, 693, 715, 737, 759, 781,
								786, 764, 742, 720, 819], name = "atmos")


# Mesh domain then optimise tets' mesh
gmsh.option.setNumber("Mesh.Algorithm", 6)    		# 2D mesh: 6: Frontal-Delaunay
gmsh.model.mesh.generate(3)
gmsh.model.mesh.optimize(method = "Relocate3D", force = True, niter = 1)


# Save mesh
#gmsh.fltk.run()
gmsh.option.setNumber("Mesh.MshFileVersion",2.0) 
gmsh.write(nameModel + ".msh")
gmsh.finalize()