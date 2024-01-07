# encoding: utf-8
import arcpy
import os

arcpy.env.overwriteOutput = True

in_features = arcpy.GetParameterAsText(0)
clip_features = arcpy.GetParameterAsText(1)
out_workspace = arcpy.GetParameterAsText(2)

features = in_features.split(";")
for feature in features:
    out_feature = os.path.join(out_workspace, feature+"_clip")
    arcpy.Clip_analysis(feature, clip_features, out_feature)
    arcpy.AddMessage("OUT" + out_feature)