# File created and owned by Tessellate Data Science (www.tessellate.science). 
# You can re-use this file as long as you abide by our licencing. We're aiming 
# to encourage innovation, so any activity that hinders this goes against our 
# intentions: https://github.com/TessellateDataScience/faceShieldOptimisations
#
# This file creates a domain of a 2D rectangle (single element wide) with 
# a blunt body (representing an infinitely-wide 'shield') within this domain. 
# This file also creates a head downstream of the shield, with an independent 
# 'nose' area that a specific boundary condition can be applied upon in foam. 
# The flow originates from a jet upstream (which is flowing around the shield). 
# 
# This template can be used to specify: domain size, shield angle, nose angle, 
# and mesh resolution and grading. The domain is meshed using structured grids 
# upstream of the shield (and unstructured grids downstream), which can be 
# graded to allow relaxation of the grid away from this blunt body. 

# Requirements
import gmsh
import math
gmsh.initialize()
gmsh.clear()


# Definitions
nameModel = 'mesh2dJet_rotationShield_nose'
gmsh.model.add(nameModel)
geoMod = gmsh.model.geo


# MODIFY: major parameters
centreX 					= 1575 	# head's centroid x-position
deltaX 						= 50 	# head width (front-to-back)
deltaY 						= 100 	# head length (height)
angle 						= 80 	# from vertical [degrees]
noseL 						= 14.5 	# nostril length (diameter)
mouthToShieldL 				= 1500	# length
domainL 					= 2000 	# length of total domain 
meshSize 					= 17.8  # size of triangular cells


# Create head including nose
centre = geoMod.addPoint(centreX, 500, 0)
pA1 = geoMod.addPoint(centreX + deltaX, 500, 0, meshSize)
pA2 = geoMod.addPoint(centreX, 500 + deltaY, 0, meshSize)
pA3 = geoMod.addPoint(centreX - deltaX, 500, 0, meshSize)
pA4 = geoMod.addPoint(centreX - deltaX + noseL * math.sin(math.radians(angle)), 
					  500 - noseL * math.cos(math.radians(angle)), 0, meshSize)
pA5 = geoMod.addPoint(centreX - deltaX + noseL, 500 - deltaY, 0, meshSize)
pA6 = geoMod.addPoint(centreX, 500 - deltaY, 0, meshSize)

majorAxis = 2 					# y-axis
arc1 = geoMod.addEllipseArc(pA1, centre, majorAxis, pA2)
arc2 = geoMod.addEllipseArc(pA2, centre, majorAxis, pA3)
arc3 = geoMod.addLine(pA3, pA4)
arc4 = geoMod.addLine(pA4, pA5)
arc5 = geoMod.addLine(pA5, pA6)
arc6 = geoMod.addEllipseArc(pA6, centre, majorAxis, pA1)

loopHead = geoMod.addCurveLoop([arc1, arc2, arc3, arc4, arc5, arc6])
surfHead = geoMod.addPlaneSurface([loopHead])
geoMod.synchronize()


# Create 1-grid thick shield (allowing easier boundary recognition 
# in OpenFOAM) 
pS1 = geoMod.addPoint(mouthToShieldL, 400, 0, meshSize)
pS2 = geoMod.addPoint(mouthToShieldL, 600, 0, meshSize)
pS3 = geoMod.addPoint(mouthToShieldL + 10, 600, 0, meshSize)
pS4 = geoMod.addPoint(mouthToShieldL + 10, 400, 0, meshSize)

lSh1 = geoMod.addLine(pS1, pS2)
lSh2 = geoMod.addLine(pS2, pS3)
lSh3 = geoMod.addLine(pS3, pS4)
lSh4 = geoMod.addLine(pS4, pS1)

loopShield = geoMod.addCurveLoop([lSh1, lSh2, lSh3, lSh4])


# Create surface around head then subtract head & shield
middleX = mouthToShieldL - 100
P2 = geoMod.addPoint(middleX, 300, 0, meshSize)
P4 = geoMod.addPoint(middleX, 490, 0, meshSize)
P5 = geoMod.addPoint(middleX, 510, 0, meshSize)
P7 = geoMod.addPoint(middleX, 700, 0, meshSize)

