import requests
from datetime import date

api_key=open('alpha.txt','r').read()

# today's date (don't keep global?)
today = str(date.today()).split("-")
a = date(int(today[0]), int(today[1]), int(today[2]))
# calculates open price, (make more efficent later)
def open_price():
    data=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey={}'.format(api_key)) #outputsize=full&
    data=data.json()
    date_list = []
    for d, v in data["Time Series (Daily)"].items():
        open_p = data["Time Series (Daily)"][d]["1. open"]
        date_list_inner = []
        date_string = d.split("-")
        b = date(int(date_string[0]), int(date_string[1]), int(date_string[2]))

        date_list_inner.append(d)
        date_list_inner.append(open_p)
        date_list_inner.append((a - b).days)
        date_list.append(date_list_inner)
    print(date_list)

# formats data into [date, price, days from today]
def SMAfunc(data):
    data=data.json()
    date_list = []
    for d, v in data["Technical Analysis: SMA"].items():
        date_list_inner = []
        open_p = data["Technical Analysis: SMA"][d]["SMA"]
        date_string = d.split("-")
        b = date(int(date_string[0]),int(date_string[1]),int(date_string[2]))

        date_list_inner.append(d)
        date_list_inner.append(open_p)
        date_list_inner.append((a - b).days)
        date_list.append(date_list_inner)
    return date_list

# data into function returns lists
def SMA():
    data=requests.get("https://www.alphavantage.co/query?function=SMA&symbol=MSFT&interval=weekly&time_period=10&series_type=open&apikey={}".format(api_key))
    SMAweekly = SMAfunc(data)
    data=requests.get("https://www.alphavantage.co/query?function=SMA&symbol=MSFT&interval=monthly&time_period=10&series_type=open&apikey={}".format(api_key))
    SMAmonthly = SMAfunc(data)

    return SMAweekly, SMAmonthly

# filter
def filter(open_price, SMAweekly):
    pass

SMA()
