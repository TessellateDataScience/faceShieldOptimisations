# File created and owned by Tessellate Data Science (www.tessellate.science). You can 
# re-use this file as long as you abide by own licencing. We're aiming to encourage 
# innovation, so any activity that hinders this goes against our intentions.
#
# This file creates a domain of a 3D rectangle while allowing a blunt body 
# (representing a shield) to be easily created in OpenFOAM within this domain. The 
# flow originates from a jet upstream (which is flowing around the shield). 
# 
# This template can be used to specify domain size, and mesh resolution and grading. 
# The 3D domain is meshed using an O-grid surface grid topology that is extruded in 
# the 3rd direction with structured grids. The structured grid can be graded to allow 
# relaxation of the grid away from the shield (blunt body). 
#
# Thanks to Martin Einarsve for openly sharing his code for 'flow around a cylinder' 
# which has been adapted within this file: 
# https://github.com/meinarsve/CFDwOpenFoam/tree/master/LaminarVortexShedding

# requirements
import gmsh
gmsh.initialize()
gmsh.clear()


# MODIFY: major parameters [mm]. You will also need to adjust further mesh 
# parameters below (specifically 'hex-mesh density' & 'streamwise grid grading')
nameModel = "mesh3dJet_withShield_noHeads"
mouthWidth = 50
mouthHeight = 20
shieldLength =200
distanceMouthToShield = 1500
distanceBehindShield = 500
meshSize = 10
meshDepthSize = 50


# definitions
gmsh.model.add(nameModel)
geoMod = gmsh.model.geo


# mouth surface
centre = geoMod.addPoint(0, 0, 0, meshSize)
xPlus = geoMod.addPoint(mouthHeight / 2, 0, 0, meshSize)
yPlus = geoMod.addPoint(0, mouthWidth / 2, 0, meshSize)
xMinus = geoMod.addPoint(-(mouthHeight / 2), 0, 0, meshSize)
yMinus = geoMod.addPoint(0, -(mouthWidth / 2), 0, meshSize)

majorAxis = 2 # y-axis
lineMouth1 = geoMod.addEllipseArc(xPlus, centre, majorAxis, yPlus)
lineMouth2 = geoMod.addEllipseArc(yPlus, centre, majorAxis, xMinus)
lineMouth3 = geoMod.addEllipseArc(xMinus, centre, majorAxis, yMinus)
lineMouth4 = geoMod.addEllipseArc(yMinus, centre, majorAxis, xPlus)

mouthCurve = geoMod.addCurveLoop([lineMouth1, lineMouth2, lineMouth3, lineMouth4])
mouthSurf = geoMod.addPlaneSurface([mouthCurve])
geoMod.synchronize()


# cylinder surface around mouth
p1 = geoMod.addPoint(30, 30, 0, meshSize)
p2 = geoMod.addPoint(-30, 30, 0, meshSize)
p3 = geoMod.addPoint(-30, -30, 0, meshSize)
p4 = geoMod.addPoint(30, -30, 0, meshSize)

lineCyl1 = geoMod.addCircleArc(p1, centre, p2)
lineCyl2 = geoMod.addCircleArc(p2, centre, p3)
lineCyl3 = geoMod.addCircleArc(p3, centre, p4)
lineCyl4 = geoMod.addCircleArc(p4, centre, p1)

cylCurve = geoMod.addCurveLoop([lineCyl1, lineCyl2, lineCyl3, lineCyl4])
cylSurf = geoMod.addPlaneSurface([cylCurve, mouthCurve])
geoMod.synchronize()


# set of block surfaces around cylinder
rectP1 = geoMod.addPoint(shieldLength / 2, shieldLength / 2, 0, meshSize)
rectP2 = geoMod.addPoint(-(shieldLength / 2), shieldLength / 2, 0, meshSize)
rectP3 = geoMod.addPoint(-(shieldLength / 2), -(shieldLength / 2), 0, meshSize)
rectP4 = geoMod.addPoint(shieldLength / 2, -(shieldLength / 2), 0, meshSize)

lineRect1 = geoMod.addLine(rectP1, rectP2)
lineRect2 = geoMod.addLine(rectP2, rectP3)
lineRect3 = geoMod.addLine(rectP3, rectP4)
lineRect4 = geoMod.addLine(rectP4, rectP1)

lineBlock1 = geoMod.addLine(p1, rectP1)
lineBlock2 = geoMod.addLine(p2, rectP2)
lineBlock3 = geoMod.addLine(p3, rectP3)
lineBlock4 = geoMod.addLine(p4, rectP4)

