import arcpy.mapping as map

mymap = map.MapDocument("current")

adf = mymap.activeDataFrame


lyrs = map.ListLayers(mymap, "地名")


sym = lyrs.symbology
dir(sym)




