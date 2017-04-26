import requests
import re
from pprint import pprint
from termcolor import colored

proxy={
    # go get a public proxy
    "http":"http://{}".format("52.43.175.248:3128"),
    "https":"http://{}".format("52.43.175.248:3128")
}
pid = input("Please enter Pid: ")
url = "http://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Product-GetVariants?pid={0}".format(pid)

user_Agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2)AppleWebKit/537.36 (KHTML, like Gecko) Chrome 55.0.2883.5 Safari/537.36"

header ={
"User-Agent": user_Agent,
"Accept-Language": "en-US,en;q=0.8"
"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

session = requests.session()
res = session.get(url, headers=header, proxies=proxy)
if(res.status_code != 200):
    print("Retrive stock failed, code: {}".format(res.status_code))
else:
    ID = 0
    ATS = 0
    T_ATS = 0
    res_json = res.json()
    variants = res.json()["variations"]["variants"]
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
