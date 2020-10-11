import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
import mysql.connector
import re as regexp

mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="",
                                database="ss_sludinajumi")
db = mydb.cursor()

url = "https://www.ss.com/lv/real-estate/flats/ogre-and-reg/ogre/sell/"
rss = "rss/"

# DB
def db_select(sql_query):
    sql = db.execute(sql_query)
    result = db.fetchall()
    return result

def db_insert(sql_query, sql_values):
    db.execute(sql_query, sql_values)
    mydb.commit()
    print("Dati pievienoti DB")


# html
def get_html(url):
    req = requests.get(url)
    return req.text



def get_item(soup):
    items = soup.find_all("item")
    for item in items:
        item_url = item.description.a["href"]
        item_date = item.pubdate.text
        print("-----------------------------------------------------------")
        print(item_url) 
        get_item_data(item_url, item_date)
        time.sleep(0.5)

def get_item_data(item_url, item_date):
    item_html = BeautifulSoup(get_html(item_url), 'lxml')
    div_data = item_html.find("div", {"id": "msg_div_msg"})
    table_data = div_data.find("table", {"class": "options_list"})
    table_row_data = table_data.tr.find_all("tr")
    price_data = div_data.find("td", {"class": "ads_price"})

    tr_name = []
    tr_data = []

    for row in table_row_data:
        r_name = row.find("td", {"class": "ads_opt_name"})
        r_data = row.find("td", {"class": "ads_opt"})
        tr_name+=[r_name.text]
        tr_data+=[r_data.text]

    date = item_date
    rajons = tr_data[0]
    pilseta = tr_data[1]
    iela = tr_data[2]
    istabas = tr_data[3]
    kv_m = tr_data[4]
    stavs = tr_data[5]
    cena = price_data.text
    url = item_url
    
    sql = "INSERT INTO ss_sludinajumi.dzivokli_ogre (date, rajons, pilseta, iela, istabas, kvm, stavs, cena, url) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    sql_val = (date, rajons, pilseta, iela, istabas, kv_m, stavs, cena, url)

    db_insert(sql, sql_val)




def main():
    soup = BeautifulSoup(get_html(url+rss), 'lxml')
    print("=======================================================================")
    get_item(soup)
    

    


if __name__ == "__main__":
    main()
