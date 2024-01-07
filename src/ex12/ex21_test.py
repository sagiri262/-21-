# coding utf=8
import arcpy
import arcpy.mapping as map

mymap = map.MapDocument(r"D:\data\  ")
adf = mymap.activateDataFrame



mxd = map.MapDocument()

dfjpg = r"D:\temp\pics.jpg"
outfolder = r""

map.ExportToJPEG(mymap, dfjpg, adf)

dfpdf = r"D:\temp\picss.pdf"
map.ExportToPDF(mymap, dfjpg, adf)

lyrs = map.ListLayers(mxd)
lyr = lyrs[0]

def exportJpgByFid(fid):
    lyr.setSelectionSet("NEW", [fid])
    adf.zoomToSelectedFeatures()
    arcpy.RefreshActiveView()
    lyr.setSelectionSet("NEW",[])
    arcpy.RefreshActiveView()
    outJpgs = r'.jpg'.format(outfolder, fid)
    map.ExportToJPEG(mxd, outJpgs)

result = arcpy.GetCount_management(lyr)
count = int(result.getOutput(0))

for fid in range(count):
    exportJpgByFid(fid)

print("DONE")
