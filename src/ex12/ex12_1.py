# coding=utf-8

import arcpy
import arcpy.mapping as map

mxdpath = r'D:\1658386661779\Guangxi\广西市界.mxd'
mxd = map.MapDocument(mxdpath)
adf = mxd.activeDataFrame
outFolder = r'D:\1658386661779\savemxd'

lyrs = map.ListLayers(mxd)
lyr = lyrs[0]


def expoertJpgByLayers(fid):
    lyr.setSectionSet("NEW", [fid])
    adf.zoomToSelectedFeatures()
    lyr.setSectionSet("NEW", [])
    arcpy.RefreshActiveView()
    outfile = r''
