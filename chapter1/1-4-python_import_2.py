#1-4-python_import_2.py
#写一个 Python 程序，绘制出至少一个周期的包含三角函数的任意函数。
import numpy as np
import matplotlib.pyplot as plt

pi=np.pi
x=np.arange(0,4*pi,pi/360)  #x轴的取值范围是0到4pi，步长是pi/360
y=np.sin(x) #y轴的取值是x的sin
plt.plot(x,y)
plt.show()

