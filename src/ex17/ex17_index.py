# encoding: utf-8
import arcpy
import arcpy.mapping as map

arcpy.env.workspace = r'D:\1658386661779\QingzhouCity'


arcpy.AddField_management('区界.shp',
                          'AREA',
                          'DOUBLE')
arcpy.AddField_management('区界.shp',
                          'LENGTH',
                          'DOUBLE')

# 周长表达式
arcpy.CalculateField_management('区界.shp', 'AREA',
                                '!shape.geodesicArea@SQUAREMETERS!', 'PYTHON_9.3')
arcpy.CalculateField_management('区界.shp', 'LENGTH',
                                '!shape.geodesicLength@METERS!', 'PYTHON_9.3')

# 加入LSI用以存放景观指数
arcpy.AddField_management('区界.shp',
                          'LSI',
                          'DOUBLE')
print("赵旸+2021b33040")
# 计算景观指数
arcpy.CalculateField_management('区界.shp',
                                'LSI',
                                '0.25 * !LENGTH! / (!AREA!) ** 0.5',
                                'PYTHON_9.3')



