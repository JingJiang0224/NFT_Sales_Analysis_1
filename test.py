import pandas as pd
import json
import requests
import os
import numpy as np


# def convertform(data):
# #     return '"' + str(data) + '"'
# #
# # file_url = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//analyze_data//df_blockNumber.csv'
# #
# #
# # df = pd.read_csv(file_url)
# # print(df.min(), df.max())

# print(df.dtypes)

#file_url = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//meta_data//raw_sales_all.csv'
#df = pd.read_csv(file_url, low_memory=False)

#print(min(df.quantity), max(df.quantity))

# def func(data):
#     if data < 0.00006:
#         data = 0.00006
#     return data
#
#
# file_url = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//meta_data//add_timestamp_sales_all.csv'
# df = pd.read_csv(file_url, low_memory=False)
# print(min(df.sell_amount2), max(df.sell_amount2))
# print(df['sell_amount2'].iloc[135:160])
#df['sell_amount2'] = df['sell_amount2'].apply(func)
#print(min(df.sell_amount2), max(df.sell_amount2))

# a=[]
# def func(data):
#     a.append(int(data))
#     #print (str(data)+","+(type(data).__name__))
#
# file_url = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//meta_data//update_sales_all.csv'
#
# df = pd.read_csv(file_url, encoding='utf-8', engine='python')
# df['quantity'].apply(func)
# print(max(a))
# print(df['quantity'].min())


# f = open(file_url, "r")
# for row in f:
#     print(row)
#     break



# len1 = df['quantity'].size
# # 1887826
# lst = []
# for i in range(len1):
#    df['quantity'] = int(df['quantity'][i])

# #print(i)
# print(type(df['quantity'][1]), type(df['sell_amount2'][1]))
# print(df['quantity'][1] == 1)

# # <class 'str'> <class 'numpy.float64'>
#
# df['quantity'] = df['quantity'].astype(int)
#file_name = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//meta_data//process_amount2_sales_all2.csv'
#df.to_csv(file_name)