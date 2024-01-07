# encoding: utf-8

import arcpy
import time

start_time = time.time()
arcpy.env.workspace = ur'D:\ExperimentData\pythonProject\1658386661779\QingzhouCity'

decs = arcpy.Describe("区界.shp")
spatialrefer = decs.spatialReference

print(spatialrefer.name)

end_time = time.time()
times = end_time - start_time
print(times)