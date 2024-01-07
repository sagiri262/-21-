# coding=utf-8
import arcpy
from arcpy.sa import *
from arcpy import env
import numpy as np

env.workspace = "D:\ExperimentData\GIS应用大赛历年试题\10第十届全国大学生GIS应用技能大赛\下午数据"
arcpy.CheckOutExtension("Spatial")

env.cellSizeProjectionMethod = "CONVERT_UNITS"
env.cellSize = "DTM.tif"
env.mask = "Building.shp"

# 输入DTM数据
inRaster = r""
latitude = 41.77686382537
sksize = 200
timeCOnfig = [TimeMultipleDays(2021,1,31),
              TimeMultipleDays(2021,32,59),
              TimeMultipleDays(2021,60,90),
              TimeMultipleDays(2021,91,120),
              TimeMultipleDays(2021,121,151),
              TimeMultipleDays(2021,152,181),
              TimeMultipleDays(2021,182,212),
              TimeMultipleDays(2021,213,243),
              TimeMultipleDays(2021,244,273),
              TimeMultipleDays(2021,274,304),
              TimeMultipleDays(2021,305,334),
              TimeMultipleDays(2021,335,365)]

dayInterval = 14
hourInterval = 0.5
zFactor = 1







