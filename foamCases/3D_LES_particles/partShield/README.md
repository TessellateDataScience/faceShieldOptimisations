# README: nostrils' surface: angled non-horizontally with quality meshing
## Summary
This development branch aims to allow geometry variation, namely nostrils' entry 'surface' with a direction vector that is not only vertical. Also, better meshing of nostrils' surface is proposed as preliminary computational investigations perhaps suggest flow resolution is unusual (we believe due to poor geometry representation, i.e. nostrils' geometrically planar surface is changed into non-planar triangles after meshing).

## Rationale
We believe a 'parameter study' involving varying nostrils angle will produce significantly novel flow dynamics, especially when the shield geometry is also varied. This could allow more fundamental type research and associated publication in traditional higher impact-factor journals. 

## Quickstart
A premade workflow is attached for guidance: see 'caseSetup.sh'. We currently are able to mesh only part of the nostrils' entry with a planar representation (~ half still appears non-planar). Some other software will be needed to be installed besides OpenFOAM-dev.