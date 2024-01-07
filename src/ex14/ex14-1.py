# coding=utf-8
import arcpy
import arcpy.mapping as map
import time

starttime = time.time()

arcpy.env.workspace = ur'D:\ExperimentData\1658386661779\QingzhouCity'

flds = arcpy.ListFields(r'兴趣点.shp')
for fid in flds:
    print(fid.name, fid.type, fid.length)

print("-------------------")

disc = arcpy.Describe(r'兴趣点.shp')
fldds = disc.fields
fld = fldds[0]
print(fld)

print("-------------------")

for fd in fldds:
    print(fd.name, fd.type, fd.length)

endtime = time.time()

print(endtime - starttime)