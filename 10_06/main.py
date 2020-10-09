import requests
import time
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.ss.com/lv/real-estate/flats/ogre-and-reg/sell/"


def get_html(url):
    req = requests.get(url)
    return req.text

def table_headers(all_html):
    th_data = all_html.find("tr", {"id":"head_line"})
    th_elements = th_data.find_all("td")
    th_names = [el.text for el in th_elements[1:]]
    th_names += ["desc", "url"]
    print(th_names)
    #print(th_names[7]) # desc
    #print(th_names[8]) # url
    return th_names

def table_rows(all_html):
    tr_data = all_html.find_all("tr")
    tr_elements = [row for row in tr_data if row.get('id',"").startswith("tr_") and not row.get('id',"").startswith("tr_bnr") ]
    # tr_td = tr_elements[0].find_all('td')
    # print(tr_elements)
    return tr_elements

def get_table(th, tr):
    rowDict = {}
    th = th
    i = 0
    x = 0
    for row in tr:
        row_td = tr[i].find_all('td')
        desc = row_td[2].text
        city = row_td[3].text
        room = row_td[4].text
        kv_m = row_td[5].text
        floor = row_td[6].text
        ser = row_td[7].text
        price_kvm = row_td[8].text
        price = row_td[9].text
        #print(city, price_kvm)
        rowDict.append(city)
        # for row in th:
        #     print(th[x])
        #     x+=1
        i += 1
    print(rowDict)
        


def main():
    soup = BeautifulSoup(get_html(url), 'lxml')
    header = table_headers(soup)
    rows = table_rows(soup)
    get_table(header, rows)
    #print(rows[0])

if __name__ == "__main__":
    main()

