import pandas as pandas
from numpy import dstack
from numpy import vstack
from pandas import read_csv
from pandas import DataFrame

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

def load_data(data_files, path=''):
	filepath = path + data_files + '/Inertial Signals/'
	files = list()
	files += ['total_acc_x_' + data_files + '.txt', 'total_acc_y_' + data_files + '.txt', 'total_acc_z_' + data_files + '.txt']
	files += ['body_acc_x_' + data_files + '.txt', 'body_acc_y_' + data_files + '.txt', 'body_acc_z_' + data_files + '.txt']
	files += ['body_gyro_x_' + data_files + '.txt', 'body_gyro_y_' + data_files + '.txt', 'body_gyro_z_' + data_files + '.txt']
	group_file = load_groupfiles(files, filepath)
	output = load_file(path + data_files + '/y_' + data_files + '.txt')
	return group_file,output

def verif(data):
	dFrame = DataFrame(data)
	counts = dFrame.groupby(0).size()
	counts = counts.values
	for i in range(len(counts)):
		percent = counts[i] / len(dFrame) * 100
		print('Activity = %d, Total = %d, Percentage = %.3f' % (i+1, counts[i], percent))


print("Exemple pour lire une fichier : load_file(chemin du fichier)")
data = load_file('UCI HAR Dataset/train/Inertial Signals/total_acc_y_train.txt')
print(data.shape)

print("Exemple pour lire plusieurs fichier : load_groupfiles([nom des fichiers] + chemin)")
files = ['total_acc_x_train.txt', 'total_acc_y_train.txt', 'total_acc_z_train.txt']
total_acc = load_groupfiles(files, path='UCI HAR Dataset/train/Inertial Signals/')
print(total_acc.shape)

print("Exemple pour lire les données")
print("Data train")
trainX, trainy = load_data('train', 'UCI HAR Dataset/')
print(trainX.shape, trainy.shape)
print("Data test")
testX, testy = load_data('test', 'UCI HAR Dataset/')
print(testX.shape, testy.shape)

print("Verification du jeu de donnée")
train_Y = load_file('UCI HAR Dataset//train/y_train.txt')
print('Train Y Dataset')
verif(train_Y)
test_Y = load_file('UCI HAR Dataset//test/y_test.txt')
print('Test Y Dataset')
verif(test_Y)
print('Both')
combined = vstack((train_Y, test_Y))
verif(combined)