from django.shortcuts import render
import json
from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import datetime


def home(request):

    base_url = "http://www.chittorgarh.com/report/nse_nifty_index_50_stocks_live_list/7/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    req = urllib2.Request(base_url, None, headers)
    read_url = urllib2.urlopen(req)
    response = read_url.read()
    soup = BeautifulSoup(response, "lxml")
    table = soup.find_all("table", attrs={'class': 'table'})
    table_data = [j for i in table for j in i.find_all("tr")]
    table_header = [str(j.text.strip()) for d in table_data[0:1]
                    for j in d.find_all("th")]
    table_value = table_data[1:]

    dataset = []
    header = ("name", "open", "high", "low", "ltp", "change", "ltp1", "change1", "shares_traded", "trades", "date", "size")
    for d in table_value:
        cols = d.find_all("td")
        cols = [str(element.text.strip()) for element in cols]
        size = int(float(cols[9]) / 1000)
        if size > 100:
            size = int(size / 10)
        cols.append(size)
        each_dict = dict(zip(header, tuple(cols)))
        dataset.append(each_dict)

    json_dict_val = {}
    json_dict_val["name"] = "Shares"
    json_dict_val["children"] = dataset

    with open('static/json/data_json_val.json', 'w') as jsonfile:
        json.dump(json_dict_val, jsonfile)
    context = {}
    return render(request, "index.html", context)

