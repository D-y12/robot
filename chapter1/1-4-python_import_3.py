#1-4-python_import_3.py
#写一个 Python 函数，输入一个二维数组 (类型为 numpy.array)，输出其行列式大小。
import numpy as np

print("请输入输入二维数组的宽度或者高度：")
n=int(input())
i=1
list=[]
while i<=n*n:
    print("请输入第",i,"个数：")
    a=int(input())
    i=i+1
    list.append(a)
print("输入完毕")
list=np.array(list).reshape(n,n)
print("输入的二维数组是："+'\n',list)
print("输入的二维数组的行列式大小是：",np.linalg.det(list))

