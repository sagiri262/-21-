# encoding: utf-8
"""
@author:ZhaoYang
@StuID:2021b33040
@Date:2023/1/4
@workTitle: 三角面积水图层转格网积水图层程序
"""
import arcpy
from arcpy import env
import os.path
from arcpy.sa import *

# 设置工作空间
arcpy.env.workspace = r'D:\ExperimentData\GIS应用开发\实训\示例数据\积水'
# 设置可复写文件
# 设置为True表示可以被覆写
arcpy.env.overwriteOutput = True

# 设置临时工作空间
arcpy.env.scratchWorkspace = r''

feature_Classes = arcpy.ListFeatureClasses()

for fc in feature_Classes:
    print(fc)
# 检查工作空间文件夹内的数据


# wkid = 4549 表示 CGCS2000_3_Degree_GK_CM_120E
wkid_cgs_2000 = 4549
wkid_wgs_1984 = 4326
feature_Class = feature_Classes.split(";")

for feature in feature_Classes:
    out_coor_system = arcpy.SpatialReference(wkid_cgs_2000)
    # 要素类转栅格，栅格的value为要素类中的SPEED2D
    OutRaster = arcpy.PolygonToRaster_conversion(feature, SPEED2D, )
    Raster_temp = OutRaster * 10000000
    Raster_Int = Int(Raster_temp)
    # 输入上面转为整形的栅格数据，输出要素类数据
    Raster2feature = arcpy.RasterToPolygon_conversion(Raster_Int, # )
    arcpy.AddField_management(Raster2feature, newgrid)
    arcpy.CalculateField_management(Raster2feature, newgrid, gridcode / 10000000, )




# 矢量转栅格
'''
PolygonToRaster_conversion(
输入要素：in_features, 
以哪个字段为转栅格的像元值value_field, 
输出栅格out_rasterdataset,
暂时不需要管这些参数：{cell_assignment}, {priority_field}, {cellsize})
'''
arcpy.PolygonToRaster_conversion()
'''
RasterToPolygon_conversion(
输入栅格数据：in_raster, 
输出要素类：out_polygon_features, 
以下参数均为默认：{simplify}, {raster_field}, {create_multipart_features}, {max_vertices_per_feature})
'''
