import keyword
from sys import argv, path  # 导入特定的成员
import funTest

#关键词列表
print(keyword.kwlist)
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path
print("test---")


#基本数据类型
a=1
b='str'
c=2.3
d=4+3j


#判断
if a==1:
    b='string';
elif a==2:
    b='str2'
else:
    b='str3'


#循环
for var in  b:
    print(var,end=" ")

q = 1
while q < 2:
    print(q)
    q=q+1;

for i in range(0, 10, 3) :
    print(i)


#释放
del a,b,c,d;


#数组
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表

#元组 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2)

#集合
set1 = {1,2,4}
set2=set()

#字典
#列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

#运算符 http://www.runoob.com/python3/python3-basic-operators.html
#数据结构 http://www.runoob.com/python3/python3-data-structure.html


#测试自定义函数
areaValue=funTest.area(200,30)
print("面积=",areaValue)
funTest.area(width=200,height=30)

funTest.printinfo1(70, 60, 50 )
funTest.printinfo(1, a=2,b=3)


#lambda
sum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
print("相加后的值为 : ", sum(10, 20))


#作用域
x = int(2.9)  # 内建作用域
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域
















