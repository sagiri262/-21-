# encoding:utf-8
import arcpy
import os

arcpy.env.overwriteOutput = True

# 输入数据
in_features = arcpy.GetParameterAsText(0)
clip_features = arcpy.GetParameterAsText(1)
out_workspace = arcpy.GetParameterAsText(2)

features = in_features.split(";")
for feature in features:
    out_feature = arcpy.Clip_analysis(feature, clip_features)
    '''
    Clip_analysis(in_features, clip_features)
    in_features：输入被裁剪的数据
    clip_features：用于裁剪的数据
    '''
