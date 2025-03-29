#1-4-python_import_1.py
#写一个 Python 函数，输入 (x1, y1) 和 (x2, y2) 两点，输出两点之间的距离
import math
def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

if __name__ == '__main__':
    x1=float(input("请输入第一个点的 x1 坐标："))
    y1=float(input("请输入第一个点的 y1 坐标："))
    x2=float(input("请输入第二个点的 x2 坐标："))
    y2=float(input("请输入第二个点的 y2 坐标："))
    print(f"两点之间的距离是{distance(x1,y1,x2,y2)}")





