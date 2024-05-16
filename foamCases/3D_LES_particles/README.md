# README: 3D OpenFOAM simulations with particle tracking
## Summary
Our 3D cases are developed/tested using _OpenFOAM-dev_. Prior to running OpenFOAM, our mesh (and geometry) was developed using both _GMSH_ & _cfMesh_ (ready-to-roll with _OpenFOAM-2312_). Below is some advice for getting your computations going (refer to the README: 2D OpenFOAM simulations for prerequisite advice).

## Meshing
Our mesh included using a non-conformal interface that surrounded the shield region. This allowed the complex geometry of the region surrounding the shield to be meshed using polyhedra elements (cfMesh). The remaining domain was meshed using a structured O-grid topology while embedding the mouth outline around the centre (Gmsh).

### Gmsh
This stand-alone software allows meshing using both tetrahedra & hexahedra elements (cells). For our geometry (in './partOther'), we used this Python-based module to create most of the domain (leaving a volume that represented the region surrounding the shield un-meshed). We used Gmsh from within _IPython_, a Python intepreted that has enhanced features such as colouring of syntax. We used Gmsh on Linux (www.gmsh.info), using _Ubuntu_ via Windows Subsystem for Linux (www.learn.microsoft.com/en-us/windows/wsl/about). 

### cfMesh
This OpenFOAM-integrated module allows meshing using polyhedra elements (in addition to tetrahedra and hexahedra elements that are also available). For our geometry (in './partShield'), we used the `cartesianMesh` module that incorporated a combination of predominantly hexahedra, tetrahedra, & some polyhedra elements. To make cfMesh available for use, you'll need to install OpenFOAM v2312 (www.openfoam.com/news/main-news/openfoam-v2312).

Due to the complex geometry of incorporating a shield/head/body into the domain, we ran a semi-iterative meshing sequence to pinpoint exact mesh sizing parameters that resulted in acceptable quality metrics (as determined by `checkMesh`). Further mesh sizing advice is given in './partShield/meshing.md'.

## OpenFOAM
Our case files are suitable for _OpenFOAM-11_ and OpenFOAM-dev (build): dev-fb4d7abf4217 (www.openfoam.org/download/dev-ubuntu). This case includes files allowing 'particle tracking' that could represent airborne viruses (bio-aerosols). Unlike the 2D case, here particle's trajectories are calculated concurrently alongside the flow. Due to technical limitations, OpenFOAM-dev is preferred to allow more control of the introduction of these particles. The same turbulence modelling is used here as in our 2D OpenFOAM simulations.

## Computations
We have utilised a moderately-powerful hardware platform consisting of 20 Xeon-based processors. The Ubuntu 22 LTS (Server) operating system was installed before installing OpenFOAM-dev. Using all processors on a single case (i.e. 'parallelised') resulted in computing the flow for 20 [secs] within a 24 [hour] computational-time period. Our computation time was significantly increased due to numerically having to accomodate moderately-high mesh non-orthogonality.

### Footnotes
_Software_ that needs installation. Software is generally 'open-source' thus free-of-charge to use and explore.