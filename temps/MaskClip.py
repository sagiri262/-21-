# encoding:utf-8
import arcpy
import os
from arcpy.sa import *
from arcpy import env

arcpy.env.overwriteOutput = True

in_rasters = arcpy.GetParameterAsText(0)
in_mask_data = arcpy.GetParameterAsText(1)
out_workspace = arcpy.GetParameterAsText(2)

rasters = in_rasters.split(";")
for raster in rasters:
    out_raster = ExtractByMask(raster, in_mask_data)
    out_raster.save(os.path.join(out_workspace), "mask_" + raster)
    arcpy.AddMessage("Out " + out_raster.catalopPath)