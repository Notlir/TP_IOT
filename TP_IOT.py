import tensorflow as tf
import pandas as pd

data=pd.read_csv("/UCI HAR Dataset/train/X_train.txt",delim_whitespace=True)

classes= pd.read_csv("/UCI HAR Dataset/train/y_train.txt")

print(data.shape[1])

data.info()

classes=[]

for i in range (0,100):
	classes.append(i)

print(classes)

features_train= data.loc[0:561,classes]

print(features_train)
#classifier = tf.estimator.LinearClassifier(classes)

#classifier.train(input_fn=data,steps=2000)

#predictions = classifier.predict(input_fn=classes)



