# encoding: utf-8

import arcpy

arcpy.env.workspace = ur'D:\ExperimentData\pythonProject\1658386661779\QingzhouCity'

fcs = arcpy.ListFeatureClasses()

wkid = 4524
srs = arcpy.SpatialReference(wkid)
print (srs.name)


# epsg 3857 =
# out_layer = 'point_XY'
# lyr = arcpy.MakeXYEventLayer_management('Outpoint.txt', 'POINT_X', 'POINT_Y', '')
