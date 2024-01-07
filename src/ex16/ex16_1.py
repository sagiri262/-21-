# encoding: utf-8
import arcpy
print("2021b33040+zhaoyang")
arcpy.env.workspace = ur'D:\1658386661779\QingzhouCity'
arcpy.ImportToolbox(r'')

print("2021b33040+zhaoyang")
arcpy.AddField_management('区界.shp', 'AREA', 'DOUBLE')
arcpy.CalculateField_management('District_leTEST.shp', '')
arcpy.AddField_management('District_leTEST.shp', 'LENGTH', 'DOUBLE')
arcpy.CalculateField_management('District_leTEST.shp', 'LENGTH', '!shape.geodesicArea@SQUAREMETERS!')

