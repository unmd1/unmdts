import requests
import re
from unidecode import unidecode
from bs4 import BeautifulSoup
import time
import datetime
from datetime import timedelta
import os
import math
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def significant(num, signum):

    expo = str(num)[:-signum] + "00"
    return int(expo)
if not os.path.exists(os.path.dirname(__file__) + "/changeprice-logs"):
    os.makedirs(os.path.dirname(__file__) + "/changeprice-logs")
dtandtm = datetime.datetime.now()
f = open(os.path.dirname(__file__) + "/changeprice-logs/" + dtandtm.strftime("%y-%m-%d--%H-%M-%S-%f") + ".txt", "w")

s = requests.Session()
ck = {
    'login[password]':"M@hbor1330",
    'login[email]':"mrmatoofi1@gmail.com"
}

list2 = {
    'items':"4000",
    'page': "1",
    'search[type]': "all"
}
url= "https://seller.digikala.com/account/login/?_back=https://seller.digikala.com/"
url1= "https://seller.digikala.com/promotion/0/eligible-variants/search/"
url2= "https://seller.digikala.com/ajax/periodic-prices/active/search/"
r = s.post(url, data=ck)

r = s.post(url2, data=list2)
soup = BeautifulSoup(r.text, 'html.parser')
Adkpc = []
Ddkpc = []
wine=0
lose=0
errorcount=0
gotowin=0
allcount=0
addtopromotion=0
addtopromotionall=0
lent=[]
lent2=[]
ww=10
logstring=""
lastx=0
# print(soup.a.string)
for link in soup.find_all('tr',class_ = "js-edit-row"):
    Adkpc.append(link['data-id'])
    
    for datelink in link.find_all(class_="js-promotion-date-picker"):
        Adkpc.append(datelink['value'])
    Adkpc.append(link.find(class_="js-save-promotion-price-record-changes")["data-promotion-variant-id"])
    Adkpc.append(link.find(class_="js-promotion-price")["value"])
    Adkpc.append(int(unidecode(link.find_all(class_="c-mega-campaigns-join-modal__body-table-input-sub-title")[1].string.replace("حداکثر قیمت مجاز:","").replace("ریال","").replace(",",""))))




for x in range(519):
    list1 = {
        'page':x+1
        #, 'query':"15526740"
    }
    lent.append(x)
    r = s.post(url1, data=list1)
    soup = BeautifulSoup(r.text, 'html.parser')
    while len(soup.find_all('tr',class_ = "c-ui-table__row--with-hover")) < 8:
        r = s.post(url1, data=list1)
        soup = BeautifulSoup(r.text, 'html.parser')
    


    for link in soup.find_all('tr',class_ = "c-ui-table__row--with-hover"):
        allcount+=1
        if link['data-variant-id'] in Adkpc:
            lastx=0
            # indexnum=Adkpc.index(link['data-variant-id'])
            # Winner_price=unidecode(link.contents[9].string.replace(",",""))
            # price =Adkpc[indexnum+4]
            # if Winner_price < price:
            #     iwantwin = int(Winner_price)-500
            #     if iwantwin > int(Adkpc[indexnum+5]) :
            #         iwantwin = int(Adkpc[indexnum+5])
            #     lose+=1
            #     logstring="(" + str(allcount) + "-LOSER) - " + str(lose - gotowin) + ' : ' + str(Adkpc[indexnum]) + ' = From (' + str(f'{int(price):,}') + ') Goto (' + str(f'{int(iwantwin):,}') + ') - and winer price is : ' + str(f'{int(Winner_price):,}')
            #     if iwantwin > 77000 :
            #         list3 = {
            #         'promotion_variant_id': Adkpc[indexnum+3],
            #         'id': Adkpc[indexnum],
            #         'promotion_order_limit': "3",
            #         'promotion_limit': "5000",
            #         'promotion_price': iwantwin,
            #         'start_at': Adkpc[indexnum+1],
            #         'end_at': Adkpc[indexnum+2]
            #         }
            #         r2 = s.post("https://seller.digikala.com/ajax/periodic-prices/save/", data=list3)
            #         while r2.status_code == 429:
            #             errorcount+=1
            #             time.sleep(30)
            #             print("error" + str(r2.status_code),)
            #             r2 = s.post("https://seller.digikala.com/ajax/periodic-prices/save/", data=list3)
            #         gotowin+=1
            #         logstring="(" + str(allcount) + "-GO TO WIN) - " +str(gotowin) + ' : ' + str(Adkpc[indexnum]) + ' = From (' + str(f'{int(price):,}') + ') Goto (' + str(f'{int(iwantwin):,}' + ')')
                    
                    
            # else:
            #     wine+=1
            #     logstring="(" + str(allcount) + "-WINNER) - " +str(wine) + ' : ' + str(Adkpc[indexnum])
            # Ddkpc.extend([Adkpc[indexnum+3],Adkpc[indexnum],3,5000,price-1000,Adkpc[indexnum+1],Adkpc[indexnum+2]])
        else:
            addtopromotionall+=1
            price = int(unidecode(link.contents[9].string.replace(",","")))
            myprice=int(unidecode(link.contents[13].string.replace(",","")))
            if price > 10000 and myprice > 10000:
                if myprice == 300000 or myprice == 700000:
                    iwantwin = 179000
                elif myprice == 550000:
                    iwantwin = 297000
                elif myprice == 800000 or myprice == 1200000:
                    iwantwin = 497000
                else:
                    iwantwin = int(myprice - int(myprice * 0.05))

                # if iwantwin > price - 500:
                #     iwantwin = price - 500
                iwantwin2=significant(iwantwin, 2)
                print(iwantwin2,)
                if iwantwin2 > 77000:
                    addtopromotion+=1
                    dtandtm = datetime.datetime.now()
                    startdt= dtandtm + timedelta(minutes=25)
                    print('\033[92m' + startdt.strftime("%Y-%m-%d %H:%M:%S") + '\033[0m',)
                    enddt= dtandtm + timedelta(days=28)
                    list4 = {
                    'promotion_variant_id': "",
                    'id': link['data-variant-id'],
                    'promotion_order_limit': "3",
                    'promotion_limit': "5000",
                    'promotion_price': iwantwin2,
                    'start_at': startdt.strftime("%Y-%m-%d %H:%M:%S"),
                    'end_at': enddt.strftime("%Y-%m-%d %H:%M:%S")
                    }
                    r3 = s.post("https://seller.digikala.com/ajax/periodic-prices/save/", data=list4)
                    while r3.status_code == 429:
                        errorcount+=1
                        time.sleep(5)
                        print("error" + str(r3.status_code),)
                        r3 = s.post("https://seller.digikala.com/ajax/periodic-prices/save/", data=list4)
                    logstring="(" + str(allcount) + "-ADD TO PROMOTION) - " +str(addtopromotion) + ' : ' + link['data-variant-id'] + ' = Price (' + str(f'{int(iwantwin2):,}') + ')\n' + r3.text
                    f.write(logstring+"\n")
                    print(logstring,)
f.close()
print(wine)
print(lose - gotowin)
print(gotowin)
print(allcount)
print(errorcount)
print(addtopromotion)
print(addtopromotionall)
print(*lent2)
print(lastx)
# time.sleep(300)
