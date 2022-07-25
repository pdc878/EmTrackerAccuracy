fromMarkupsNodeID_0 = slicer.modules.markups.logic().AddNewFiducialNode()
fromMarkupsNode_0 = getNode(fromMarkupsNodeID_0)
fromMarkupsNode_0.SetName("Compare_Points_0")

for z in range(0, 4):
   for y in range(0,5):
      for x in range(0,5):
         fromMarkupsNode_0.AddFiducial(x*120+150, y*100-200, z*50-100)





fromMarkupsNodeID_1 = slicer.modules.markups.logic().AddNewFiducialNode()
fromMarkupsNode_1 = getNode(fromMarkupsNodeID_1)
fromMarkupsNode_1.SetName("Compare_Points_1")

for z in range(0, 4):
   for y in range(0,5):
      for x in range(0,5):
         fromMarkupsNode_1.AddFiducial(x*120+150, y*100-200, z*50-100)





fromMarkupsNodeID_2 = slicer.modules.markups.logic().AddNewFiducialNode()
fromMarkupsNode_2 = getNode(fromMarkupsNodeID_2)
fromMarkupsNode_2.SetName("Compare_Points_2")

for z in range(0, 4):
   for y in range(0,5):
      for x in range(0,5):
         fromMarkupsNode_2.AddFiducial(x*120+150, y*100-200, z*50-100)
         
         
         

numFids = fromMarkupsNode_3.GetNumberOfControlPoints()

fp = vtk.vtkPoints()
f1 = [0, 0, 0,0]
f2 = [0, 0, 0,0]
f3 = [0, 0, 0,0]

fromMarkupsNodeID_average = slicer.modules.markups.logic().AddNewFiducialNode()
fromMarkupsNode_average = getNode(fromMarkupsNodeID_average)
fromMarkupsNode_average.SetName("Compare_Points_average")


for i in range(numFids):
  fromMarkupsNode_1.GetNthFiducialWorldCoordinates(i, f1)
  fromMarkupsNode_2.GetNthFiducialWorldCoordinates(i, f2)	
  fromMarkupsNode_3.GetNthFiducialWorldCoordinates(i, f3)
  
  x = (f1[0] + f2[0] + f3[0])/3
  y = (f1[1] + f2[1] + f3[1])/3
  z = (f1[2] + f2[2] + f3[2])/3
  fromMarkupsNode_average.AddFiducial(x, y, z)





fromMarkupsNodeID_3 = slicer.modules.markups.logic().AddNewFiducialNode()
fromMarkupsNode_3 = getNode(fromMarkupsNodeID_3)
fromMarkupsNode_3.SetName("Compare_Points_3")

for z in range(0, 4):
   for y in range(0,5):
      for x in range(0,5):
         fromMarkupsNode_3.AddFiducial(x*120+150, y*100-200, z*50-100)

