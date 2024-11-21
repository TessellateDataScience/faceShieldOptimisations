# README: Bioaerosol trajectories within speech-driven airflow with turbulence (LES) modelling
## Summary
Our 3D cases are developed/tested using _OpenFOAM-12_. Prior to running OpenFOAM, our mesh (and geometry) was developed using both _GMSH_ & _cfMesh_ (ready-to-roll with _OpenFOAM-2312_). Below is some background information for getting you up-to-speed to do further development.

## Meshing
Our mesh included using a non-conformal interface that surrounded the shield region. This allowed the complex geometry of the region surrounding the shield to be meshed using polyhedra elements (cfMesh). The remaining domain was meshed using a structured O-grid topology while embedding the mouth outline around the centre (Gmsh).

### Gmsh
This stand-alone software allows meshing using both tetrahedra & hexahedra elements (cells). For our geometry (in './partOther'), we used this Python-based module to create most of the domain (leaving a volume that represented the region surrounding the shield un-meshed). We used Gmsh from within _IPython_, a Python intepreted that has enhanced features such as colouring of syntax. We used Gmsh on Linux (www.gmsh.info), using _Ubuntu_ via Windows Subsystem for Linux (www.learn.microsoft.com/en-us/windows/wsl/about). 

### cfMesh
This OpenFOAM-integrated module allows meshing using polyhedra elements (in addition to tetrahedra and hexahedra elements that are also available). For our geometry (in './partShield'), we used the `cartesianMesh` module that incorporated a combination of predominantly hexahedra, tetrahedra, & some polyhedra elements. To make cfMesh available for use, you'll need to install OpenFOAM v2312 (www.openfoam.com/news/main-news/openfoam-v2312). cfMesh meshing advice is given in './partShield/meshing.md'.

## OpenFOAM
Our case files are suitable for _OpenFOAM-12_ (www.openfoam.org/download). This case includes files allowing 'particle tracking' that could represent airborne viruses (bioaerosols). These particles' trajectories are calculated concurrently alongside the airflow. Due to technical limitations, OpenFOAM > 11 is preferred to allow more control of the introduction of these particles. The turbulence modelling used is Large Eddy Simulation.

### Computational effort
We utilised a moderately-powerful hardware platform consisting of 20 Xeon-based processors. The Ubuntu 22 LTS (Server) operating system was installed before installing OpenFOAM. Using all processors on a single case (i.e. 'domain decomposition') resulted in simulating the flow for ~ 60 [secs] using 7.5 [hours] computing (real) time, using the provided case.

### Speech-driven flow
The airflow out of the mouth is specified via a custom 'boundary condition' (located in 'BCmouthVel'). This condition represents the assumed general flow of speech over a significant period of time by randomising the direction of flow at the mouth (assumed a surface of constant area). Turbulence generation is represented via smaller random variations away from the main axial (constant) velocity. Both randomisations are assumed normally distributed with a relatively large total range (as compared to the mean flow magnitude).

### Getting started
We've provided a fully-functional case ready for 'solving' in OpenFOAM (located in './combined'. But you'll first need to 'compile' our boundary condition to allow it's use: `cd ./BCmouthVel`. 

#### Boundary condition
In './Make/files' change the path of compiled program to make it applicable to your name. Then `wmake`, and ensure sure no errors ( likely highlighted in red) are seen. Then, in '../combined/system/controlDict' ensure the path is also reflected. 

#### Solving
Change into the './combined' directory then `foamRun` to start brute-forcing the mathematical 'governing' equations at every time-step (you'll see lots of solving-related information on your screen). To stop the solver press 'Ctrl + z' then `ps` to find the foamRun process, then `kill -9 <ID>`. 

#### Further development
If you're wanting to do a parameter variation (bioaerosol inhalation rate as function of shield length, for example), you'll need to redo and merge the mesh components. See 'caseSetup' in respective directories for meshing process. Also see 'meshing.md' for guidance on meshing via cfMesh (around the person & shield). 

## Footnotes
_Software_ that needs installation. Software is generally 'open-source' thus free-of-charge to use and explore.