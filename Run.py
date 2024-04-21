import Algorithm.Gaussian_NB as GNB
import Algorithm.Gradient_Boosting as GB
import Algorithm.Random_Forest as RF
import Vis.DataVis as DataVis
import Vis.AccTime2D as AT2D
import Vis.AccTime3D as AT3D
import pandas as pd

from sklearn.naive_bayes import GaussianNB

train_data = "./Data/train.csv"
test_data = "./Data/test.csv"
portmap_data = "./Data/Portmap.csv"

DataVis.DataVis(train_data)

accuracy_GNB, timeGNB, pr_GNB, fa_GNB = GNB.GNB(train_data, test_data)

accuracy_GB , timeGB, pr_GB, fa_GB = GB.GB(train_data, test_data)

accuracy_RF, timeRF, pr_RF, fa_RF = RF.RF(train_data, test_data)

algorithms = ['GNB', 'GB', 'RF']
accuracies = [accuracy_GNB, accuracy_GB, accuracy_RF]
time_used = [timeGNB, timeGB, timeRF]
pr = [pr_GNB, pr_GB, pr_RF]
fa = [fa_GNB, fa_GB, fa_RF]

AT2D.AccTime2D(algorithms, accuracies, time_used)

AT3D.AccTime3D(algorithms, accuracies, time_used)

print("Algorithm\t Accuracy\t\t Time Used\t\t Precision Rate\t\t False Alarm Rate")
for i in range(len(algorithms)):
    print(algorithms[i], "\t\t", round(accuracies[i], 10), "\t\t", round(time_used[i], 10), "\t\t", round(pr[i], 10), "\t\t", round(fa[i], 10))

'''
model = GaussianNB()
model.fit(X_train, y_train)

new_features = pd.DataFrame({
    'Flow Duration': [10000],
    'Total Fwd Packets': [2]
})

predicted_data = GNB.predict_ddos_features(model, new_features)
'''