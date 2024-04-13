import Gaussian_NB
import Gradient_Boosting
import Random_Forest
import DataVis
import AccTime2D as AT2D
import AccTime3D as AT3D

train_data = "./Data/train.csv"
test_data = "./Data/test.csv"
portmap_data = "./Data/Portmap.csv"

DataVis.DataVis(train_data)

accuracy_GNB, timeGNB = Gaussian_NB.GNB(train_data, test_data)

accuracy_GB , timeGB = Gradient_Boosting.GB(train_data, test_data)

accuracy_RF, timeRF = Random_Forest.RF(train_data, test_data)

algorithms = ['Gaussian Naive Bayes', 'Gradient Boosting', 'Random Forest']
accuracies = [accuracy_GNB, accuracy_GB, accuracy_RF]
time_used = [timeGNB, timeGB, timeRF]

AT2D.AccTime2D(algorithms, accuracies, time_used)

AT3D.AccTime3D(algorithms, accuracies, time_used)

print("Algorithm\t\tAccuracy\t\tTime Used")
for i in range(len(algorithms)):
    print(algorithms[i], "\t\t", round(accuracies[i], 10), "\t\t", round(time_used[i], 10))
