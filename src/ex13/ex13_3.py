# coding=utf-8
import arcpy
import arcpy.mapping as map
import math

dms = [120, 23, 40]

deg = dms[0] + dms[1] / 60.0 + dms[2] / 3600.0
print(deg)


def dms2deg(dms):
    deg = dms[0] + dms[1] / 60.0 + dms[2] / 3600.0
    return deg


outdeg = dms2deg(dms)
print(outdeg)
print("赵旸+2021b33040")

