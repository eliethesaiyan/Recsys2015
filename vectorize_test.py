import pandas as pd
from collections import OrderedDict
import csv
import json
import numpy as np
from datetime import datetime



#count default number of returned session items
count=5
f = "%d/%m/%Y %H:%M:%S"


script_start=datetime.now()
#reads buys
def load_sessions(count):
    vectors=pd.read_csv("yoochoose-test.dat",names=["session","timestamp","item","category"],dtype={'item':pd.np.int64},converters={'category': lambda c: -1 if c=='S' else c}, parse_dates=['timestamp'],infer_datetime_format=True) 
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
        if(update_end==False and temp_vec['timestamp']>session_end):
           update_end=True 
        if session_end==None:
           session_end=temp_vec['timestamp']
           update_end=False
        if update_end:
           session_end=session_start
        if update_start:
           session_start=temp_vec['timestamp']
           update_start=False
          #update_end=False
        print("Start date")
        print(session_start)
        print("End date")
        print(session_end)
        if dwell_init:
           dwell_time=(session_end-session_start).total_seconds()
           dwell_init=False
           before_dwell=temp_vec['timestamp']
        else:
           dwell_time=(temp_vec['timestamp']-before_dwell).total_seconds() 
           before_dwell=temp_vec['timestamp']
        print("Dwell Time")
        print(dwell_time)
        vector['1']=temp_vec['session']
        vector['2']=temp_vec['timestamp'].weekday()
        vector['3']=temp_vec['timestamp'].hour
        vector['4']=temp_vec['category']
        vector['5']=temp_vec['item']
        vector['6']=dwell_time 
        dwell_time=0 
        vectors.append(vector)
    print("session duration")
    print((session_end-session_start).total_seconds())

print(vectors)
        

def write_to_file(vector_list=None):
    with open('data/yoochoose-vec-test.dat','w') as f:
       for dic in vector_list: 
          feature_list=[]
          print(dic)
          for key,value in dic.items():
             feature_list.append(str(key)+":"+str(value))
          feature_line=" ".join(feature_list)
          f.write(feature_line+"\n")


write_to_file(vectors)
script_end=datetime.now()
print((script_end-script_start).total_seconds()/60)
print("mins")



























   
