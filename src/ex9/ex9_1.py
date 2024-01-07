import arcpy
import arcpy.mapping as map

# file position
arcpy.env.workspace = r"D:/"

layer = map.Layer("")
mymap = map.MapDocument("current")
adf = mymap.activeDataFrame
map.AddLayer(adf, layer)

# change layer name
lyr = layer[0]



