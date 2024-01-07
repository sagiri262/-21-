import arcpy
import os

arcpy.env.overwriteOutput = True

in_features = arcpy.GetParameterAsText(0)
clip_features = arcpy.GetParameterAsText(1)
out_path = arcpy.GetParameterAsText(2)

features = in_features.split(";")

for fe in features:
    arcpy.AddMessage()
    out_file = os.path.join(out_path, fe + "_clip")
    arcpy.Clip_analysis(fe, clip_features, out_file)
    
