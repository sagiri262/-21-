# encoding: utf-8
import arcpy
import arcpy.mapping as map

outpath = r'D:\1658386661779\savemxd'

mxd = map.MapDocument("current")
adf = mxd.activeDataFrame
lyrs = map.ListLayers(mxd)
lyr = lyrs[0]


def exportJpgByFID(fid):
    lyr.setSelectionSet('New',[fid])
    adf.zoomToSelectedFeatures()
    arcpy.RefreshActiveView()
    lyr.setSelectionSet('NEW',[])
    arcpy.RefreshActiveView()
    outJpg = r'{}\{}.jpg'.format(outpath,fid)
    map.ExportToJPEG(mxd, outJpg)


result = arcpy.GetCount_management(lyr)
count = int(result.getOutput(0))

for i in range(count):
    exportJpgByFID(i)