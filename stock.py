import requests

api_key=open('alpha.txt','r').read()

def open_price():
    data=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey={}'.format(api_key)) #outputsize=full&
    data=data.json()
    for date, v in data["Time Series (Daily)"].items():
        open_p = data["Time Series (Daily)"][date]["1. open"]
        print(date)
        print(open_p)

def SMAweekly():
    data=requests.get("https://www.alphavantage.co/query?function=SMA&symbol=MSFT&interval=weekly&time_period=10&series_type=open&apikey={}".format(api_key))
    data=data.json()
    for date, v in data["Technical Analysis: SMA"].items():
        open_p = data["Technical Analysis: SMA"][date]["SMA"]
        print(date)
        print(open_p)

def SMAmonthly():
    data=requests.get("https://www.alphavantage.co/query?function=SMA&symbol=MSFT&interval=monthly&time_period=10&series_type=open&apikey={}".format(api_key))
    data=data.json()
    for date, v in data["Technical Analysis: SMA"].items():
        open_p = data["Technical Analysis: SMA"][date]["SMA"]
        print(date)
        print(open_p)



SMAweekly()
SMAmonthly()