import requests
import re
from pprint import pprint
from termcolor import colored


#app.minicart.url = "/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-MiniAddProduct";
#app.minicart.show = "/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-MiniCart";
#app.minicart.productCountUrl = "/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-ProductCount";

class stock:

    def __init__(self, pid):
        self.pid = pid

    def check(self):
        proxy={
            # go get a public proxy
            "http":"http://{}".format("52.43.175.248:3128"),
            "https":"http://{}".format("52.43.175.248:3128")
        }
        url = "http://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Product-GetVariants?pid={0}".format(self.pid)

        user_Agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2)AppleWebKit/537.36 (KHTML, like Gecko) Chrome 55.0.2883.5 Safari/537.36"

        header ={
        "User-Agent": user_Agent,
        "Accept-Language": "en-US,en;q=0.8"
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        }

        session = requests.session()
        res = session.get(url, headers=header, proxies=proxy)
        try:
            variants = res.json()["variations"]["variants"]
        except Exception as error:
            print("Retrive stock failed, code: {}".format(res.status_code))
            return

        ID = 0
        ATS = 0
        T_ATS = 0
        print("{}".format("Stock check".center(20," ")))
        print("-------------------")
        for each in variants:
            ID = each['id']
            ATS = each['ATS']
            T_ATS += ATS
            print("{0}|{1}".format(
            "{}".format(each['attributes']['size']).center(8," "),
            colored(str(each["ATS"]).center(12," "), 'green' if ATS!= 0 else 'red')))
        print("-------------------")
        print("Total stock: {}".format(colored(T_ATS,'green')))


pid = input("Please enter Pid: ")
stock = stock(pid)
stock.check()
