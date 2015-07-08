import pandas as pd
import pylab as pl
import sys
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction import DictVectorizer,FeatureHasher
from sklearn.feature_extraction.text import HashingVectorizer
from datetime import datetime



#count default number of returned session items
count=5
sns.set_palette('hls')
mpl.rc("figure",figsize=(8,4))


#reads buys
def read_buy(count):
    print("Reading buys")
    buys=pd.read_csv("yoochoose-buys.dat",names=["session","timestamp","item","price","qty"],parse_dates=["timestamp"])
    if count==0:
        return buys
    return buys[:count]


#read clicks
def read_clicks(count):
    print("Reading clicks")
    clicks=pd.read_csv("yoochoose-clicks.dat",names=["session","timestamp","item","category"], dtype={'item':pd.np.int64}, converters={"category": lambda c: -1 if c=="S" else c},parse_dates=['timestamp'])
    if count==0:
        return clicks
    return clicks[:count]



buys=read_buy(0)
clicks=read_clicks(0)
item_bought=buys['item'].tolist()
print("filtering categories")
print(datetime.now().time())
item_clicked_bought=clicks[clicks['item'].isin(item_bought)]
print(datetime.now().time())
print("End Filtering ")
print("...........")
print("Logging to files")

#Writing data to ./data/exploratory.txt file
with open("./data/exploratory.txt","w") as f:
	f.write("EXPLORATORY ANALYSIS \n")
	f.write("-------------------- \n")
	f.write("BUYS \n")
	f.write("-------------------- \n")
	f.write("Unique Items bought: "+str(buys['item'].unique().size)+"\n")
	f.write("Unique Category bought: "+str(item_clicked_bought['category'].unique().size)+"\n")
	f.write("Number of item Bought : "+str(buys.shape[0])+"\n")
	f.write("Session With Buys : "+str(buys["session"].unique().size)+"\n")
	f.write("CLICKS \n")
	f.write("--------------------")
	f.write("Number of Clicks : "+str(clicks.shape[0])+"\n")
	f.write("Unique Items in click: "+str(clicks['item'].unique().size)+"\n")
	f.write("Unique Sessions : "+str(clicks["session"].unique().size)+"\n")
	f.write("Unique Category clicked: "+str(clicks['category'].unique().size)+"\n")
	f.write("CLICKS VS BUYS \n")
	f.write("Clicks ending with Buys : "+str(buys['session'].unique().size*100/float(clicks['session'].unique().size)) +"% \n")
	f.write("Bought Categories vs  Available Categories : "+str(item_clicked_bought['category'].unique().size*100/float(clicks['category'].unique().size)) +"% \n")
	f.write(str(clicks.describe())+"% \n")
	f.write(str(buys.describe())+"% \n")
print(datetime.now().time())
print("End logging")
print(datetime.now().time())
print("Starting item count by")
buys_per_session=buys[['session','item']].groupby('session').count()
buys_per_session.columns=['buys_per_session']
buys_per_session[buys_per_session['buys_per_session']<20].plot(kind='hist',bins=19)
plt.show()
print(datetime.now().time())
print("Finish item count by session")
print("Grouping session by session_id ") 
print(datetime.now().time())
timestamp_by_session = clicks[["session", "timestamp"]].groupby("session")
print("End Grouping ")  
print("counting mins and max ")  
mints = timestamp_by_session.min()
maxts = timestamp_by_session.max()
duration = maxts - mints
duration.columns = ["session_duration"] 
duration_in_s = duration["session_duration"] / np.timedelta64(1, 's')
sns.kdeplot(duration_in_s[(duration_in_s < 1000) & (duration_in_s > 0)]);
plt.show()
    































   
