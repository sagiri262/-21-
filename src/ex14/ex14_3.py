# coding = utf-8

import arcpy
import math


def deg2dms(deg):
    secs = deg * 3600
    secs_parts = math.modf(secs)
    secs_decimal = secs_parts[0]
    secs_int = int(secs_parts[1])
    s = secs_int % 60
    dm = secs_int % 60
    m = dm % 60
    return s, dm, m

