# encoding: utf-8
import arcpy

# 2021b33040 赵旸
# 设置工作空间
arcpy.env.workspace = r'D:\1658386661779\QingzhouCity'

desc = arcpy.Describe('区界.shp')

wkid = 4524
sr = arcpy.SpatialReference(wkid)

print(sr.name)

# sf = desc.spatialReference
# print(sf.name)

# feature_classes = arcpy.ListFeatureClasses()
# for fc in feature_classes:
#    descs = arcpy.Describe(fc)
#    sr_1 = descs.spatialReference
#    print(sr_1.name)
#    print("2021b33040 赵旸")