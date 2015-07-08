import pandas as pd
from collections import OrderedDict
import csv
import json
import numpy as np
from datetime import datetime


script_start=datetime.now()
def read_buy(count):
    print("Reading buys")
    buys=pd.read_csv("yoochoose-buys.dat",names=["session","timestamp","item","price","qty"],parse_dates=["timestamp"])
    if count==0:
        return buys
    return buys[:count]

buys=read_buy(0)
buys['counts']=buys.groupby(['item'])['item'].transform('count')
count_dict=buys.set_index('item')['counts'].to_dict()
print(count_dict)
vectors=[]

dfile=open("vectorized/yoochoose-train.dat.1") 
csv_f=csv.reader(dfile)
for row in csv_f:
    print(row[5])
    vector=OrderedDict()
    vector[0]=row[0] #label
    vector['1']=row[2]#week
    vector['2']=row[3]#hour
    vector['3']=count_dict.get(int(row[5]),0)#bought count
    vector['4']=row[6]
    vectors.append(vector) 

def write_to_file(vector_list=None):
    with open('data/yoochoose-libformat.dat.1','w') as f:
       for dic in vector_list: 
          feature_list=[]
          print(dic)
          beginLine=True
          for key,value in dic.items():
              if(beginLine):
                feature_list.append(str(value))
                beginLine=False
              else:
                feature_list.append(str(key)+":"+str(value)) 
          feature_line=" ".join(feature_list)
          f.write(feature_line+"\n")


write_to_file(vectors)
script_end=datetime.now()
print((script_end-script_start).total_seconds()/60)
print("mins")



























   
