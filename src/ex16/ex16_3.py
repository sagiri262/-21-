# encoding: utf-8
import arcpy


print("2021b33040+zhaoyang")
arcpy.env.workspace = ur'D:\1658386661779\QingzhouCity'

print("赵旸+2021b33040")
arcpy.AddField_management('区界.shp',
                          'FULLNAME',
                          'TEXT')

print("赵旸+2021b33040")
arcpy.CalculateField_management('区界.shp',
                                'FULLNAME',
                                'u"{}{}".format(!City!, !NAME99!)',
                                'PYTHON_9.3')

# 字段拆分
# 取前三个字符表达式
print("赵旸+2021b33040")
arcpy.AddField_management('区界.shp',
                          'FE',
                          'TEXT')
arcpy.CalculateField_management('区界.shp',
                                'FE',
                                '!NAME99![:3]',
                                'PYTHON_9.3')

# 取前四个字符到末尾表达式
print("赵旸+2021b33040")
arcpy.AddField_management('区界.shp',
                          'FP',
                          'TEXT')
arcpy.CalculateField_management('区界.shp',
                                'FP',
                                '!NAME99![3:]',
                                'PYTHON_9.3')


print("DONE")