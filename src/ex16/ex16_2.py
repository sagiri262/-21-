# encoding: utf-8
import arcpy
print("2021b33040+zhaoyang")
arcpy.env.workspace = ur'D:\1658386661779\QingzhouCity'


arcpy.AddField_management('区界.shp',
                          'AREA_MU',
                          'DOUBLE')

# 计算亩
print("赵旸+2021b33040")
arcpy.CalculateField_management('区界.shp',
                                'AREA_MU',
                                '!Shape_Area!/10000/15',
                                'PYTHON_9.3')

print("DONE")


