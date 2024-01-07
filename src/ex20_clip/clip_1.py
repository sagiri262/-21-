# encoding: utf-8
import arcpy
import os

# 2021b33040
arcpy.env.overwriteOutput = True
out_temp = r"D:\ExperimentData\pythonProject\9qinfu"

# 获取道路要素
in_feature = arcpy.GetParameterAsText(0)
# 获取土地利用要素
in_landcover = arcpy.GetParameterAsText(1)
# 输出的统计结果路径
out_static = arcpy.GetParameterAsText(2)

os.path.join(out_temp, roadbuffer)
arcpy.Buffer_analysis(in_feature, roadbuffer, 50)
# 2021b33040
arcpy.Clip_analysis(in_feature, in_landcover, out_clip)
# 2021b33040
arcpy.Statistics_analysis(out_clip, out_static, [["Shape_Area", "SUM"]], "TBLXMC")
'''
out_clip：包含用于计算统计数据的字段的输入表。
out_static：将存储计算的统计数据的输出 dBASE 或地理数据库表。
[["Shape_Area", "SUM"]]：指定包含用于计算指定统计数据的属性值的数值字段。
                        可以指定多项统计数据和字段组合。
                        空值将被排除在所有统计计算之外。
                        可使用第一种和最后一种统计来对文本属性字段进行汇总。
                        可使用任何一种统计来对数值属性字段进行汇总。
"TBLXMC"：“输入”中用于为每个唯一属性值（如果指定多个字段，则为属性值组合）单独计算统计数据的一个或多个字段。

摘自ArcPy的官方文档，Link:https://desktop.arcgis.com/zh-cn/arcmap/latest/tools/analysis-toolbox/summary-statistics.htm
'''


