import pandas as pd
from datetime import datetime, timedelta

# create blockchain number 17162287~17816433
block_list = [i for i in range(17162287, 17816434)]

# create date from 0501-0731
start_date = datetime(2023, 5, 1)
end_date = datetime(2023, 7, 31)
timestamp_format = '%Y-%m-%d %H:%M:%S'  # Customize the format as needed

total_block_num = 654147
current_date = start_date
i = 2
date_list = [start_date.strftime(timestamp_format)]
while i <= total_block_num:
    current_date += timedelta(seconds=12.1514)
    date_list.append(current_date.strftime(timestamp_format))
    i += 1
# print(date_list)


# create DataFrame
df_timestamp_table = pd.DataFrame()
df_timestamp_table['blockNum'] = block_list
df_timestamp_table['block_timestamp'] = date_list

# Convert the 'timestamp_column' to datetime format
df_timestamp_table['block_timestamp'] = pd.to_datetime(df_timestamp_table['block_timestamp'])

# Extract YYYY-MM-DD format
df_timestamp_table['date_only'] = df_timestamp_table['block_timestamp'].dt.strftime('%Y-%m-%d')


# print(df_date_table)




file_name = 'C://Users//jingj//Documents//jingjiang_documents//daily_learning//Project//NFT_analysis_version2//meta_data//block_timestamp.csv'
df_timestamp_table.to_csv(file_name)

