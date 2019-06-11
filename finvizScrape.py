from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

stock_list = []

def stocker():

    # L = ["","&r=21"]
    # url_list = []
    # for c in L:
    #     url1 = "https://finviz.com/screener.ashx?v=111&f=an_recom_buybetter,sh_curvol_o50,ta_highlow20d_nh,ta_highlow50d_nh,ta_highlow52w_nh,ta_perf_4w10o,ta_perf2_13w10o,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=4"
    #     url1 += c
    #     url_list.append(url1)

    # for url in url_list:
    url = "https://finviz.com/screener.ashx?v=111&f=an_recom_buybetter,sh_curvol_o100,ta_change_u,ta_highlow20d_nh,ta_highlow50d_nh,ta_highlow52w_nh,ta_perf_4w20o,ta_perf2_13w20o,ta_rsi_ob70,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa,ta_volatility_mo2&ft=3"
    uClient = uReq(url)
    page = uClient.read()
    uClient.close()
    page_soup = soup(page, "html.parser")

    dark_stocks = page_soup.findAll("tr", {"class": "table-dark-row-cp"})
    light_stocks = page_soup.findAll("tr", {"class": "table-light-row-cp"})

    all_stocks = [dark_stocks, light_stocks]
    for color_stock in all_stocks:
        for i in range(len(color_stock)):
            stocks = str((color_stock[i].td.a)).split("t=")
            stock_name = ""
            for c in stocks[1]:
                if c == "&":
                    break

                stock_name += c
            stock_list.append(stock_name)

    return (stock_list)
    # print(len(stock_list))

x = stocker()

L = ['AMD', 'CFMS', 'HEI', 'IOVA', 'MRTX', 'PAGS', 'QIWI', 'ARRY', 'DATA', 'IIPR', 'MDB', 'OKTA', 'PLAN', 'TTD']
A = []
for i in x:
    if i not in L:
        A.append(i)
print(A)