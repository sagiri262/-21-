import math
import arcpy


def dms2deg(dms):
    deg = dms[0] + dms[1] / 60.0 + dms[2] / 3600.0
    return deg


input_deg = arcpy.GetParameterAsText(0)
input_min = arcpy.GetParameterAsText(1)
input_sec = arcpy.GetParameterAsText(2)


input_dms = [input_deg, input_min, input_sec]
outputdms = dms2deg(input_dms)
print("zhaoyang + 2021b33040")

arcpy.SetParameter(3, outputdms)
arcpy.AddMessage()
