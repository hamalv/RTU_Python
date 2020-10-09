import requests as req
import json
import pandas as pd
import time


def main():
    url = "https://api.covid19api.com/countries"
    r = req.get(url)
    data = r.json()

    # show available keys
    print(data[1])
    print(type(data[1]['Country']))
    print(data[1]['Country'])

    # countries = data.get('countriesRoute')
    # country = countries.get('Name')
    # print(countries[2])
    # print(type(country))
    c_list = []
    i = 0
    for country in data:
        c_list.append(data[i]['Country'])
        i+=1
    print(c_list)

    
   
if __name__ == "__main__":
    main()
