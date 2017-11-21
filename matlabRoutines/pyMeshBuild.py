#!/usr/bin/python

## HEALTH WARNING - BETA CODE IN DEVELOPMENT ##

'''
This standalone application will build a mesh from a nifti classification file.
To keep the procedure as similar as possible to the way mrMesh used to do this,
we will keep this as a standalon application. Matlab reads in the segmented 
nifti file using vistasofts own nifti class handler meshBuild>mrmBuild>
meshBuildFromClass - we just dont use the old build_mesh mex file - we do that
bit and any smoothing in this application and send a mesh struture back to
matlab.

AG 2017
'''

import os,sys
import scipy
import vtk

from numpy import *
from scipy.io import loadmat, savemat
from vtk.util import numpy_support

debug = True

'''
from matlab generate some voxels
filename = '/groups/Projects/P1215/data/fMRI/structural/lr_flip_freesurfer_class_to_vista.nii.gz';
msh = meshBuildFromNiftiClass_mrMeshPy(filename,'left'); %puts voxels in workspace
voxels = permute(voxels,[3,2,1]);
save /tmp/voxels.mat voxels;
system('/groups/examples/mrMeshPy/mrMeshPy/matlabRoutines/launchMeshBuild.sh /groups/examples/mrMeshPy/testCode/testMeshBuild.py')
'''

# load the voxel data that has been dumped to disk
voxels = scipy.io.loadmat('/tmp/voxels.mat')
mmPerVox = voxels['mmPerVox'][0]
if debug: print mmPerVox

voxels = voxels['voxels'] #unpack

if debug: print voxels

if debug: print shape(voxels)

extent = shape(voxels)
if debug: print extent
if debug: print extent[0]
if debug: print extent[1]
if debug: print extent[2]


# import voxels to vtk
dataImporter = vtk.vtkImageImport()
data_string = voxels.tostring()
dataImporter.CopyImportVoidPointer(data_string, len(data_string))
dataImporter.SetDataScalarTypeToUnsignedChar()
dataImporter.SetDataExtent(0, extent[2]-1, 0, extent[1]-1, 0, extent[0]-1) # TODO have to work this out
dataImporter.SetWholeExtent(0, extent[2]-1, 0, extent[1]-1, 0, extent[0]-1) # TODO have to work this out
dataImporter.SetDataSpacing(mmPerVox[0],mmPerVox[1],mmPerVox[2]) # TODO have to work this out
dataImporter.Update()


if debug: print dataImporter.GetOutput()

# mc = vtk.vtkContourFilter() #- could use a contour filter instead?
mc = vtk.vtkMarchingCubes()
mc.SetInputConnection(dataImporter.GetOutputPort())
mc.SetValue(0,0.5) #extract 0-th surface at 0.5?
mc.ComputeGradientsOff()
#mc.ComputeNormalsOff()
mc.ComputeScalarsOff()
mc.Update()

if debug: print mc.GetOutput()


# ---- Initial vertices - unsmoothed ---------------------
init_verts = mc.GetOutput().GetPoints().GetData()
output_init_verts = array(numpy_support.vtk_to_numpy(init_verts).transpose(),'d')

if debug: print output_init_verts


# ---- Polys (triangles) ---------------------
triangles = mc.GetOutput().GetPolys().GetData()
tmp_triangles = numpy_support.vtk_to_numpy(triangles)

# N.B. the polygon data returned here have 4 values for poly - the first is the number
# of vertices that describe the polygo (ironically always 3) and the next 3 are the 
# indices of the vertices that make up the polygon

# so first we need to reshape data from a vector
tmp_triangles = reshape(tmp_triangles,(len(tmp_triangles)/4,4))

# and then we drop the first column (all 3's)
output_triangles = array((tmp_triangles[:,1:4]).transpose(),'d') #remember zero index here, add one for matlab

if debug: print output_triangles


# ---- Normals ---------------------

## normals already computed by mc algorithm so this code is obsolete
#normals = vtk.vtkPolyDataNormals()
#normals.SetInputConnection(mc.GetOutputPort())
#normals.Update()
#print normals.GetOutput()


norm = mc.GetOutput().GetPointData().GetNormals()
output_normals = array(numpy_support.vtk_to_numpy(norm).transpose(),'d')

if debug: print output_normals


# -------- smoothed version of mesh ----------------

smooth = vtk.vtkSmoothPolyDataFilter()
smooth.SetNumberOfIterations(0) #standard value sused in old mrMesh
smooth.SetRelaxationFactor(0.1) #standard value sused in old mrMesh
smooth.FeatureEdgeSmoothingOff()
smooth.SetInputConnection(mc.GetOutputPort())
smooth.Update()

# ---- Vertices - smoothed ---------------------
smooth_verts = smooth.GetOutput().GetPoints().GetData()
output_smooth_verts = array(numpy_support.vtk_to_numpy(smooth_verts).transpose(),'d')

if debug: print output_smooth_verts


# ---- Curvature ---------------------
curvature = vtk.vtkCurvatures()
curvature.SetInputConnection(smooth.GetOutputPort())
curvature.SetCurvatureTypeToMean()
curvature.Update()

curv = curvature.GetOutput().GetPointData().GetScalars()
output_curvature = array(numpy_support.vtk_to_numpy(curv).transpose(),'d')

print min(output_curvature)
print max(output_curvature)

if debug: print output_curvature


# -------- colours based on curvature ------------

# turn curvature into color
tmp_colors = output_curvature.copy()

#min_curv = min(tmp_colors)
#max_curv = max(tmp_colors)
#tmp_colors = (tmp_colors -min_curv) / (max_curv-min_curv) *255

tmp_colors[tmp_colors>=0] = 160 #standard value sused in old mrMesh
tmp_colors[tmp_colors<0] = 78 #standard value sused in old mrMesh

output_colors = vstack((tmp_colors, tmp_colors, tmp_colors, ones((1,len(tmp_colors)))*255))
output_colors = array(output_colors,'d')

if debug: print output_colors

# OK we have all the data we need now, lets write it out to file

data = {} #empty dictionary
data['initVertices'] = output_init_verts
data['initialvertices'] = output_init_verts
data['vertices'] = output_smooth_verts
data['colors'] = output_colors
data['normals'] = output_normals
data['triangles'] = output_triangles
data['curvature'] = output_curvature

savemat('/tmp/temp2.mat',data)


pdm = vtk.vtkPolyDataMapper()
pdm.SetInputConnection(mc.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(pdm)

ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

ren.AddActor(actor)
ren.SetBackground(1,1,1)
renWin.SetSize(500,500)

iren.Initialize()
iren.Start()



pdm = vtk.vtkPolyDataMapper()
pdm.SetInputConnection(smooth.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(pdm)

ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

ren.AddActor(actor)
ren.SetBackground(1,1,1)
renWin.SetSize(500,500)

iren.Initialize()
iren.Start()

