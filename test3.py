import pandas as pd
import json
import requests
import os
import numpy as np

file_url = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//meta_data//add_timestamp_sales_all.csv'
df = pd.read_csv(file_url, encoding='utf-8', engine='python')

# max: 110400000.0
selected = df[df['sell_amount2']>80000000.0]
file_name = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//meta_data//top_amount_records.csv'
selected.to_csv(file_name)
