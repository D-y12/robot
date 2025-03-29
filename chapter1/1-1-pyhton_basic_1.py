# 实验1-1： 开发环境与坐标变换基础
# 实验成员：052210424丁雨童
# 日期：2025.3.11
# 文件名：1-1-python_basic_1.py


print('Welcome to Robotics Simulation World!') # 打印功能，括号中内容会从终端界面显示出

# 加减乘除及幂运算，2**3表示2的3次方，//表示整除，%表示取余
num =1*4 -2**3 +10/3 +10//3 +10%3
print(num)

flag =False # Bool（布尔）类型的变量定义与赋值，True或False，注意大小写
name ='user003' # String（字符串）类型的变量定义与赋值，单引号‘’中为字符串内容
if name =='user001':
# if 条件语句的写法，将name变量与字符串'user001'进行比较，
# 注意以冒号结尾，做判断时等于符号用'=='
    flag =True
    print('Welcome to user001\'s workspace!') # 字符串''中若要包含'，则需加上\，即\'
elif name =='user002':
    flag =True
    print('Welcome to {}\'s workspace!'.format(name)) # 将name值替代{}
elif name =='user003':
    flag =True
    print('Welcome to ' +name +'\'s workspace!') # 直接使用'+'连接三个字符串
else:
    print(name)
if not flag: # 等同于 if flag == False:
    print('no valid user!')

# 列表定义与操作
# 列表是一种有序的集合，可以随时添加和删除其中的元素，列表中的元素可以是不同的数据类型  
list1 =[1, 2, 3, 4, 5] # 定义一个列表
print(list1) # 打印输出列表，输出为：[1, 2, 3, 4, 5]
list1.append(6) # 在列表末尾添加一个元素6
print(list1) # 打印输出列表，输出为：[1, 2, 3, 4, 5, 6]
list1.remove(3) # 删除列表中的元素3
print(list1) # 打印输出列表，输出为：[1, 2, 4, 5, 6]




