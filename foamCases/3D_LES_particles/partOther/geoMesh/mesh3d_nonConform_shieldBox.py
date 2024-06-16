# File created and owned by Tessellate Data Science (www.tessellate.science). You can 
# re-use this file as long as you abide by own licencing. We're aiming to encourage 
# innovation, so any activity that hinders this goes against our intentions.
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
nameModel = 'mesh3d_nonConform_shieldBox'
gmsh.model.add(nameModel)
geoMod = gmsh.model.geo


# MODIFY: major parameters [mm]
meshSizeMouth 			= 5.0   	# tets' size within mouth
meshSize                = 17.5 		# tets' size surrounding shield
meshCircleEdge 			= 17 		# mesh density (number) on circle region's circumference
meshMouthPerp 			= 9 		# mesh density perpendicular to mouth's circumference
meshOuterPerp 			= 12 		# mesh density (perpendicular) of outer blocks 

shieldWidth             = 300   	# *linear* distance from shield's ends (near ears)
shieldHeight            = 140
mouthToShield           = 1000
mouthZ                  = 75


# Mouth lines
Y = 300
centre = geoMod.addPoint(0, Y, 0, meshSizeMouth)
xPlus = geoMod.addPoint(20, Y, 0, meshSizeMouth)
zPlus = geoMod.addPoint(0, Y, 10, meshSizeMouth)
xMinus = geoMod.addPoint(-20, Y, 0, meshSizeMouth)
zMinus = geoMod.addPoint(0, Y, -10, meshSizeMouth)
geoMod.synchronize()

majorAxis = 2 # y-axis
lineMouth1 = geoMod.addEllipseArc(xPlus, centre, majorAxis, zPlus, 101)
lineMouth2 = geoMod.addEllipseArc(zPlus, centre, majorAxis, xMinus, 102)
lineMouth3 = geoMod.addEllipseArc(xMinus, centre, majorAxis, zMinus, 103)
lineMouth4 = geoMod.addEllipseArc(zMinus, centre, majorAxis, xPlus, 104)
geoMod.synchronize()


# Circle around mouth lines
circleP1 = geoMod.addPoint(80, Y, 80, meshSize)
circleP2 = geoMod.addPoint(-80, Y, 80, meshSize)
circleP3 = geoMod.addPoint(-80, Y, -80, meshSize)
circleP4 = geoMod.addPoint(80, Y, -80, meshSize)
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
rectSize = 200 # Y
rectP1 = geoMod.addPoint(rectSize, Y, rectSize)
rectP2 = geoMod.addPoint(-rectSize, Y, rectSize)
rectP3 = geoMod.addPoint(-rectSize, Y, -rectSize)
rectP4 = geoMod.addPoint(rectSize, Y, -rectSize)

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

expansion = 1.1
geoMod.mesh.setTransfiniteCurve(lineBlock1, meshMouthPerp, "Progression", expansion)
geoMod.mesh.setTransfiniteCurve(lineBlock2, meshMouthPerp, "Progression", expansion)
geoMod.mesh.setTransfiniteCurve(lineBlock3, meshMouthPerp, "Progression", expansion)
geoMod.mesh.setTransfiniteCurve(lineBlock4, meshMouthPerp, "Progression", expansion)

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
rectOutP1 = geoMod.addPoint(rectSize, Y, rectSize)
rectOutP2 = geoMod.addPoint(-rectSize, Y, rectSize)
rectOutP3 = geoMod.addPoint(-rectSize, Y, -rectSize)
rectOutP4 = geoMod.addPoint(rectSize, Y, -rectSize)

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

expansion2 = 1.1
geoMod.mesh.setTransfiniteCurve(lineBlockOut1, meshOuterPerp, "Progression", expansion2)
geoMod.mesh.setTransfiniteCurve(lineBlockOut2, meshOuterPerp, "Progression", expansion2)
geoMod.mesh.setTransfiniteCurve(lineBlockOut3, meshOuterPerp, "Progression", expansion2)
geoMod.mesh.setTransfiniteCurve(lineBlockOut4, meshOuterPerp, "Progression", expansion2)

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
N = int(mouthToShield / meshSize)

## mesh density: behind shield (approximately)
N2 = int(700 / meshSize)

ext1 = geoMod.extrude(surfsExtAll, 
					  0, mouthToShield, 0,
 					  numElements = [1] * N, 
					  #heights = h_norm,
 					  recombine = True)
ext2 = geoMod.extrude(surfsExtOut, 
					  0, -700, 0,
 					  numElements = [1] * N2, 
 					  recombine = True)
geoMod.synchronize()


# Specify domain where you want fluid dynamics predicted
entities = gmsh.model.getEntities(3)
entitiesInt = []
for entity in entities:
	entitiesInt.append(entity[1])
gmsh.model.addPhysicalGroup(3, entitiesInt)


# Specify surfaces for 'boundary conditions'
gmsh.model.addPhysicalGroup(2, [101, 301, 355, 356, 357, 358, 
								707, 729, 751, 773], name = 'interface')
gmsh.model.addPhysicalGroup(2, [480], name = "mouth")
gmsh.model.addPhysicalGroup(2, [522, 544, 566, 588, 610, 632, 654, 676, 698], 
 								name = "wall")
gmsh.model.addPhysicalGroup(2, [627, 649, 671, 693, 715, 737, 759, 781,
 								786, 764, 742, 720, 819], name = "atmos")


# Mesh domain then save mesh
gmsh.option.setNumber("Mesh.Algorithm", 6)
gmsh.model.mesh.generate(3)

gmsh.option.setNumber("Mesh.MshFileVersion",2.0) 
gmsh.write(nameModel + ".msh")
gmsh.finalize()