# encoding: utf-8
import arcpy

arcpy.env.workspace = ur'D:\ExperimentData\pythonProject\1658386661779\QingzhouCity'
sr = arcpy.SpatialReference(4326)
# espg的值代表不同的地里及投影坐标系
# espg = 4326 就是WGS-1984

out_layer = 'place_xy_lyr'
lyr = arcpy.MakeXYEventLayer_management('Outpoint.txt', 'POINT_X', 'POINT_Y', out_layer, sr)
arcpy.FeatureclassToCoverage_conversion(out_layer, r'D:\ExperimentData\pythonProject\ex17', 'outpoints.shp')
