import arcpy
import arcpy.mapping as map
import math



degree = 120.3333
print(degree)
secs = degree * 3600

sec_parts = math.modf(secs)
sec_decimal = sec_parts[0]
sec_int = int(sec_parts[1])


print(sec_decimal, sec_int)


s = sec_int % 60
dm = sec_int // 60
m = dm % 60
print(dm, m, s)

