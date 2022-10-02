from ScrapeData import scrape_data_to_json
from CleanAndStoreData import clean_and_store_data
import pandas as pd
import json


json_name = 'posts.json'


if __name__ == '__main__':

    scrape_data_to_json(['https://www.blocket.se/annonser/hela_sverige?q=MacBook+Pro+M1+pro', 'https://www.blocket.se/annonser/hela_sverige?page=2&q=MacBook+Pro+M1+pro'],json_name)
    clean_json = clean_and_store_data(json_name)
    mac_df = pd.read_json(json.dumps(clean_json), orient='records')
    mac_df.to_excel('blocket_macs.xlsx')
    print(mac_df)
    # Possibility for further analysis of data using pandas
