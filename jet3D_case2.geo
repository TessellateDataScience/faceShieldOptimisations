// -----------------------------------------------------------------------------
//  Gmsh geometry file
//
//  3D geometry of ball within a rectangular domain.
//
//  Domain will be used to conduct a Computational Fluid Dynamics investigation
//  of a jet flow that hits a ball. The jet represents someone talking, while 
//  the ball represents someone else listening. 
//
//  This investigation will inform design innovation of Personal Protective 
//  Equipment. For further information, or to get involved, regarding this 
//  investigation please check the following link (defined here as the 'Link'): 
//  www.github.com/TessellateDataScience/faceShieldOptimisations
//  
//  Created by Nicholas Howlett. All applicable code and writing created by him
//  in relation to this investigation is released under the Licenses written
//  on the Link.
// -----------------------------------------------------------------------------

SetFactory("OpenCASCADE"); // use alternative 'kernel' (method of construction)

Mesh.MeshSizeFromPoints = 0; // mesh using file following this one

// create 3D rectangle representing domain boundary

L = 150; // dimension of shorter box length
Box(1) = {0, 0, 0, L, L, 2 * L}; // only usable with OpenCASCADE kernel

// create sphere representing head

Sphere(2) = {0.5 * L, 0.5 * L, 4 / 3 * L, 5}; 

// create actual fluid domain

BooleanDifference(3) = { Volume{1}; }{ Volume{2}; };

// create surface representing mouth

Disk(10) = {0.5 * L, 0.5 * L, 2 / 3 * L, 2, 1}; // constraint: Rx >= Ry

// create BC's 