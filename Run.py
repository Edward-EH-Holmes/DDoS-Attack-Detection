import Algorithm.Gaussian_NB as GNB
import Algorithm.Gradient_Boosting as GB
import Algorithm.Random_Forest as RF
import Vis.DataVis as DataVis
import Vis.DataVis2D as DV2D
import Vis.DataVis3D as DV3D
import pandas as pd

from sklearn.naive_bayes import GaussianNB

train_data = "./Data/train.csv"
test_data = "./Data/test.csv"
portmap_data = "./Data/Portmap.csv"

DataVis.DataVis(train_data)

accuracy_GNB, timeGNB, pr_GNB, rr_GNB, f1_GNB = GNB.GNB(train_data, test_data)

accuracy_GB , timeGB, pr_GB, rr_GB, f1_GB = GB.GB(train_data, test_data)

accuracy_RF, timeRF, pr_RF, rr_RF, f1_RF = RF.RF(train_data, test_data)

algorithms = ['GNB', 'GB', 'RF']
accuracies = [accuracy_GNB, accuracy_GB, accuracy_RF]
time_used = [timeGNB, timeGB, timeRF]
pr = [pr_GNB, pr_GB, pr_RF]
rr = [rr_GNB, rr_GB, rr_RF]
f1 = [f1_GNB, f1_GB, f1_RF]

DV2D.DataVis2D(algorithms, accuracies, time_used, pr, rr, f1)

DV3D.DataVis3D(algorithms, accuracies, time_used, pr, rr, f1)

print("Algorithm\t Accuracy\t\t Time Used\t\t Precision Rate\t\t Recall Rate\t\t F1 Score")
for i in range(len(algorithms)):
    print(algorithms[i], "\t\t", round(accuracies[i], 10), "\t\t", round(time_used[i], 10), "\t\t", round(pr[i], 10), "\t\t", round(rr[i], 10), "\t\t", round(f1[i], 10))