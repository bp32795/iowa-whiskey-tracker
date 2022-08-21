import requests
import pandas as pd
import os.path

def check_csv_exists(filename,url):
    if os.path.exists(filename):
        already_created_csv = pd.read_csv(filename)
        online_table = scrape_table_from_url(url)
        if already_created_csv == online_table:
            exit()
        else:
            df = scrape_table_from_url(url)
            df.to_csv(filename)
    else:
        df = scrape_table_from_url(url)
        df.to_csv(filename)

def scrape_table_from_url(url):
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    return df




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scrape_table_from_url("https://abd.iowa.gov/alcohol/snapshot/inventory?product_op=starts&product=&items_per_page=All&category%5Ball-whiskies%5D=all-whiskies")


