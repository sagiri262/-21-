# encoding: utf-8
import arcpy
import arcpy.mapping as map

outpath = r'D:\1658386661779\savemxd'
mxdpath = r'D:\1658386661779\Guangxi\广西市界.mxd'

print("赵旸+2021b33040")
mxd = map.MapDocument("current")
adf = mxd.activeDataFrame
lyr = arcpy.GetParameter(0)
outFolder = arcpy.GetParameterAsText(1)


def exportJpgByFID(fid):
    lyr.setSelectionSet('New',[fid])
    adf.zoomToSelectedFeatures()
    arcpy.RefreshActiveView()
    lyr.setSelectionSet('NEW',[])
    arcpy.RefreshActiveView()
    outJpg = r'{}\{}.jpg'.format(outpath,fid)
    map.ExportToJPEG(mxd, outJpg)

