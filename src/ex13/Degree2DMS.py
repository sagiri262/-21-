import arcpy
import arcpy.mapping as map
import math

rad = arcpy.GetParameterAsText(0)
deg = math.degrees(rad)
arcpy.AddMessage(str(deg))
arcpy.SetParameter(1, deg)


