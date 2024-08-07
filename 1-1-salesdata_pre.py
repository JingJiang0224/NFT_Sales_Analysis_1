import requests
import json
import pandas as pd
import numpy as np
from pathlib import Path

def getMetaData(url, headers):
    response = requests.get(url, headers=headers)

    # get meta data
    metadata = json.loads(response.text)
    market_place = [nftsales['marketplace'] for nftsales in metadata['nftSales']]
    # print(market_place)
    contractAddress = [nftsales['contractAddress'] for nftsales in metadata['nftSales']]
    tokenId = [nftsales['tokenId'] for nftsales in metadata['nftSales']]
    quantity = [int(nftsales['quantity']) for nftsales in metadata['nftSales']]
    buyerAddress = [nftsales['buyerAddress'] for nftsales in metadata['nftSales']]
    sellerAddress = [nftsales['sellerAddress'] for nftsales in metadata['nftSales']]
    blockNumber = [nftsales['blockNumber'] for nftsales in metadata['nftSales']]

    sell_amount = [float(nftsales['sellerFee']['amount']) for nftsales in metadata['nftSales']]
    sell_tokenAddress = [nftsales['sellerFee']['tokenAddress'] for nftsales in metadata['nftSales']]
    sell_symbol = [nftsales['sellerFee']['symbol'] for nftsales in metadata['nftSales']]

    #### Set sell time == block time
    # sell_timestamp = [metadata['validAt']['blockTimestamp']] * len(metadata['nftSales'])

    #### Handling missing data
    # format NaN sell_decimals to 18
    sell_decimals = []
    for nftsales in metadata['nftSales']:
        if 'decimals' in nftsales['sellerFee']:
            tmp = nftsales['sellerFee']['decimals']
        else:
            tmp = 18
        sell_decimals.append(tmp)
    # format: sell_symbol == '' into 'ETH'
    # for i in range(len(sell_symbol)):
    #     if sell_symbol[i] == '':
    #         sell_symbol[i] = 'ETH'

    dict_sales_details = {'market_place': market_place, 'contractAddress': contractAddress, 'tokenId': tokenId,
                          'quantity': quantity, 'buyerAddress': buyerAddress, "sellerAddress": sellerAddress,
                          'blockNumber': blockNumber, 'sell_amount': sell_amount,
                          'sell_tokenAddress': sell_tokenAddress, 'sell_symbol': sell_symbol,
                          'sell_decimals': sell_decimals}
    df_sales_details = pd.DataFrame(dict_sales_details)


    ### add a column to format sales amount.
    df_sales_details['sell_amount2'] = df_sales_details['sell_amount'] / (np.power(10, df_sales_details['sell_decimals'].astype(np.int64)))


    # df_sales_details.to_csv('df_sales_details.csv')
    return df_sales_details, metadata

def outputFile_initial(metadata, df_sales_details, pageKey, n):
    if "pageKey" in metadata:
        file_name = 'sales_details' + '_' + pageKey + 'null_' + str(n) + '.csv'
        df_sales_details.to_csv(file_name)
        # print(file_name)

    else:
        file_name = 'sales_details_' + str(n) + '.csv'
        df_sales_details.to_csv(file_name)
        # print(file_name)

def outputFile(metadata, df_sales_details, pageKey, n):
    if "pageKey" in metadata:
        file_name = 'sales_details' + '_' + pageKey + '_' + str(n) + '.csv'
        df_sales_details.to_csv(file_name)
        # print(file_name)

    else:
        file_name = 'sales_details_' + str(n) + '.csv'
        df_sales_details.to_csv(file_name)
        # print(file_name)

def updateUrl_initial(metadata, url):
    pageKey = ''
    if "pageKey" in metadata:
        pageKey = metadata['pageKey']
        url = url + "&pageKey=" + pageKey
        # print(url)
    else:
        pass
    return pageKey, url

def updateUrl(metadata, url):
    pageKey = ''
    if "pageKey" in metadata:
        pageKey = metadata['pageKey']
        index = url.index("pageKey=")
        url = url[:index + len("pageKey=")] + pageKey
    else:
        pass
    return pageKey, url


# fromBlock=17162287&toBlock=17816433
url = "https://eth-mainnet.g.alchemy.com/nft/v2/ilAzM2HDLNS-DZOaRfRhyFz-jI_NhzyR/getNFTSales?fromBlock=17162287&toBlock=17816433&order=asc"
headers = {"accept": "application/json"}
pageKey = ''
n = 1


#print(url)
# get meta data
df_sales_details, metadata = getMetaData(url, headers)
# generate csv
outputFile_initial(metadata, df_sales_details, pageKey, n)
# update pageKey and url
pageKey, url = updateUrl_initial(metadata, url)
# print(pageKey, url)

while "pageKey" in metadata:
    n += 1
    df_sales_details, metadata = getMetaData(url, headers)

    outputFile(metadata, df_sales_details, pageKey, n)
    pageKey, url = updateUrl(metadata, url)
    # print(pageKey)
    # print(url)