block1Curve = geoMod.addCurveLoop([lineBlock1, lineRect1, -lineBlock2, -lineCyl1])
block2Curve = geoMod.addCurveLoop([lineBlock2, lineRect2, -lineBlock3, -lineCyl2])
block3Curve = geoMod.addCurveLoop([lineBlock3, lineRect3, -lineBlock4, -lineCyl3])
block4Curve = geoMod.addCurveLoop([lineBlock4, lineRect4, -lineBlock1, -lineCyl4])

block1Surf = geoMod.addPlaneSurface([block1Curve])
block2Surf = geoMod.addPlaneSurface([block2Curve])
block3Surf = geoMod.addPlaneSurface([block3Curve])
block4Surf = geoMod.addPlaneSurface([block4Curve])
geoMod.synchronize()


# Another block surfaces set (around previous block set)
rectLP1 = geoMod.addPoint(300, 300, 0, meshSize)
rectLP2 = geoMod.addPoint(-300, 300, 0, meshSize)
rectLP3 = geoMod.addPoint(-300, -300, 0, meshSize)
rectLP4 = geoMod.addPoint(300, -300, 0, meshSize)

lineRectL1 = geoMod.addLine(rectLP1, rectLP2)
lineRectL2 = geoMod.addLine(rectLP2, rectLP3)
lineRectL3 = geoMod.addLine(rectLP3, rectLP4)
lineRectL4 = geoMod.addLine(rectLP4, rectLP1)

lineBlockL1 = geoMod.addLine(rectP1, rectLP1)
lineBlockL2 = geoMod.addLine(rectP2, rectLP2)
lineBlockL3 = geoMod.addLine(rectP3, rectLP3)
lineBlockL4 = geoMod.addLine(rectP4, rectLP4)

blockL1Curve = geoMod.addCurveLoop([lineBlockL1, lineRectL1, -lineBlockL2, -lineRect1])
blockL2Curve = geoMod.addCurveLoop([lineBlockL2, lineRectL2, -lineBlockL3, -lineRect2])
blockL3Curve = geoMod.addCurveLoop([lineBlockL3, lineRectL3, -lineBlockL4, -lineRect3])
blockL4Curve = geoMod.addCurveLoop([lineBlockL4, lineRectL4, -lineBlockL1, -lineRect4])

blockL1Surf = geoMod.addPlaneSurface([blockL1Curve])
blockL2Surf = geoMod.addPlaneSurface([blockL2Curve])
blockL3Surf = geoMod.addPlaneSurface([blockL3Curve])
blockL4Surf = geoMod.addPlaneSurface([blockL4Curve])
geoMod.synchronize()


# MODIFY: hex-mesh density
geoMod.mesh.setTransfiniteCurve(lineMouth1, 10)
geoMod.mesh.setTransfiniteCurve(lineMouth2, 9)
geoMod.mesh.setTransfiniteCurve(lineMouth3, 9)
geoMod.mesh.setTransfiniteCurve(lineMouth4, 8)

geoMod.mesh.setTransfiniteCurve(lineCyl1, 20)
geoMod.mesh.setTransfiniteCurve(lineCyl2, 19)
geoMod.mesh.setTransfiniteCurve(lineCyl3, 19)
geoMod.mesh.setTransfiniteCurve(lineCyl4, 18)

geoMod.mesh.setTransfiniteCurve(lineRect1, 20)
geoMod.mesh.setTransfiniteCurve(lineRect2, 19)
geoMod.mesh.setTransfiniteCurve(lineRect3, 19)
geoMod.mesh.setTransfiniteCurve(lineRect4, 18)

geoMod.mesh.setTransfiniteCurve(lineRectL1, 20)
geoMod.mesh.setTransfiniteCurve(lineRectL2, 19)
geoMod.mesh.setTransfiniteCurve(lineRectL3, 19)
geoMod.mesh.setTransfiniteCurve(lineRectL4, 18)

geoMod.mesh.setTransfiniteCurve(lineBlock1, 20)
geoMod.mesh.setTransfiniteCurve(lineBlock2, 20)
geoMod.mesh.setTransfiniteCurve(lineBlock3, 20)
geoMod.mesh.setTransfiniteCurve(lineBlock4, 20)

geoMod.mesh.setTransfiniteCurve(lineBlockL1, 20)
geoMod.mesh.setTransfiniteCurve(lineBlockL2, 20)
geoMod.mesh.setTransfiniteCurve(lineBlockL3, 20)
geoMod.mesh.setTransfiniteCurve(lineBlockL4, 20)


# define hex-mesh locations
geoMod.mesh.setTransfiniteSurface(block1Surf, "Left")
geoMod.mesh.setTransfiniteSurface(block2Surf, "Left")
geoMod.mesh.setTransfiniteSurface(block3Surf, "Left")
geoMod.mesh.setTransfiniteSurface(block4Surf, "Left")

geoMod.mesh.setRecombine(2, block1Surf)
geoMod.mesh.setRecombine(2, block2Surf)
geoMod.mesh.setRecombine(2, block3Surf)
geoMod.mesh.setRecombine(2, block4Surf)

