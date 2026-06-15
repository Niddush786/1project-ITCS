train.py
Splitting into training and test sets

 
[ ]
from sklearn.model_selection import train_test_split
 
[ ]
#random_state=42 determines that shuffling between samples is determiistic

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2, random_state=42)
Choosing and Training a model

 
[ ]
#We will be using a decision tree classifier. Helps to classify the features easily and is easy to visualise.
#They work well on small datasets
Initialising the model

 
[ ]
from sklearn.tree import DecisionTreeClassifier
 
[ ]
model=DecisionTreeClassifier(random_state=42)

Train the model (Fitting the model)

 
[ ]
model.fit(x_train, y_train)

 

