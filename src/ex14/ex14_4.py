import arcpy
import math
print("zhaoyang+2021b33040")


def deg2dms(deg):
    secs = deg * 3600
    secs_parts = math.modf(secs)
    secs_decimal = secs_parts[0]
    secs_int = int(secs_parts[1])
    s = secs_int % 60
    dm = secs_int % 60
    m = dm % 60
    return s, dm, m

print("zhaoyang+2021b33040")
input_degree = arcpy.GetParameterAsText(0)

print("zhaoyang+2021b33040")
deg = float(input_degree)
dms = deg2dms(deg)

arcpy.SetParameter(input_degree, deg, dms)
arcpy.AddMessage("{0}complete!".format(dms))
print("zhaoyang+2021b33040")