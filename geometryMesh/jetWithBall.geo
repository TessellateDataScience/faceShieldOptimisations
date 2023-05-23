// -----------------------------------------------------------------------------
//  Gmsh geometry file
//
//  Geometry creation of a 3D rectangular domain with a ball shape removed.
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

SetFactory("OpenCASCADE"); 			// use alternative method of construction

Mesh.MeshSizeFromPoints = 0; 		// mesh using file following this one

// 3D rectangle representing domain boundary

L = 150; 							// dimension of shorter box length
rMaxMouth = 2;
rMinMouth = 1;
Box(1) = {0, 0, 0, L, L, 2 * L}; 	// only with OpenCASCADE kernel (method)

// Sphere representing head

Sphere(2) = {0.5 * L, 0.5 * L, 4 / 3 * L, 5}; 

// Actual fluid domain

BooleanDifference(3) = { Volume{1}; }{ Volume{2}; };

// Surface representing mouth

Disk(10) = {0.5 * L, 0.5 * L, 2 / 3 * L, rMaxMouth, rMinMouth}; // constraint: Rx >= Ry

// Boundary Conditions

//TODO: assign articular surfaces to groups (including to: sphere surface, jet source, domain's enclosing surface around it's volume) 
