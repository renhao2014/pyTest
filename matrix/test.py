#http://www.runoob.com/numpy/numpy-tutorial.html
import numpy as np
a = np.array([[1,  2],  [3,  4]])
print (a)


x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ('我们的数组是：' )
print (x)
print ('\n')
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
y = x[[0,0],[3,3],[0,2],[0,2]]
print  ('这个数组的四个角元素是：')
print (y)




