# coding=utf-8
import arcpy
import arcpy.mapping as map

mymap = map.MapDocument("current")
adf = mymap.activateDataFrame

lyrs = map.ListLayers(mymap)
lyr = lyrs[0]

# exportJpgby

# lyr.setSelection
# arcpy.RefreshActiveView()
# adf.zoomToLayer


def ExportJpgbyId(fid):
    lyr.setSelectionSet("NEW",[fid])
    arcpy.RefreshActiveView()
    adf.zoomToSelectedFeatures()
    lyr.setSelectionSet("NEW",[])
    arcpy.RefreshActiveView()
    output = r" //Route "
    map.ExportToJPEG(mymap,output)


ExportJpgbyId(1)
arcpy.GetCount_management("//文件名")

count = arcpy.GetCount_management(lyr)
n = int(count.getOutput(0))

print('-------------------------------')
print(n)
print('-------------------------------')

for i in range(n):
    ExportJpgbyId(i)


def ExportJpgbyLayer(inputlyr, fid):
    inputlyr.setSelectionSet("NEW",[fid])
    arcpy.RefreshActiveView()
    adf.zoomToSelectedFeatures()
    inputlyr.setSelectionSet("NEW",[])
    arcpy.RefreshActiveView()
    output = r" //Route "
    map.ExportToJPEG(mymap,output)


def ExportJPGbyLayer(path, inputlyr, fid):
    inputlyr.setSelectionSet("NEW",[fid])
    arcpy.RefreshActiveView()
    adf.zoomToSelectedFeatures()
    inputlyr.setSelectionSet("NEW",[])
    arcpy.RefreshActiveView()
    # 灵活匹配输出路径
    output = path + r"\{}.jpg".format(fid)
    map.ExportToJPEG(mymap,output)