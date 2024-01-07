# encoding: utf-8
import arcpy

arcpy.env.workspace = ur'D:\1658386661779\QingzhouCity'
arcpy.env.overwriteOutput = True

out_feature = r'D:\1658386661779\savefile'

arcpy.Clip_analysis('铁路.shp', '钦南区.shp', out_feature)
