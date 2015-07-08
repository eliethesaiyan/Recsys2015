# Recsys2015
Code Used in RecSys2015

The Task

Given a sequence of click events performed by some user during a typical session in an e-commerce website, the goal is to predict whether the user is going to buy something or not, and if he is buying, what would be the items he is going to buy. The task could therefore be divided into two sub goals:

Is the user going to buy items in this session? Yes|No
If yes, what are the items that are going to be bought?
The Data

Download the Data

Training Data Files

The training data comprises two different files:

yoochoose-clicks.dat - Click events. Each record/line in the file has the following fields:
Session ID – the id of the session. In one session there are one or many clicks.
Timestamp – the time when the click occurred.
Item ID – the unique identifier of the item.
Category – the category of the item.
yoochoose-buys.dat - Buy events. Each record/line in the file has the following fields:
Session ID - the id of the session. In one session there are one or many buying events.
Timestamp - the time when the buy occurred.
Item ID – the unique identifier of item.
Price – the price of the item.
Quantity – how many of this item were bought.
The Session ID in yoochoose-buys.dat will always exist in the yoochoose-clicks.dat file – the records with the same Session ID together form the sequence of click events of a certain user during the session. The session could be short (few minutes) or very long (few hours), it could have one click or hundreds of clicks. All depends on the activity of the user.

Test File

The Test data is one file:

yoochoose-test.dat - identically structured as the yoochoose-clicks.dat of the training data
Session ID
Timestamp
Item ID
Category
Solution file

The task is to predict for each session in the test file, whether there is going to be a buying event in this session, and if there is, what are the items that will be bought. No need to predict quantities.

The solution file, that has to be submitted, comprises records that have exactly two fields:

solution.dat
Session ID
Comma separated list of Item IDs that have been bought in this session
All the Session IDs that exist in the solution file are coming from the test file. In the solution file there will be all the Session IDs that the challenger predicts to be ending with at least one buying event. The second field in each record/line will comprise a list of one or many Item IDs separated by “,” character. The field delimiter between Session ID and the list of Item IDs is “;”. No spaces are required in the file. An example of a solution file could be found here.

If a Session ID exists in the test file but does not exist in the solution file, it means that this is a session that the challenger predicts not to end up with a buying event. Since approximately 95% of the sessions end without a buying event, the challenge is hence twofold, first - recognize the exact sessions that end with a buying event, and second - what are the items that will be bought in these sessions.

Evaluation Measure

Consequently, the evaluation is taking into consideration the ability to predict both aspects – whether the sessions end with buying event, and what were the items that have been bought. Let’s define the following:

Sl – sessions in submitted solution file
S - All sessions in the test set
s – session in the test set
Sb – sessions in test set which end with buy
As – predicted bought items in session s
Bs – actual bought items in session s
then the score of a solution will be :


For each session which is included in the solution file, we are adding the value of   to the overall score in case the session comprises a buying event in reality. Additionally, the Jaccard score   is computed between the predicted and the actual set of bought items and is later added to the overall score. If the challenger predicts that the session will end with buying events but lists the wrong items, he still gets a positive score. 
However, in case the challenger predicts that a session ends with buying events while in reality it didn’t, then there is a penalty of which is substracted from the overall score for each wrong prediction. 
Consequently, the final score may be negative. Therefore, every score resides on the following interval:  
This unique measure developed in order to have the ability to evaluate the two tasks involved in the challenge, as well as to manage the balance of the importance between the two tasks.
Exploratory.py file give an exploratory analysis of clicks vs 
