# encoding: utf-8
import os
import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = ur'D:\1658386661779\raster-lx'

input_tifs = arcpy.GetParameterAsText(0)
mask_shp = arcpy.GetParameterAsText(1)
out_path = arcpy.GetParameterAsText(2)

in_tif = input_tifs.split(";")
for input_tif in input_tifs:
    outfiles = os.path.join(out_path, input_tif+"_clip")
    arcpy.Clip_analysis(input_tif, mask_shp, outfiles)
