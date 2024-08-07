import pandas as pd
import json
import requests
import os
import numpy as np

file_url = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//meta_data//add_timestamp_sales_all.csv'
df = pd.read_csv(file_url, encoding='utf-8', engine='python')

print(max(df['quantity']), df['quantity'].max())
# 9900000000000000 9900000000000000