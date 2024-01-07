# encoding: utf-8
"""
@Author:ZhaoYang
@StuID:2021b33040
@Title:外部目录投影转换批处理程序
"""

import arcpy
from arcpy import env
import os

"""
思路：设定工作空间，获取目录下所有矢量要素文件，通过循环遍历，设置输出路径，进行批量处理
使用的方法提示：
1、设定工作空间的属性
arcpy.env.workspace
2、获取目录下所有要素文件方法
arcpy.ListFeatureClasses()
3、遍历中用到的方法
arcpy.Project_management
"""



