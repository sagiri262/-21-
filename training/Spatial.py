# encoding: utf-8
"""
@第一题
@Author:ZhaoYang
@StuID
"""

import arcpy

inputfile = r'D:\ExperimentData\GIS应用开发\实训\示例数据\批处理\点矢量数据文件\YSGD_H51G039003_4.shp'
outfile = r'D:\ExperimentData\GIS应用开发\实训\示例数据\输出\YSGD_H51G039003_4_wgs_1984.shp'

wkid = 4326
out_coor_system = arcpy.SpatialReference(wkid)

arcpy.Project_management(inputfile, outfile, out_coor_system)