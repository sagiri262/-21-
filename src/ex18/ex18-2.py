# encoding: utf-8
import arcpy

# 2021b33040 赵旸
# 设置工作空间
arcpy.env.workspace = r'D:\1658386661779\QingzhouCity'

sr = arcpy.SpatialReference(4326)
out_layer = 'place_xy_lyr'

arcpy.MakeXYEventLayer_management('Outpoint.txt', 'POINT_X', 'POINT_Y', out_layer, sr)
arcpy.FeatureclassToCoverage_conversion(out_layer, r'D:\1658386661779\savefile', "outpoints-1.shp")

