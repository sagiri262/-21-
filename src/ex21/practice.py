# encoding: utf-8
import os.path
import arcpy
import time

outtemp = r'D:\ExperimentData\pythonProject\temps'

arcpy.env.workspace = r'D:\ExperimentData\pythonProject\9qinfu'

fs = arcpy.ListFeatureClasses()
for i in fs:
    starttime = time.time()
    # out_flie = os.path.join(outtemp, f)
    print(i)
    endtime = time.time()
    times = endtime - starttime
    print(times)