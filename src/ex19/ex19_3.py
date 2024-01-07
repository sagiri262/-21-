# encoding:utf-8
import os.path
import arcpy

# 2021b33040 赵旸
arcpy.env.workspace = ur'D:\1658386661779\QingzhouCity'
arcpy.env.overwriteOutput = True
# 2021b33040 赵旸
in_features = arcpy.GetParameterAsText(0)
clip_features = arcpy.GetParameterAsText(1)
out_workspace = arcpy.GetParameterAsText(2)
# 2021b33040 赵旸
features = in_features.split(";")
# 2021b33040 赵旸
out_f = os.path.join(out_workspace, features+"_clip")
# 2021b33040 赵旸
arcpy.Clip_analysis(in_features, clip_features, out_f)


