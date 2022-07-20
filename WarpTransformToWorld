fromFidsName = "Compare_Points_0"
toFidsName = "Compare_Points_average"
outputTransformName = "Averaged_EmRefToOpRef"

coolTransform = "EmPointerToOpRef"
EmToOp = slicer.util.getFirstNodeByName(coolTransform)
EmToOp_Matrix=  EmToOp.GetMatrixTransformToParent()

fromFids = slicer.util.getFirstNodeByName(fromFidsName)
toFids = slicer.util.getFirstNodeByName(toFidsName)

fromFids_Word = slicer.util.arrayFromMarkupsControlPoints(fromFids, world=True)
toFids_Word = slicer.util.arrayFromMarkupsControlPoints(toFids, world=True)


numFids = fromFids.GetNumberOfControlPoints()

fp = vtk.vtkPoints()
tp = vtk.vtkPoints()
f = [0, 0, 0]
t = [0, 0, 0]

for i in range(numFids):
  fromFids.GetNthFiducialPosition(i, f)
  toFids.GetNthFiducialPosition(i, t)
  
  fp.InsertNextPoint(fromFids_Word[i])
  tp.InsertNextPoint(toFids_Word[i])


tps = vtk.vtkThinPlateSplineTransform()
tps.SetSourceLandmarks(fp)
tps.SetTargetLandmarks(tp)
tps.SetBasisToR()

emRefToOpRefNode = slicer.mrmlScene.GetFirstNodeByName(outputTransformName)
if emRefToOpRefNode is None:
  emRefToOpRefNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTransformNode", outputTransformName)


emRefToOpRefNode.SetAndObserveTransformToParent(tps)


