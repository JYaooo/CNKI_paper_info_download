# -*- coding: utf-8 -*-
# @Time : 2023/8/19 20:46 
# @Author : Yao
# @File : combined_excel.py

import os
import pandas as pd

# 指定文件夹路径
folder_path = '/知网_文献信息获取/data/2019'  #'/path/to/your/folder'

# 获取文件夹下所有的 xls 文件路径
xls_files = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith('.xlsx')]

# 创建一个空的 DataFrame 用于存储所有数据
all_data = pd.DataFrame()

# 遍历每个 xls 文件，读取数据并拼接到 all_data 中
for xls_file in xls_files:
    data = pd.read_excel(xls_file)
    all_data = pd.concat([all_data, data], ignore_index=True)

# 去除重复的行
all_data = all_data.drop_duplicates()

# 输出拼接后的数据到一个新的 xls or csv 文件
# all_data.to_csv('combined_data.csv', index=False)
all_data.to_excel('2019_combined_data.xlsx', index=False)

print("拼接完成，输出文件")
