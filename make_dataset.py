# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

import pandas as pd
from sklearn.feature_extraction import DictVectorizer, FeatureHasher
from sklearn.feature_extraction.text import HashingVectorizer

c_file = "./data/yoochoose-clicks.dat"
b_file = "./data/yoochoose-buys.dat"

c_index = ["SessionID", "Timestamp", "ItemID", "Category"]
b_index = ["SessionID", "Timestamp", "ItemID", "Price", "Quantity"]

#clicks = [line.strip().split(",") for line in open(c_file)]
#buys = [line.strip().split(",") for line in open(b_file)]
clicks = pd.read_csv(c_file, header=None, names=c_index)
buys = pd.read_csv(b_file, header=None, names=b_index)

# data[0]: アイテムが買われたら+1、買われないなら-1
# data[1]: リスト
print "merge clicks and buys data"
X = []
c = []
for i, click in enumerate(clicks):
    is_buy = False
    feature = {}
    for buy in buys:
        if (click[0] == buy[0] and click[2] == buy[2]):
            c.append(1)
            feature["SessionId"] = click[0]
            feature["FromTimestamp"] = click[1]
            feature["ToTimestamp"] = buy[1]
            feature["ItemId"] = click[2]
            feature["Category"] = click[3]
            feature["Price"] = buy[3]
            feature["Quantitiy"] = buy[4]
            X.append(feature)
            is_buy = True
            break
    if not is_buy:
        c.append( -1)
        feature["SessionId"] = click[0]
        feature["FromTimestamp"] = click[1]
        feature["ToTimestamp"] = 0
        feature["ItemId"] = click[2]
        feature["Category"] = click[3]
        feature["Price"] = 0
        feature["Quantitiy"] = 0
        X.append(feature)
    sys.stderr.write("\rProgress:%.2f%%" % (100. * i / len(clicks)))

# make dictvect
print "make dict vect"
v = DictVectorizer()
X_dict_sparse = v.fit_transform(X)
X_dict = [zip(map(str, row.indices), row.data) for row in X_dict_sparse]

# Feature Hashing
print "Feature Hashing"
n_features = 2**24
hasher = FeatureHasher(n_features=n_features, input_type='pair')
X_hash_sparse = hasher.fit_transform(X_dict)
X_hash = [zip(row.indices, row.data) for row in X_hash_sparse]

# make libsvm data
with open("./data/yoochoose-train.dat", "w") as f:
    for val, features in zip(c, X_hash):
        features_list = []
        for feature in features:
            features_list.append(str(feature[0]) + ":" + str(feature[1]))
        features_line = " ".join(features_list)
        f.write(str(val)+" "+features_line+"\n")
