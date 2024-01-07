import arcpy.mapping as map

mymap = map.MapDocument("current")
lyres = map.ListLayers(mymap, "兴趣点")
lyr = lyres[0]

lyr.symbologyType
lyr.symbology