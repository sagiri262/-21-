# coding: utf-8
import numpy as np
#计算绝对值
a = np.abs(-10)
print(a)
print("赵旸+2021b33040")

print("-------------")

a1 = 10
b1 = 10.5
c1 = "我是赵旸，学号2021b33040"

print(type(a1))
print(type(b1))
print(type(c1))
print("赵旸+2021b33040")

print("-------------")

a2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in a2:
    if i < 5:
        print(0)
    else:
        print(1)


print(a2[4])
print(len(a2))
print("赵旸+2021b33040")

print("-------------")

bj = {}
bj["coord"] = {"lon":116.37, "lat":39.93}
bj["pop"] = 21707000
print(bj)

sh = {}
sh["coord"] = {"lon":121.53, "lat":31.26}
sh["pop"] = 24183300
print(sh)
print("赵旸+2021b33040")

print("-------------")

sum = 0
for i in range(1, 101):
    sum += i
print(sum)
print("赵旸+2021b33040")

print("-------------")

pwd = 123
invalid = True

while invalid:
    input_value = input("输入密码：")
    if(input_value != pwd):
        print("密码错误!")
    else:
        print("登录成功！")
        invalid = False
