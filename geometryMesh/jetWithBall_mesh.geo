// -----------------------------------------------------------------------------
//  Gmsh meshing file
//
//  Meshing of a 3D rectangular domain with a ball shape removed. 
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
//
//  The mesh has increased mesh density within a cylinder joining the ball and 
//  jet. Mesh density also increases towards the ball's surface.
// -----------------------------------------------------------------------------

// Use predefined geometry

Include "jet3D_case2.geo";

// Mesh sizes (global & local)

mshSizeG = 6.0;
mshSizeL = 1.5;
Mesh.MeshSizeMin = mshSizeL;

// Local mesh refinement

Field[1] = Cylinder;			// cylinder between jet and ball
Field[1].VIn = mshSizeL;
Field[1].VOut = mshSizeG;
Field[1].Radius = rMaxMouth;
Field[1].XAxis = 0;
Field[1].YAxis = 0;
Field[1].ZAxis = 50;			// magnitude for each direction
Field[1].XCenter = 0.5 * L;
Field[1].YCenter = 0.5 * L;
Field[1].ZCenter = L;

//TODO: "mesh density increase approaching surface of ball"

//TODO: "mesh transition from cylinder end to mouth (elipse) faces"

Background Field = 1;			// requirement for meshing with Field

// Mesh geometry then save mesh

Mesh.Algorithm = 5; // more robust to spatial mesh-size changes than algo. = 6
Mesh 3;				// mesh 3D geometry ('Mesh 2' represents a surface)
//Save "mesh.unv";
