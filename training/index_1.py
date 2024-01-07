# encoding: utf-8
import arcpy
import os.path

arcpy.env.overwriteOutput = True

in_features = arcpy.GetParameterAsText(0)
out_workspace = arcpy.GetParameterAsText(1)

outSpatialRef = arcpy.SpatialReference(4326)

features = in_features.split(";")
for feature in features:
    out_feature = os.path.join(out_workspace, feature)
    arcpy.Project_management(feature, out_feature, outSpatialRef)
    arcpy.AddMessage(feature + " DONE!")
