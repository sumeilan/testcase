import pandas as pd
import os

def merge_sheets():
    # root = os.getcwd() #获取当前路径
    root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  # 获取当前的上一级路径
    path = root + '\data\case1.xlsx'
    new_path = root + '\data\case2.xlsx'
    iris = pd.read_excel(path, None)  # 读入数据文件
    keys = list(iris.keys())
    # 第三步：数据合并
    iris_concat = pd.DataFrame()
    for i in keys:
        iris1 = iris[i]
        iris_concat = pd.concat([iris_concat, iris1])

    iris_concat.to_excel(new_path, index=False)  # 数据保存路径
