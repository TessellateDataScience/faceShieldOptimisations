# Geometry/Mesh creation of a 3D rectangular domain with a ball shape removed,
# using Gmsh's Python API.
# 
# Domain will be used to conduct a Computational Fluid Dynamics investigation
# of a jet flow that hits a ball. The jet represents someone talking, while 
# the ball represents someone else listening. 
# 
# This investigation will inform design innovation of Personal Protective 
# Equipment. For further information, or to get involved, regarding this 
# investigation please check the following link (defined here as the 'Link'): 
# www.github.com/TessellateDataScience/faceShieldOptimisations
# 
# Created by Nicholas Howlett. All applicable code and writing created by him
# in relation to this investigation is released under the Licenses written
# on the Link.
#
# Meshing of geometry will include both tetrahedrons & prisms, with prisms
# inside a 3D cylindrical region within the domain.

# requirements
import gmsh
gmsh.initialize()

# modify: parameters
gmsh.model.add("jetAroundBall_tetsPrisms")
L = 150
cylL = 100
rMouthMax = 2
rMouthMin = 1
rHead = 10

# log all messages
gmsh.logger.start()

# create outer domain
gmsh.model.occ.addBox(0, 0, 0, L, L, 2 * L)

# create ball
gmsh.model.occ.addSphere(L / 2, L / 2, 4 / 3 * L, rHead)

# create mouth
mouth = gmsh.model.occ.addDisk(L / 2, L / 2, 2 / 3 * L, rMouthMax, rMouthMin)

# create fluid domain
domain = gmsh.model.occ.cut([(3, 1)], [(3, 2)])

# create surface of cylinder

# requirement before meshing
gmsh.model.geo.synchronize()

# create mesh within cylinder: extruding cylinder surface
#ov = gmsh.model.geo.extrude([(2, 1)], 0, 0, cylL, [numMeshElements])

# merge cylinder to fluid domain

# mesh remaining fluid domain
gmsh.model.mesh.generate(3)

# create boundary conditions

# inspect the log
log = gmsh.logger.get()
print("Logger has recorded " + str(len(log)) + " lines")
gmsh.logger.stop()

# save mesh then clear
#gmsh.write("test.msh")
gmsh.finalize()
