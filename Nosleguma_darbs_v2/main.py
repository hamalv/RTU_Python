# Lai pārbaudītu vai funkcija strādā, nepieciešams ieimportēt DB, 
# sql fails pielikumā, un palaižot py failu izdzēst ierakstu ar ID 2. 
# Pie nākamās cikla vajadzētu parādīties paziņojumam par jaunu ierakstu. 


import requests
import time
from win10toast import ToastNotifier
from bs4 import BeautifulSoup
import mysql.connector

mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="",
                                database="ss_sludinajumi")
db = mydb.cursor()

url = "https://www.ss.com/lv/real-estate/flats/riga/centre/sell/"
rss = "rss/"

# date & time
def select_time_now():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time

# DB
def db_select(sql_query):
    sql = db.execute(sql_query)
    result = db.fetchall()
    return result

def db_insert(sql_query, sql_values):
    db.execute(sql_query, sql_values)
    mydb.commit()


# html
def get_html(url):
    req = requests.get(url)
    return req.text

def get_item_once(soup):
    items = soup.find("item")
    item_date = items.pubdate.text
    item_url = items.description.a["href"]
    get_item_data(item_url, item_date)

def get_item(soup, last_row_date):
    time_now = select_time_now()

    items = soup.find("item")
    item_date = items.pubdate.text

    last_inserted_date = last_row_date
    item_url = items.description.a["href"]

    if item_date == last_inserted_date:
        print(f"Time: {time_now} Visi ieraksti ir saglabati. Pedeja ieraksta datums: {last_inserted_date}")
    else:
        get_item_data(item_url, item_date)
        print("------------------------------------------------------------------")
        print(f"!!!   Jauns ieraksts   !!! \nDatums: {item_date} \nUrl: {item_url} \nTime: {time_now}")
        print("------------------------------------------------------------------")
        toaster = ToastNotifier()
        toaster.show_toast("Jauns dzīvoklis.", f"\nDatums: {item_date} \nUrl: {item_url}\nTime: {time_now}")




    #############################################################
    # Sākumā biju uztaisījis, ka ielasa visus itemus un to datus pēc url,  
    # bet sapratu, ka tā informācija man nav aktuāla, jo mani  
    # interesē ieraudzīt sludinājumu uzreiz pēc tā ievietošanas portālā.
    
    # items = soup.find_all("item")
    # for item in items:
    #     item_url = item.description.a["href"]
    #     item_date = item.pubdate.text
    #     print(item_url) 
    #     get_item_data(item_url, item_date)
    #     time.sleep(0.5)

    #############################################################




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
    only_once = False
    if only_once == False:
        soup = BeautifulSoup(get_html(url+rss), 'lxml')
        get_item_once(soup)
        only_once = True

    while True:
        soup = BeautifulSoup(get_html(url+rss), 'lxml')

        last_row_id = db_select("SELECT max(id) from dzivokli_ogre")
        last_row_db_id = last_row_id[0][0]
        last_row = db_select(f"SELECT * from dzivokli_ogre where id={last_row_db_id}")
        last_row_date = last_row[0][1]
        
        get_item(soup, last_row_date)
        time.sleep(60)
    


if __name__ == "__main__":
    main()
