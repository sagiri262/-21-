# encoding:utf-8
import os.path
import arcpy

# 2021b33040 赵旸
arcpy.env.workspace = ur'D:\1658386661779\savefile'

# 设置可覆盖输出
arcpy.env.overwriteOutput = True

out_temp = r'D:\1658386661779\savefile'

# 引入参数
in_features = arcpy.GetParameterAsText(0)
clip_features = arcpy.GetParameterAsText(1)
out_features = arcpy.GetParameterAsText(2)

'''
第一个为要截的要素集集合（多个）
第二个为截取范围要素集、
第三个为输出路径
'''

# 用split把多个要素集分开成数组
features = in_features.split(";")
# 用os.path.join设置一个缓冲区输出文件路径
out_f = os.path.join(out_temp, features + "_clip")

