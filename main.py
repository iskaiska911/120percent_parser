from parser import max_page,items_info,item_parse
from dict_elements import headers
import time
import numpy as np
import json
import datetime
import re

max_page,product_amount=max_page('https://120percento.com/collections/all',headers=headers)
print(max_page,product_amount)

info=[]
for i in range(1,max_page+1):
    time.sleep(np.random.choice([x / 10 for x in range(7, 22)]))
    info.append(items_info(f"https://120percento.com/collections/all?page={i}",headers=headers))

names=[info[i]['products'][j]['variants'][0]['name'] for i in range(0,len(info)) for j in range(0,len(info[i]['products']))]
names=list(set([re.sub(r'\s*-\s*\d+', '', i).replace(' ','-') for i in names]))

jsonData=json.dumps(info)
filename='120percento.com'+str(datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p"))

with open(filename, 'w') as f:
    json.dump(info, f)


full_item_info=[]
for i in names:
    time.sleep(np.random.choice([x / 10 for x in range(7, 22)]))
    full_item_info.append(item_parse(f'https://120percento.com/products/{i}',headers=headers))

jsonData=json.dumps(full_item_info)
filename='full_item_120percento.com'+str(datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p"))
with open(filename, 'w') as f:
    json.dump(full_item_info, f)

