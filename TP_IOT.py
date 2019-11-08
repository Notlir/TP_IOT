import tensorflow as tf
import pandas as pd

data=pd.read_csv("../UCI HAR Dataset/train/X_train.txt",delim_whitespace=True)

print(data.shape[1])


