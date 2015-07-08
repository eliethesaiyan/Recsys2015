# Recsys2015
Code Used in RecSys2015

The Task

Given a sequence of click events performed by some user during a typical session in an e-commerce website, the goal is to predict whether the user is going to buy something or not, and if he is buying, what would be the items he is going to buy. The task could therefore be divided into two sub goals:

Is the user going to buy items in this session? Yes|No
If yes, what are the items that are going to be bought?
##The Data

[Download the Data](http://s3-eu-west-1.amazonaws.com/yc-rdata/yoochoose-data.7z)


###The training data comprises two different files:

*yoochoose-clicks.dat - Click events. Each record/line in the file has the following fields:
*Session ID – the id of the session. In one session there are one or many clicks.
*Timestamp – the time when the click occurred.
*Item ID – the unique identifier of the item.
*Category – the category of the item.
*yoochoose-buys.dat - Buy events. Each record/line in the file has the following fields:
*Session ID - the id of the session. In one session there are one or many buying events.
*Timestamp - the time when the buy occurred.
*Item ID – the unique identifier of item.
*Price – the price of the item.
*Quantity – how many of this item were bought.
*he Session ID in yoochoose-buys.dat will always exist in the yoochoose-clicks.dat file – the records with the same Session ID together form the sequence of click events of a certain user during the session. The session could be short (few minutes) or very long (few hours), it could have one click or hundreds of clicks. All depends on the activity of the user.

##Test File

###The Test data is one file:

*yoochoose-test.dat - identically structured as the yoochoose-clicks.dat of the training data
*Session ID
*Timestamp
*Item ID
*Category
*Solution file

The task is to predict for each session in the test file, whether there is going to be a buying event in this session, and if there is, what are the items that will be bought. No need to predict quantities.

The solution file, that has to be submitted, comprises records that have exactly two fields:

*solution.dat
*Session ID
Comma separated list of Item IDs that have been bought in this session
All the Session IDs that exist in the solution file are coming from the test file. In the solution file there will be all the Session IDs that the challenger predicts to be ending with at least one buying event. The second field in each record/line will comprise a list of one or many Item IDs separated by “,” character. The field delimiter between Session ID and the list of Item IDs is “;”. No spaces are required in the file. An example of a solution file could be found here.

[More on the challenge here](http://http://2015.recsyschallenge.com/challenge.html)

##The files in repo
*make_dataset.py creates logs vector pairs after grouping clicks and buys together is session log(@ishiyama)
*exploratory.py gives an insight of clicks over buys and time
*libformat_generator.py generates training set format that can be read by [libsvm-python](https://github.com/arnaudsj/libsvm/tree/master/python) from file generated by vectorize(training set)

*libformat_test.py does the same for the test data
*pip-require.txt  has some essential pip package to install
*vectorize.py creates vectors from make_dataset.py
*vectorize_test.py creates vectors for test_set

