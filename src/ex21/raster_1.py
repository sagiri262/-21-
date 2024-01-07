# encoding: utf-8
import arcpy

arcpy.env.workspace = ur'D:\1658386661779\raster-lx'

extracted = arcpy.sa.ExtractByMask("qinzhou_up.tif","钦南区.shp")
extracted.save(r'D:\1658386661779\raster-lx\qinnan_up_clip.tif')

'''
raster = arcpy.ListRasters()
for r in raster:
    print(r)

raster_filepath = r'D:\ExperimentData\pythonProject\9qinfu'
'''

arcpy.env


def Raster_clip(raster_file, shape_file):
    extraction = arcpy.sa.ExtractByMask(raster_file, shape_file)
    extraction.save()


