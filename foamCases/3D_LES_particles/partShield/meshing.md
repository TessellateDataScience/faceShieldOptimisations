# Meshing
## Mesh: 'checkMesh'
- Geometry errors must be removed (checkMesh will report 'Mesh OK.' if solvable).
- Can solve (run) with mesh quality issues such as skewness, aspect ratio, and non-orthogonality:
	- May lead to solver instability (i.e. diverging), and if not give significantly erroneous results [1].

## Mesh: non-orthogonality
- Significant maximum non-orthoganality (~ 80 degrees) required modification to fvSolution to increase number of corrector loops [2] to maintain solver stability: 
	PIMPLE
	{
	    nNonOrthogonalCorrectors    3;
	}
- Mesh size required iteration of differing meshing schemes. cfMesh's cartesianMesh [3] gave us a 'convergent' mesh as determined by checkMesh, besides non-orthogonality above. Some notable aspects include:
	- mesh size changes of relatively small magnitude (delta = 0.005 mm) caused zeroVolumedCells to vary slightly.
	- beyond a range of acceptable values, the number of 'bad' cells increased very significantly (we assume qualitative changes in the mesh topology are the cause).

### Footnotes
[1] Advanced meshing using OpenFOAM technology cfMesh: Mesh quality assessment in CFD: Checking mesh quality in OpenFOAM: www.wolfdynamics.com/training/CFMESH/cfmesh2017.pdf

[2] CFD Online: Running high non orthogonality mesh: Thanks to Kuzey Can Derman: https://www.cfd-online.com/Forums/openfoam-solving/249271-running-high-non-orthogonality-mesh.html

[3] cfMesh's cartesianMesh is hexahedra dominant, but will also introduce tetrahedra & polyhedra cells as required. cfMesh is available ready-to-roll with OpenFOAM-v2312: https://www.openfoam.com/news/main-news/openfoam-v2312