P8 = geoMod.addPoint(domainL, 700, 0, meshSize)
P9 = geoMod.addPoint(domainL, 300, 0, meshSize)

L2 = geoMod.addLine(P2, P4)
L4 = geoMod.addLine(P4, P5)
L5 = geoMod.addLine(P5, P7)
L7 = geoMod.addLine(P7, P8)
L8 = geoMod.addLine(P8, P9)
L9 = geoMod.addLine(P9, P2)

loopTets = geoMod.addCurveLoop([L2, L4, L5, L7, L8, L9])
surfTets = geoMod.addPlaneSurface([loopTets, loopHead, loopShield])
geoMod.synchronize()


# MODIFY: outer-boundary mesh: grading adjacent top/bottom boundaries
N = 18 					# number elements
r = 1.057 				# ratio
d = [10] 				# smallest grid size
for i in range(1, N): 
	d.append(d[-1] + (d[0]) * r**i)
d.pop()
d.append(300)
h_norm = []
for d_i in d:
	h_norm.append(d_i / 300)

noElemX = int((domainL - middleX) / meshSize)
geoMod.mesh.setTransfiniteCurve(L9, noElemX)
geoMod.mesh.setTransfiniteCurve(L7, noElemX)
line = [(1, L9)] 
extrude1 = geoMod.extrude(line, 
						  0, -300, 0,
						  numElements = [1] * N, 
						  heights = h_norm,
						  recombine = True)
line = [(1, L7)] 
extrude1 = geoMod.extrude(line, 
						  0, 300, 0,
						  numElements = [1] * N, 
						  heights = h_norm,
						  recombine = True)
geoMod.synchronize()


# MODIFY: mesh between mouth & shield: grading for streamwise direction
N = 80 					# number elements
r = 0.98493 			# ratio
d = [30] 				# largest grid size
for i in range(1, N): 
	d.append(d[-1] + (d[0]) * r**i)
d.reverse()
D = []
for d_i in d:
	D.append(d_i - 1400)
heights = []
for D_i in D:
	heights.append(D_i * -1)
heights.pop(0)
heights.append(1400)
h_norm = []
for h_i in heights:
	h_norm.append(h_i / 1400)


lines = [(1, 19), (1, L2), (1, L4), (1, L5), (1, 22)] 
extrude1 = geoMod.extrude(lines, 
						  -middleX, 0, 0,
						  numElements = [1] * N, 
						  heights = h_norm,
						  recombine = True)
geoMod.synchronize()


# Define mesh depth
gmsh.model.removeEntities([(2, 1)], True)
surfs = gmsh.model.getEntities(2)
extrude1 = geoMod.extrude(surfs, 
						  0, 0, meshSize,
						  numElements = [1], 
						  recombine = True)
geoMod.synchronize()


# Specify the domain (required for OpenFOAM): https://www.cfd-online.com/Forums/
# openfoam-meshing/185021-perhaps-you-have-not-exported-3d-elements.html
entitiesL = len(gmsh.model.getEntities(3))
entities = []
for i in range(1, entitiesL + 1):
	entities.append(i)
gmsh.model.addPhysicalGroup(3, entities)


# Group surfaces where same flow conditions can be applied in OpenFOAM (i.e. 
# assign same boundary conditions to this group). Surfaces found via GUI
gmsh.model.addPhysicalGroup(2, [231], name = "mouth")
gmsh.model.addPhysicalGroup(2, [187, 209, 253, 275], name = "solid")
gmsh.model.addPhysicalGroup(2, [89, 109, 105, 93, 97,
								113, 125, 117, 121], name = "faceShield")
gmsh.model.addPhysicalGroup(2, [101], name = "nose")
gmsh.model.addPhysicalGroup(2, [271, 165, 161, 81, 147, 143, 183], name = "atmos")
gmsh.model.addPhysicalGroup(2, [148, 126, 170, 192, 214, 236, 258, 280,
								20, 2, 24, 28, 32, 36, 40, 44], 
								name = "empty")


# Mesh then export/view
gmsh.option.setNumber("Mesh.Algorithm", 6)
gmsh.model.mesh.generate(3)
#gmsh.fltk.run()
gmsh.option.setNumber("Mesh.MshFileVersion",2.0) 
gmsh.write(nameModel + ".msh")
gmsh.finalize()