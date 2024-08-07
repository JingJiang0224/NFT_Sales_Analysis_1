import pandas as pd
import json
import requests
import os
import numpy as np

### change certain columns into string  ################
### PowerBI problem

def convertform(data):
    return '"' + str(data) + '"'

file_url = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//meta_data//raw_sales_all.csv'
df_sales_all = pd.read_csv(file_url, low_memory=False)
#print(df_sales_all.head())

tokenId = df_sales_all['tokenId']
contractAddress = df_sales_all['contractAddress']
buyerAddress = df_sales_all['buyerAddress']
sellerAddress = df_sales_all['sellerAddress']
sell_tokenAddress = df_sales_all['sell_tokenAddress']

df_sales_all['tokenId'] = tokenId.apply(convertform)
df_sales_all['contractAddress'] = contractAddress.apply(convertform)
df_sales_all['buyerAddress'] = buyerAddress.apply(convertform)
df_sales_all['sellerAddress'] = sellerAddress.apply(convertform)
df_sales_all['sell_tokenAddress'] = sell_tokenAddress.apply(convertform)


#print(df_sales_all['sell_tokenAddress'])

file_name = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//meta_data//update_sales_all.csv'
df_sales_all.to_csv(file_name, index = False)