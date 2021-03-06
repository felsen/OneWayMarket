from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import datetime


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
# final_dict = {}
column_header = ["Company_Name", "Open", "High", "Low", "LTP", "Change", "LTP1", "Percentage_Change", "Shares_Traded", "Trades", "Date_Updated"]

		"ltp1": "599",
		"shares_traded": "5480087",
		"ltp": "599",
		"trades": "89714",
		"change1": "1.02",
		"high": "600.35",
		"name": "Axis Bank Ltd.",
		"date": "9/21/2016",
		"open": "596.5",
		"change": "6.05",
		"low": "594.5",
		"size": 20

header = ("name", "open", "high", "low", "ltp", "change", "ltp1", "change1", "shares_traded", "trades", "date")

dataset = []
for d in table_value:
    cols = d.find_all("td")
    cols = [str(element.text.strip()) for element in cols]
    dataset.append(tuple(cols))
#    final_dict[cols[0]] = cols

data_frame = pd.DataFrame(data=dataset, columns=column_header)
data_frame['Date_Updated'] = pd.to_datetime(data_frame['Date_Updated'], format="%m/%d/%Y")
now = datetime.datetime.now()
csv_frame = data_frame.to_csv("today_{0}.csv".format(now), index=False)
json_converter = data_frame.to_json(path_or_buf=None, orient="records", date_format="epoch", double_precision=10, force_ascii=True, date_unit="ms", default_handler=None)

#data_dict = {}
#data_dict['name'] = "Share Market"
#data_dict['children'] = eval(json_converter)
#print data_dict

