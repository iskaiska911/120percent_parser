import requests as r
from bs4 import BeautifulSoup as bs
from dict_elements import headers,page_products
import math
import re
import json


def max_page(url,headers):
    req=r.get(url,headers)
    soup = bs(req.content, 'html.parser').find("span", id="ProductCount").text
    product_amount = int(''.join(filter(str.isdigit, soup)))
    max_page = math.ceil(product_amount / page_products)
    return max_page,product_amount

def items_info(url,headers):
    req = r.get(url, headers).text
    soup = bs(req, 'lxml')
    scripts = soup.findAll('script')
    for s in scripts:
        if 'var meta' in s.text:
            script = s.text
            script = script.split('var meta = ')[1]
            script = script.split(';\nfor (var attr in meta)')[0]
            jsonStr = script
            jsonObj = json.loads(jsonStr)
    return jsonObj

def item_parse(url,headers):
    req = r.get(url+'.json', headers).text
    return req
