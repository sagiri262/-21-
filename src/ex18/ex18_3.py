# encoding: utf-8
import arcpy

# 2021b33040 赵旸
# 设置工作空间
arcpy.env.workspace = r'D:\1658386661779\QingzhouCity'
# arcpy.CopyRows_management('兴趣点.shp', r'D:\1658386661779\savefile\outPutPoints.txt')
arcpy.CopyRows_management('兴趣点.shp', r'D:\1658386661779\savefile\outPutPoints.xls')