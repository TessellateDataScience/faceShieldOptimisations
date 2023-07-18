# File created and owned by Tessellate Data Science (www.tessellate.science). 
# You can re-use this file as long as you abide by our licencing. We're aiming 
# to encourage innovation, so any activity that hinders this goes against our 
# intentions: https://github.com/TessellateDataScience/faceShieldOptimisations
#
# This file creates a domain of a 2D rectangle (single element wide) while 
# allowing a blunt body (representing an infinitely-wide shield) to be easily 
# created in OpenFOAM within this domain. The flow originates from a jet upstream 
# (which is flowing around the shield). 
# 
# This template can be used to specify domain size, and mesh resolution and 
# grading. The domain is meshed using structured grids, which can be graded to 
# allow relaxation of the grid away from the shield (blunt body). 


# requirements
import gmsh
gmsh.initialize()
gmsh.clear()


# MODIFY: major parameters [mm]. You will also need to adjust further mesh 
# parameters below (specifically grid grading of 'all other surfaces' & 
# 'streamwise direction').
nameModel = "mesh2dJet_withShield_noHeads_case3"
mouthHeight = 20
shieldLength =200
distanceMouthToShield = 1500
distanceBehindShield = 500
depth = 70


# definitions
gmsh.model.add(nameModel)
geoMod = gmsh.model.geo


# mouth surface & grid
P1 = geoMod.addPoint(190, 0, 0)
P2 = geoMod.addPoint(190, depth, 0)
P3 = geoMod.addPoint(210, 0, 0)
P4 = geoMod.addPoint(210, depth, 0)

L1 = geoMod.addLine(P1, P3)
L2 = geoMod.addLine(P3, P4)
L3 = geoMod.addLine(P4, P2)
L4 = geoMod.addLine(P2, P1)

LoopMouth = geoMod.addCurveLoop([L1, L2, L3, L4]) # found via GUI
SurfMouth = geoMod.addPlaneSurface([LoopMouth])
geoMod.synchronize()

geoMod.mesh.setTransfiniteCurve(L1, 5)
geoMod.mesh.setTransfiniteCurve(L3, 5)
geoMod.mesh.setTransfiniteCurve(L2, 0)
geoMod.mesh.setTransfiniteCurve(L4, 0)
geoMod.mesh.setTransfiniteSurface(SurfMouth, "Left")
geoMod.mesh.setRecombine(2, SurfMouth)
geoMod.synchronize()


# MODIFY: grid grading on all other surfaces
N = 13 					# number elements
r = 1.124 				# ratio
d = [7] 				# first element thickness
for i in range(1, N): 
	d.append(d[-1] + (d[0]) * r**i)
d.pop()
d.append(200)
h_norm = []
for d_i in d:
	h_norm.append(d_i / 200)

extrude1 = geoMod.extrude([(1, L4)], -190, 0, 00, [27], recombine = True)
extrude2 = geoMod.extrude([(1, L2)], 190, 0, 00, [27], recombine = True)
extrude3 = geoMod.extrude([(1, 5)], 
						  -200, 0, 00, 
						  numElements = [1] * N, 
						  heights = h_norm,
						  recombine = True) # line found via GUI
extrude4 = geoMod.extrude([(1, 9)], 
						  200, 0, 00, 
						  numElements = [1] * N, 
						  heights = h_norm,
						  recombine = True)
geoMod.synchronize()


# MODIFY: grid grading for streamwise direction
N = 114 		# number elements
r = 0.992 		# ratio
d = [20] 		# first element thickness
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

N2 = 29
r = 1.05
d2 = [8]
for i in range(1, N2):
	d2.append(d2[-1] + (d2[0]) * r**i)
d2.pop()
d2.append(500)
hShield_norm = []
for d2_i in d2:
	hShield_norm.append((d2_i / 500) * +1)

surfs = gmsh.model.getEntities(2)
extrude1 = geoMod.extrude(surfs, 
						  0, 0, -distanceMouthToShield, 
						  numElements = [1] * N, 
						  heights = h_norm,
						  recombine = True)
extrude2 = geoMod.extrude(surfs, 
						  0, 0, distanceBehindShield, 
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


# group surfaces into regions where same flow conditions can be applied 
# (ie. assign same boundary conditions to surfaces within this group). Surfaces
# found via GUI
gmsh.model.addPhysicalGroup(2, [42], name = "mouth")
gmsh.model.addPhysicalGroup(2, [209, 165, 139, 195, 239, 99, 55, 29, 85, 129,
								121, 77, 37, 63, 107, 217, 173, 147, 187, 231], 
							name = "empty")
gmsh.model.addPhysicalGroup(2, [125, 102, 213, 152, 218, 174, 196, 240, 235, 103], 
							name = "atmos")
gmsh.model.addPhysicalGroup(2, [130, 86, 64, 108], name = "wall")


# mesh, save, then view mesh (in GUI)
gmsh.model.mesh.generate(3)
gmsh.option.setNumber("Mesh.MshFileVersion",2.0) 
gmsh.write(nameModel + ".msh")
gmsh.fltk.run()
gmsh.finalize()