import pandas as pandas
from numpy import dstack
from pandas import read_csv

def load_file(filepath):
	dataframe = read_csv(filepath, header=None, delim_whitespace=True)
	return dataframe.values

def load_groupfiles(files, path=''):
	loaded = list()
	for file in files:
		data = load_file(path + file)
		loaded.append(data)
	loaded = dstack(loaded)
	return loaded

print("Exemple pour lire une fichier : load_file(chemin du fichier)")
data = load_file('UCI HAR Dataset/train/Inertial Signals/total_acc_y_train.txt')
print(data.shape)

print("Exemple pour lire plusieurs fichier : load_groupfiles([nom des fichiers] + chemin)")
files = ['total_acc_x_train.txt', 'total_acc_y_train.txt', 'total_acc_z_train.txt']
total_acc = load_groupfiles(files, path='UCI HAR Dataset/train/Inertial Signals/')
print(total_acc.shape)