geoMod.mesh.setTransfiniteSurface(blockL1Surf)
geoMod.mesh.setTransfiniteSurface(blockL2Surf)
geoMod.mesh.setTransfiniteSurface(blockL3Surf)
geoMod.mesh.setTransfiniteSurface(blockL4Surf)

geoMod.mesh.setRecombine(2, blockL1Surf)
geoMod.mesh.setRecombine(2, blockL2Surf)
geoMod.mesh.setRecombine(2, blockL3Surf)
geoMod.mesh.setRecombine(2, blockL4Surf)
geoMod.synchronize()


# MODIFY: streamwise grid grading
N = 61 					# number elements
r = 0.97291 			# ratio
d = [meshDepthSize] 	# first element thickness
for i in range(1, N): 
	d.append(d[-1] + (d[0]) * r**i)
d.reverse()
D = []
for d_i in d:
	D.append(d_i - 1500)
heights = []
for D_i in D:
	heights.append(D_i * -1)
heights.pop(0)
heights.append(1500)
h_norm = []
for h_i in heights:
	h_norm.append(h_i / 1500)

N2 = 32
r = 1.0272
d2 = [10]
for i in range(1, N2):
	d2.append(d2[-1] + (d2[0]) * r**i)
d2.pop()
d2.append(500)
hShield_norm = []
for d2_i in d2:
	hShield_norm.append((d2_i / 500) * +1)

# 3D grid creation
gmsh.model.mesh.generate(2)
extrusionParams = [(2, mouthSurf), (2, cylSurf), (2, block1Surf), (2, block2Surf), 
				   (2, block3Surf), (2, block4Surf), (2, blockL1Surf), 
				   (2, blockL2Surf), (2, blockL3Surf), (2, blockL4Surf)]
ext1 = geoMod.extrude(extrusionParams, 
					  0, 0, 1500,
 					  numElements = [1] * N, 
 					  heights = h_norm, 
 					  recombine = True)
ext2 = geoMod.extrude(extrusionParams, 
					  0, 0, -distanceBehindShield, 
					  numElements = [1] * N2,
					  heights = hShield_norm, 
					  recombine = True)
geoMod.synchronize()


# specify the domain (required for OpenFOAM): https://www.cfd-online.com/Forums/
# openfoam-meshing/185021-perhaps-you-have-not-exported-3d-elements.html
entitiesL = len(gmsh.model.getEntities(3))
entities = []
for i in range(1, entitiesL + 1):
	entities.append(i)
gmsh.model.addPhysicalGroup(3, entities)


# group surfaces into regions where same flow conditions can be applied (ie. assign 
# same boundary conditions to surfaces within this group)
gmsh.model.addPhysicalGroup(2, [46], name = "mouth") # found via GUI

# get outer surfaces (to assign a boundary condition to this group)
surfaceOuter1 = gmsh.model.getEntitiesInBoundingBox(-300, -300, distanceMouthToShield - 1, 
	300, 300, distanceMouthToShield + 1, 2)
surfaceOuter2 = gmsh.model.getEntitiesInBoundingBox(-300, -300, -distanceBehindShield, 
	300, 300, -distanceBehindShield, 2)
surfaceOuter3 = gmsh.model.getEntitiesInBoundingBox(-300, -300, -distanceBehindShield, 
	300, -300, distanceMouthToShield, 2)
surfaceOuter4 = gmsh.model.getEntitiesInBoundingBox(-300, 300, -distanceBehindShield, 
	300, 300, distanceMouthToShield, 2)
surfaceOuter5 = gmsh.model.getEntitiesInBoundingBox(-300, -300, -distanceBehindShield, 
	-300, 300, distanceMouthToShield, 2)
surfaceOuter6 = gmsh.model.getEntitiesInBoundingBox(300, -300, -distanceBehindShield, 
	300, 300, distanceMouthToShield, 2)
surfaceOuter1.pop(0)
surfaces = []
for i in surfaceOuter1:
	surfaces.append(i[1])
for i in surfaceOuter2:
	surfaces.append(i[1])
for i in surfaceOuter3:
	surfaces.append(i[1])
for i in surfaceOuter4:
	surfaces.append(i[1])
for i in surfaceOuter5:
	surfaces.append(i[1])
for i in surfaceOuter6:
	surfaces.append(i[1])
gmsh.model.addPhysicalGroup(2, surfaces, name = "atmos")


# mesh then save mesh
gmsh.model.mesh.generate(3)
gmsh.option.setNumber("Mesh.MshFileVersion",2.0) 
gmsh.write(nameModel + ".msh")


# view in graphical user-interface (GUI)
#gmsh.fltk.run()
gmsh.finalize()