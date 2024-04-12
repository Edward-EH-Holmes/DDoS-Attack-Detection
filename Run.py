import time
import Gaussian_NB
import Gradient_Boosting
import Random_Forest

train_data = "./Data/train.csv"
test_data = "./Data/test.csv"

startGNB = time.time()
Gaussian_NB.GNB(train_data, test_data)
endGNB = time.time()
print(endGNB - startGNB)

startGB = time.time()
Gradient_Boosting.GB(train_data, test_data)
endGB = time.time()
print(endGB - startGB)

startRF = time.time()
Random_Forest.RF(train_data, test_data)
endRF = time.time()
print(endRF - startRF)