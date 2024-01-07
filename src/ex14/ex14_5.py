# encoding: utf-8

import arcpy
import math

arcpy.ImportToolbox(r'C:\Users\THINK\AppData\Roaming\ESRI\Desktop10.8\ArcToolbox\My Toolboxes\工具箱.tbx')

d, m, s = arcpy.dms2(210.33333)

print(d, m, s)
print("2021b33040+赵旸")
