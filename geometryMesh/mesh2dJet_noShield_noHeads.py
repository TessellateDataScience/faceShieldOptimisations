# Gmsh meshing file: executes error-free using GMSH 4.11.1 
#
# File created and owned by Tessellate Data Science (www.tessellate.science). You can 
# re-use this file as long as you abide by our licencing. We're aiming to encourage 
# innovation, so any activity that hinders this goes against our wishes/intentions.

# requirements
import gmsh
gmsh.initialize()
gmsh.clear()


# modify: parameters [mm]
nameModel = "mesh2dJet_noShield_noHeads"
mouthH = 20
domainH = 600
domainL = 2000
meshSize = 60
depth = 70


# definitions
gmsh.model.add(nameModel)
geoMod = gmsh.model.geo


# 2D geometry
P6 = geoMod.addPoint(0, 0, 0, meshSize)
P5 = geoMod.addPoint(domainL, 0, 0, meshSize)
P4 = geoMod.addPoint(domainL, domainH, 0, meshSize)
P3 = geoMod.addPoint(0, domainH, 0, meshSize)
P2 = geoMod.addPoint(0, domainH / 2 + mouthH / 2, 0, meshSize)
P1 = geoMod.addPoint(0, domainH / 2 - mouthH / 2, 0, meshSize)

LMouth = geoMod.addLine(P1, P2)
L1 = geoMod.addLine(P2, P3)
L2 = geoMod.addLine(P3, P4)
L3 = geoMod.addLine(P4, P5)
L4 = geoMod.addLine(P5, P6)
L5 = geoMod.addLine(P6, P1)

Curve = geoMod.addCurveLoop([LMouth, L1, L2, L3, L4, L5])
Surf = geoMod.addPlaneSurface([Curve])
geoMod.synchronize()


# graded (hex) surface grid. Note the default method (BetaLaw = 0) results in 
# inconsistent (poor) grids adjacent the top and bottom lines after approximately 
# (1 / 2) of the length
gmsh.model.mesh.field.add("BoundaryLayer", 1)
gmsh.model.mesh.field.setNumber(1, "Quads", 1)
gmsh.model.mesh.field.setNumber(1, "Size", 10)
gmsh.model.mesh.field.setNumber(1, "BetaLaw", 1)
gmsh.model.mesh.field.setNumber(1, "NbLayers", 74)
gmsh.model.mesh.field.setNumber(1, "Beta", 1.15)
gmsh.model.mesh.field.setNumbers(1, "CurvesList", [L3])
gmsh.model.mesh.field.setNumbers(1, "PointsList", [P4, P5])
geoMod.synchronize()


# hex surface grid near mouth
geoMod.mesh.setTransfiniteCurve(LMouth, 5)
geoMod.mesh.setTransfiniteCurve(L1, 57)
geoMod.mesh.setTransfiniteCurve(L5, 57)
geoMod.mesh.setTransfiniteCurve(L3, 117)
geoMod.mesh.setTransfiniteCurve(L2, 1)
geoMod.mesh.setTransfiniteCurve(L4, 1)

geoMod.mesh.setTransfiniteSurface(Surf, "Left", [P6, P3, P4, P5])
geoMod.mesh.setRecombine(2, Surf)
geoMod.synchronize()


# volume including mesh
surfParams =  [(2, Surf)]
extrudeFaceL = geoMod.extrude(surfParams, 0, 0, depth, [1], recombine = True)
geoMod.synchronize()


# specify the domain (required for OpenFOAM): https://www.cfd-online.com/Forums/
# openfoam-meshing/185021-perhaps-you-have-not-exported-3d-elements.html
entitiesL = len(gmsh.model.getEntities(3))
entities = []
for i in range(1, entitiesL + 1):
	entities.append(i)
gmsh.model.addPhysicalGroup(3, entities)


# group surfaces into regions where same flow conditions can be applied (ie. assign 
# same boundary conditions to surfaces within this group). Surfaces found via GUI
gmsh.model.addPhysicalGroup(2, [17], name = "mouth")
gmsh.model.addPhysicalGroup(2, [1, 38], name = "empty")
gmsh.model.addPhysicalGroup(2, [21, 25, 29, 33, 37], name = "atmos")


# mesh parameters & generation
gmsh.model.mesh.field.setAsBoundaryLayer(1)
gmsh.option.setNumber("Mesh.Algorithm", 5)
geoMod.synchronize()

gmsh.model.mesh.generate(3)
gmsh.option.setNumber("Mesh.MshFileVersion",2.0) 
gmsh.write(nameModel + ".msh")


# view in graphical user-interface (GUI)
gmsh.fltk.run()
gmsh.finalize()