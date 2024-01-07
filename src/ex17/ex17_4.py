# encoding: utf-8
import arcpy
print("赵旸+2021b33040")
arcpy.ImportToolbox(r'D:\1658386661779\toolbox\Toolsin.tbx')


arcpy.AddField_management('兴趣点.shp', 'd_lon', 'DOUBLE')
arcpy.AddField_management('兴趣点.shp', 'm_lon', 'DOUBLE')
arcpy.AddField_management('兴趣点.shp', 's_lon', 'DOUBLE')

express = "arcpy.Degree2DMS(!POINT_X!)[0]"
arcpy.CalculateField_management('兴趣点.shp', 'd_lat', express, 'PYTHON_9.3')
express = "arcpy.Degree2DMS(!POINT_X!)[1]"
arcpy.CalculateField_management('兴趣点.shp', 'm_lat', express, 'PYTHON_9.3')
express = "arcpy.Degree2DMS(!POINT_X!)[2]"
arcpy.CalculateField_management('兴趣点.shp', 's_lat', express, 'PYTHON_9.3')


arcpy.AddField_management('兴趣点.shp', 'd_lon', 'DOUBLE')
arcpy.AddField_management('兴趣点.shp', 'm_lon', 'DOUBLE')
arcpy.AddField_management('兴趣点.shp', 's_lon', 'DOUBLE')




print("TRUE!")



