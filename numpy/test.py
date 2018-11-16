import numpy as np

arr=np.array([1,2,3],ndmin=3)
print(str(arr))

print("扩展：")
a=1
b=np.tile(1,(2,4,8))
print(b)
print(b.shape)#返回一个元组

print("重组：")
c=np.arange(0,24,2)
c=c.reshape(2,6)
print(c)

print("矩阵乘法：")
c=c*2
print(c)

print("矩阵减法：")
d=np.ones([2,6])
e=c-d
print(e)

print("矩阵转置：")
print(e.T)

print("排序：")
f=np.array([4,5,8,1,3,9,3,0])
f=f.reshape(2,4)
g=np.sort(f)
print(g)

