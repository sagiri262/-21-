# coding=utf-8
import arcpy

arcpy.env.workspace = ur'D:\1658386661779\QingzhouCity'

fec = arcpy.ListFeatureClasses()
for fc in fec:
    print (fc)

print("zhaoyang+2021b33040")
flds = arcpy.ListFields(r'兴趣点.shp')
print("zhaoyang+2021b33040")
fld = flds[0]
print(fld.name, fld.type, fld.length)


for i in flds:
    print(i.name, i.type, i.length)

desc = arcpy.Describe(r'兴趣点.shp')
fld_s = desc.fields

print("zhaoyang+2021b33040")
fld1 = fld_s[0]

print(fld1.name, fld1.type, fld1.length)


for fld2 in fld_s:
    print(fld2.name, fld2.type, fld2.length)