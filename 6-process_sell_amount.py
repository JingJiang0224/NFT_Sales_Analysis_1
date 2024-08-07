import pandas as pd

#### change all the records whose sell_amount2 is less than 0.0006

file_url = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//meta_data//add_timestamp_sales_all.csv'
df = pd.read_csv(file_url, low_memory=False)

#print(min(df['sell_amount2']), max(df['sell_amount2']))
# max 14720000


#  1 USD = 0.0006 ETH, 1 ETH = 1657USD
def func(data):
    if data < 0.0001:
        data = 0
    return data

df['sell_amount2'] = df['sell_amount2'].apply(func)
#df['sell_amount2'] = df['sell_amount2'].round(4)
file_name = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//meta_data//process_amount2_sales_all.csv'
df.to_csv(file_name, index = False)