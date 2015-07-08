import pandas as pd
from collections import OrderedDict
import csv
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import logging as log
from patsy import dmatrices
from pytimeparse.timeparse import timeparse
import dateutil.parser
from sklearn.linear_model  import LogisticRegression 
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score 
from sklearn import metrics 
from datetime import datetime



#count default number of returned session items
count=5
f = "%d/%m/%Y %H:%M:%S"


script_start=datetime.now()
#reads buys
def load_sessions(count):
    log.info("loading vectors")
    vectors=pd.read_csv("yoochoose/yoochoose-trains.dat.1",names=["label","session","start","stop","item","category","price","qty"],dtype={'item':pd.np.int64},converters={'category': lambda c: -1 if c=='S' else c}, parse_dates=['stop','start'],infer_datetime_format=True) 
    if count==0:
        return vectors 
    return vectors[:count]



df=load_sessions(0)
print(df)
session_list=pd.unique(df['session'].values).tolist()
print(session_list)
vectors=[]
for index,sess in enumerate(session_list): 
    session_start=None
    session_end=None
    dwell_init=True
    update_start=True
    update_end=True
    dwell_time=None
    print("Start new Session id:"+str(sess))
    temp_vect=df.loc[df['session']==sess]
    for i,temp_vec in temp_vect.iterrows():
        vector=OrderedDict()
        if(update_end==False and temp_vec['start']>=session_end):
           update_end=True 
        if update_start:
           session_start=temp_vec['start']
           update_start=False
        if session_end==None:
           update_end=True
        if update_end:
            if temp_vec['stop']!='0':
                if temp_vec['start']<pd.to_datetime(temp_vec['stop']):
                   session_end=pd.to_datetime(temp_vec['stop'])
            else:
               session_end=temp_vec['start']
          #update_end=False
        print("Start date")
        print(session_start)
        print("End date")
        print(session_end)
        if dwell_init:
            dwell_time=(session_end-session_start).total_seconds()
            dwell_init=False
            before_dwell=temp_vec['start']
        else:
            dwell_time=(temp_vec['start']-before_dwell).total_seconds() 
            before_dwell=temp_vec['start']
        print("Dwell Time")
        print(dwell_time)
        vector['label']=temp_vec['label']
        vector['session']=temp_vec['session']
        vector['weekday']=temp_vec['start'].weekday()
        vector['hour']=temp_vec['start'].hour
        vector['category']=temp_vec['category']
        vector['item']=temp_vec['item']
        vector['dwell']=dwell_time 
        dwell_time=0 
        vectors.append(vector)
    print("session duration")
    print((session_end-session_start).total_seconds())

print(vectors)
           
    #(temp_vect)
    #temp_duration=0
    #vector['session']=crow['session']
    #vector['session']=crow['session']
    #vector['session_duration']=
        


def write_to_file(vector_list=None):
    keys=vector_list[0].keys()
    with open('vectorized/yoochoose-train.dat.1','w') as f:
        dict_wrt=csv.DictWriter(f,keys)
        dict_wrt.writerows(vector_list)





write_to_file(vectors)
script_end=datetime.now()
print((script_end-script_start).total_seconds()/60)
print("mins")



























   
