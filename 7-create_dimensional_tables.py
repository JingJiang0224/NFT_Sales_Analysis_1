import pandas as pd

file_url = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//meta_data//process_amount2_sales_all.csv'
df = pd.read_csv(file_url, low_memory=False)
#print(df.head())

print(df['market_place'].size)
# 854654


# df = df[['market_place', 'contractAddress', 'tokenId',
#          'quantity', 'buyerAddress', "sellerAddress",
#          'blockNumber', 'sell_amount',
#          'sell_tokenAddress', 'sell_symbol',
#          'sell_decimals',
#          'sell_amount2', 'block_timestamp', 'date_only']]

### generate dimensional tables
df_market_place = pd.DataFrame(df['market_place'].drop_duplicates(ignore_index = True))
df_contractAddress = pd.DataFrame(df['contractAddress'].drop_duplicates(ignore_index = True))
df_tokenId = pd.DataFrame(df['tokenId'].drop_duplicates(ignore_index = True))
df_buyerAddress = pd.DataFrame(df['buyerAddress'].drop_duplicates(ignore_index = True))
df_sellerAddress = pd.DataFrame(df['sellerAddress'].drop_duplicates(ignore_index = True))
df_blockNumber = pd.DataFrame(df['blockNumber'].drop_duplicates(ignore_index = True))
df_sell_symbol = pd.DataFrame(df['sell_symbol'].drop_duplicates(ignore_index = True))
df_sell_decimals = pd.DataFrame(df['sell_decimals'].drop_duplicates(ignore_index = True))
df_sell_tokenAddress = pd.DataFrame(df['sell_tokenAddress'].drop_duplicates(ignore_index = True))
#df_block_timestamp = pd.DataFrame(df['block_timestamp'].drop_duplicates(ignore_index = True))
df_block_date = pd.DataFrame(df['date_only'].drop_duplicates(ignore_index = True))



path = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//analyze_data//'
df_market_place.to_csv(path + 'df_market_place.csv')
df_contractAddress.to_csv(path + 'df_contractAddress.csv')
df_tokenId.to_csv(path + 'df_tokenId.csv')
df_buyerAddress.to_csv(path + 'df_buyerAddress.csv')
df_sellerAddress.to_csv(path + 'df_sellerAddress.csv')
df_blockNumber.to_csv(path + 'df_blockNumber.csv')
df_sell_symbol.to_csv(path + 'df_sell_symbol.csv')
df_sell_decimals.to_csv(path + 'df_sell_decimals.csv')
df_sell_tokenAddress.to_csv(path + 'df_sell_tokenAddress.csv')
df_block_date.to_csv(path + 'df_block_date.csv')


### block number range
#path = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_sales_analysis//dimensional_tables//'
#df1 = pd.read_csv(path + 'df_blockNumber.csv')
#print(df1.min(), df1.max())