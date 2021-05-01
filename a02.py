
        
import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import ghpythonlib.treehelpers as th 
import math

# pointList1 = []
# x=50
# for i in range(x):
#     point = rg.Point3d(i,0,0)
#     pointList1.append(point)
# #a = pointList1

# pointList2 = []
# y=50
# for i in range(x):
#     point = rg.Point3d(i,y,0)
#     pointList2.append(point)
# #b = pointList2

# lines1 = []
# for i in range(len(pointList1)):
#     line = rg.Line(pointList1[i], pointList2[i])
#     lines1.append(line)
# #c = lines1

# pointsCurve= []
# v=3
# for i in lines1:
#     #print(i)
#     #print(type(i))
#     crv = i.ToNurbsCurve()
#     #print(crv)
#     param = crv.DivideByCount(v, True)
#     divPoints = []
#     for j in param:
#         divPoints.append(crv.PointAt(j))
#     pointsCurve.append(divPoints)
    
# #d = th.list_to_tree(pointsCurve)

# movedPts = []
# u=6
# for list in pointsCurve:
#     moved = []
#     for i in list:
#         print(i)
#         print(type(i))
#         vec = rg.Vector3d(i)
#         length = vec.Length
#         mag = math.sin(length)
#         vec2 = rg.Vector3d(0, 0,mag*u)
#         pt = i - vec2
#         moved.append(pt)
#     movedPts.append(moved)
# #e = th.list_to_tree(movedPts)

# curves = []
# for list in movedPts:
#     crv = rg.Curve.CreateInterpolatedCurve(list, 3)
#     curves.append(crv)
# #f = curves

# srf= rg.Brep.CreateFromLoft(curves, rg.Point3d.Unset, rg.Point3d.Unset, 0, False)
# #g = srf

# h = rg.Mesh.CreateFromBrep(srf[0], rg.MeshingParameters(0, v))

#1.
#compute face normals using rg.Mesh.FaceNormals.ComputeFaceNormals()
#output the vectors to a

a = rg.Mesh.Normals().ComputeFaceNormals()

#2.
#get the centers of each faces using rg.Mesh.Faces.GetFaceCenter()
#store the centers into a list called centers 
#output that list to b

centers = rg.Mesh.Faces.GetFaceCenter()

b = centers

#3.
#calculate the angle between the sun and each FaceNormal using rg.Vector3d.VectorAngle()
#store the angles in a list called angleList and output it to c

angleList = rg.Vector3d.VectorAngle()

c = angleList


#4. explode the mesh - convert each face of the mesh into a mesh
#for this, you have to first copy the mesh using rg.Mesh.Duplicate()
#then iterate through each face of the copy, extract it using rg.Mesh.ExtractFaces
#and store the result into a list called exploded in output d
exploded = []
meshcopy = rg.Mesh.Duplicate()
for face in meshcopy:
    extratface = rg.Mesh.ExtractFaces(face)
    exploded.append(extractface)
d = exploded

#after here, your task is to apply a transformation to each face of the mesh
#the transformation should correspond to the angle value that corresponds that face to it... 
#the result should be a mesh that responds to the sun position... its up to you!
