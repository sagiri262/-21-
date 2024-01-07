# coding=utf-8
import arcpy

print("zhaoyang+2021b33040")
arcpy.env.workspace = ur'D:\1658386661779\QingzhouCity'

fec = arcpy.ListFeatureClasses()
for fc in fec:
    print (fc)

desc = arcpy.Describe(r'区界.shp')
fids = desc.fields
fid = fids[0]
print(fid.name, fid.length, fid.type)

arcpy.AddField_management('path', 'area_ha','DOUBLE')
arcpy.CalculateField_management('path', 'area_ha', '!AREA!/10000', 'PYTHON_9.3')

arcpy.AddField_management('District_')



