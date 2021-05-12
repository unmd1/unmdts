import requests
import re
from unidecode import unidecode
from bs4 import BeautifulSoup
import time
import datetime
from datetime import timedelta
import json
import cssutils
import os
import io
import math

class promotions:
    def __init__(self, s):
        self.s = s

    def get_promotions(self):
        s = self.s
        r = s.get("https://seller.digikala.com/periodic-prices/active/")
        soup = BeautifulSoup(r.text, 'html.parser')
        count = int(unidecode(soup.find(class_ = "c-ui-paginator__total")["data-rows"]))
        Adkpc = []
        all=0
        repeat = math.ceil(count/1000)
        # print(repeat)
        url= "https://seller.digikala.com/ajax/periodic-prices/active/search/"
        for x in range(repeat):
            list1 = {
                'items': "1000",
                'page': x+1,
                'search[type]':"all"
            }
            r = s.post(url, data=list1)
            # print(r.text)
            soup = BeautifulSoup(r.text, 'html.parser')
            for link in soup.find_all(class_ = "js-edit-row"):
                Adkpc.append(link['data-id'])
                
                for datelink in link.find_all(class_="js-promotion-date-picker"):
                    Adkpc.append(datelink['value'])
                Adkpc.append(link.find(class_="js-save-promotion-price-record-changes")["data-promotion-variant-id"])
                Adkpc.append(link.find(class_="js-promotion-price")["value"])
                Adkpc.append(int(unidecode(link.find_all(class_="c-mega-campaigns-join-modal__body-table-input-sub-title")[1].string.replace("حداکثر قیمت مجاز:","").replace("ریال","").replace(",",""))))
                Adkpc.append(link.find(class_="js-promotion-price")["value"])
                Adkpc.append(link.find(class_="c-mega-campaigns-join-list__container-table-btn--delete")["data-promotion"])
                all+=1
                print(str(all) + " " + link['data-id'])
        return Adkpc