fromFidsName = "Compare_Points_0"
toFidsName = "Compare_Points_average"
outputTransformName = "EmRefToOpRef"

fromFids = slicer.util.getFirstNodeByName(fromFidsName)
toFids = slicer.util.getFirstNodeByName(toFidsName)

numFids = fromFids.GetNumberOfControlPoints()

fp = vtk.vtkPoints()
tp = vtk.vtkPoints()
f = [0, 0, 0]
t = [0, 0, 0]

for i in range(numFids):
  fromFids.GetNthFiducialPosition(i, f)
  toFids.GetNthFiducialPosition(i, t)
  fp.InsertNextPoint(f)
  tp.InsertNextPoint(t)


tps = vtk.vtkThinPlateSplineTransform()
tps.SetSourceLandmarks(fp)
tps.SetTargetLandmarks(tp)
tps.SetBasisToR()

emRefToOpRefNode = slicer.mrmlScene.GetFirstNodeByName(outputTransformName)
if emRefToOpRefNode is None:
  emRefToOpRefNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTransformNode", outputTransformName)


emRefToOpRefNode.SetAndObserveTransformToParent(tps)
