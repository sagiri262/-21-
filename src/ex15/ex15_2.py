import arcpy

arcpy.env.workspace = ur'D:\ExperimentData\1658386661779\QingzhouCity'

arcpy.AddField_management('BeibuGulfUniversity.shp', 'AREA_HA', 'DOUBLE')
arcpy.CalculateField_management('BeibuGulfUniversity.shp', 'AREA_HA', '!AREA!/10000', 'Python_9.3')



