#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.9.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'D:/Documents/devProjects/cfd/airflowAroundShields/1-jet2D_case3-0')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
centreHead_1 = geompy.MakeVertex(0, 0, 0)
centreHead_2 = geompy.MakeVertex(0, 120, 0)
CircleHead_1 = geompy.MakeCircle(centreHead_1, OZ, 10)
CircleHead_2 = geompy.MakeCircle(centreHead_2, OZ, 10)
Vertex_1 = geompy.MakeVertex(2.5, 0, 0)
Vertex_2 = geompy.MakeVertex(2.5, 15, 0)
Vertex_3 = geompy.MakeVertex(-2.5, 15, 0)
Vertex_4 = geompy.MakeVertex(-2.5, 0, 0)
Vertex_1_1 = geompy.MakeVertex(-2.5, 0, 0)
Line_L = geompy.MakeLineTwoPnt(Vertex_1_1, Vertex_3)
Line_R = geompy.MakeLineTwoPnt(Vertex_1, Vertex_2)
Vertex_R = geompy.MakeVertexOnLinesIntersection(CircleHead_1, Line_R)
Vertex_L = geompy.MakeVertexOnLinesIntersection(Line_L, CircleHead_1)
Line_1 = geompy.MakeLineTwoPnt(Vertex_R, Vertex_2)
Line_2 = geompy.MakeLineTwoPnt(Vertex_2, Vertex_3)
Line_3 = geompy.MakeLineTwoPnt(Vertex_3, Vertex_L)
Line_1_vertex_2 = geompy.GetSubShape(Line_1, [2])
Line_4 = geompy.MakeLineTwoPnt(Vertex_L, Line_1_vertex_2)
FaceRect = geompy.MakeFaceWires([Line_1, Line_2, Line_3, Line_4], 1)
FaceHead_1 = geompy.MakeFaceWires([CircleHead_1], 1)
FaceHead_2 = geompy.MakeFaceWires([CircleHead_2], 1)
FaceMouthHead_1 = geompy.MakeCutList(FaceHead_1, [FaceRect], True)
Vertex_5 = geompy.MakeVertex(210, -210, 0)
Vertex_7 = geompy.MakeVertex(210, 430, 0)
Vertex_8 = geompy.MakeVertex(-210, 430, 0)
Vertex_9 = geompy.MakeVertex(-210, -210, 0)
Line_5 = geompy.MakeLineTwoPnt(Vertex_9, Vertex_8)
Line_6 = geompy.MakeLineTwoPnt(Vertex_8, Vertex_7)
Line_7 = geompy.MakeLineTwoPnt(Vertex_7, Vertex_5)
Line_8 = geompy.MakeLineTwoPnt(Vertex_5, Vertex_9)
FaceRectDomain = geompy.MakeFaceWires([Line_5, Line_6, Line_7, Line_8], 1)
FaceDomain = geompy.MakeCutList(FaceRectDomain, [FaceHead_2, FaceMouthHead_1], True)
Head_1 = geompy.CreateGroup(FaceDomain, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Head_1, [17, 15])
Mouth = geompy.CreateGroup(FaceDomain, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Mouth, [12])
Boundary = geompy.CreateGroup(FaceDomain, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Boundary, [3, 8, 10, 6])
Head_2 = geompy.CreateGroup(FaceDomain, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Head_2, [19])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( centreHead_1, 'centreHead-1' )
geompy.addToStudy( centreHead_2, 'centreHead-2' )
geompy.addToStudy( CircleHead_1, 'CircleHead-1' )
geompy.addToStudy( CircleHead_2, 'CircleHead-2' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Vertex_3, 'Vertex_3' )
geompy.addToStudy( Vertex_4, 'Vertex_4' )
geompy.addToStudy( Vertex_1_1, 'Vertex_1' )
geompy.addToStudy( Line_L, 'Line_L' )
geompy.addToStudy( Line_R, 'Line_R' )
geompy.addToStudy( Vertex_R, 'Vertex_R' )
geompy.addToStudy( Vertex_L, 'Vertex_L' )
geompy.addToStudy( Line_1, 'Line_1' )
geompy.addToStudy( Line_2, 'Line_2' )
geompy.addToStudy( Line_3, 'Line_3' )
geompy.addToStudyInFather( Line_1, Line_1_vertex_2, 'Line_1:vertex_2' )
geompy.addToStudy( Line_4, 'Line_4' )
geompy.addToStudy( FaceRect, 'FaceRect' )
geompy.addToStudy( FaceHead_1, 'FaceHead-1' )
geompy.addToStudy( FaceHead_2, 'FaceHead-2' )
geompy.addToStudy( FaceMouthHead_1, 'FaceMouthHead-1' )
geompy.addToStudy( Vertex_5, 'Vertex_5' )
geompy.addToStudy( Vertex_7, 'Vertex_7' )
geompy.addToStudy( Vertex_8, 'Vertex_8' )
geompy.addToStudy( Vertex_9, 'Vertex_9' )
geompy.addToStudy( Line_5, 'Line_5' )
geompy.addToStudy( Line_6, 'Line_6' )
geompy.addToStudy( Line_7, 'Line_7' )
geompy.addToStudy( Line_8, 'Line_8' )
geompy.addToStudy( FaceRectDomain, 'FaceRectDomain' )
geompy.addToStudy( FaceDomain, 'FaceDomain' )
geompy.addToStudyInFather( FaceDomain, Head_1, 'Head-1' )
geompy.addToStudyInFather( FaceDomain, Mouth, 'Mouth' )
geompy.addToStudyInFather( FaceDomain, Boundary, 'Boundary' )
geompy.addToStudyInFather( FaceDomain, Head_2, 'Head-2' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
