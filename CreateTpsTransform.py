fromFidsName = "Em_Ref_Points"
toFidsName = "Op_Ref_Points"
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

emRefToOpRefNode = slicer.util.getFirstNodeByName(outputTransformName)
if emRefToOpRefNode is None:
  emRefToOpRefNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTransformNode", outputTransformName)


emRefToOpRefNode.SetAndObserveTransformToParent(tps)
