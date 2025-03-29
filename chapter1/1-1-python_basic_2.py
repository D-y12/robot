# 实验1-1： 开发环境与坐标变换基础
# 实验成员：052210424丁雨童
# 日期：2025.3.11
# 文件名：1-1-python_basic_2.py

#输入秒数转化成时分秒
seconds = int(input("请输入秒数："))
hours = seconds // 3600 #整除
seconds = seconds % 3600 #取余
minutes = seconds // 60 #整除
seconds = seconds % 60 #取余
print(f"{hours}时{minutes}分{seconds}秒") #f-string格式化输出 
