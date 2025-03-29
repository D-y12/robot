#2-4-SE3.py
# 实验成员：052210424丁雨童

from spatialmath import *
from spatialmath.base import *
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


#功能测试
T0 = SE3(np.identity(4)) # 由4阶单位矩阵构造一个单位齐次变换矩阵
T1 = SE3.Rx(30, 'deg') # 构造一个绕x轴旋转30°的齐次变换矩阵
T2 = SE3.Ry(0.1, 'rad') # 构造一个绕y轴旋转0.1弧度的齐次变换矩阵
T3 = SE3.Rz(45, 'deg') # 构造一个绕z轴旋转45°的齐次变换矩阵
T = T1 * T2 * T3 # 将多个齐次变换矩阵进行合成
T.print() # 两种打印输出的方式
print(T)
T_rpy =SE3(rpy2tr(30, 45, 60, unit="deg")) # 以RPY角的形式构造齐次变换矩阵
T_eul =SE3(eul2tr(60, 45, 30, unit="deg")) # 以欧拉角的形式构造齐次变换矩阵
T_pure_trans =SE3(transl(3, 0.0, 0.0)) # 构造纯平移运动的齐次变换矩阵
fig =plt.figure()
ax_3d =fig.add_subplot(projection='3d')
trplot( transl(0,0,0), frame='O', width=2, dims=[-5, 5, -5, 5,-5, 5], ax=ax_3d)
trplot( T_pure_trans.data, frame='A', width=2,color='red',ax=ax_3d)
trplot( (T_rpy*T_pure_trans).data, frame='B', width=2,color='blue',ax=ax_3d)
trplot( (T_pure_trans*T_rpy).data, frame='C', width=2,color='yellow',ax=ax_3d)
plt.show()

#分析齐次变换矩阵顺序和复合运动之间的关系
T_rpy =SE3(rpy2tr(30, 45, 60, unit="deg")) # 以RPY角的形式构造齐次变换矩阵
T_pure_trans =SE3(transl(3, 0.0, 0.0)) # 构造纯平移运动的齐次变换矩阵
#齐次变换矩阵是按照先旋转后移动的顺序
# 先旋转后平移
t1 = T_rpy * T_pure_trans
print("先旋转后平移:", t1)
# 先平移后旋转
t2 = T_pure_trans * T_rpy
print("先平移后旋转:", t2)
# 比较两种变换顺序的结果
print("两种变换顺序的结果是否相同:", np.allclose(t1, t2))



#使用现有工具函数，编写一个 Python 函数，构造出如图1.13所示两连杆极坐标机械臂的正运动学模型，即输入 θ 和 l，输出其末端位置和姿态。
#建立连杆坐标系，确定连杆参数
def two_link_rt(theta, l):
    # 构造第一个连杆的齐次变换矩阵。
    T1 = SE3.Rz(theta, 'deg') * SE3(transl(l, 0, 0))
    
    return T1

theta =int(input('输入转动关节转动角度'))  # 关节的角度
l = int(input('输入移动关节移动距离'))      # 第一个连杆的长度

end_pose = two_link_rt(theta, l)
print("末端位置和姿态:")
end_pose.print()