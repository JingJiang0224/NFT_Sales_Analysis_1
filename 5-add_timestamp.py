import pandas as pd

#### add column to salesdata
file_url = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//meta_data//update_sales_all.csv'
df = pd.read_csv(file_url, encoding='utf-8', engine='python')

file_url = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//meta_data//block_timestamp.csv'
df_timestamp = pd.read_csv(file_url)

merged = pd.merge(df, df_timestamp, how = 'left', left_on = 'blockNumber', right_on='blockNum')
res = merged[['market_place', 'contractAddress', 'tokenId',
                          'quantity', 'buyerAddress', "sellerAddress",
                          'blockNumber', 'sell_amount',
                          'sell_tokenAddress', 'sell_symbol',
                          'sell_decimals',
                          'sell_amount2', 'block_timestamp', 'date_only']]

file_name = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//meta_data//add_timestamp_sales_all.csv'
res.to_csv(file_name)