import pandas as pd
import json
import requests
import os
import numpy as np

# Read single CSV file from the specified URL
#file_url = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_sales_analysis//data_source//sales_details_null_1.csv'
#df = pd.read_csv(file_url)



# Get a list of all files in the directory
directory_path = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//raw_data//'

file_names = os.listdir(directory_path)

df_sales_all = pd.DataFrame()
row = 0
for file_name in file_names:
    file_path = os.path.join(directory_path, file_name)
    # print(file_path)
    df = pd.read_csv(file_path)
    df = df[['market_place', 'contractAddress', 'tokenId',
                          'quantity', 'buyerAddress', "sellerAddress",
                          'blockNumber', 'sell_amount',
                          'sell_tokenAddress', 'sell_symbol',
                          'sell_decimals',
                          'sell_amount2']]
    #print(df.shape)
    row += df['market_place'].size
    df_sales_all = pd.concat((df_sales_all, df), axis=0)
    #print(df_sales_data.head())
    print(row)




file_name = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//meta_data//raw_sales_all.csv'
df_sales_all.to_csv(file_name, index = False)

print(row)