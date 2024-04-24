import matplotlib.pyplot as plt

import pandas as pd

def DataVis(rawdata):

    # CSV？拿来吧你
    data = pd.read_csv(rawdata)

   # 大于2500你就别来了，看着烦
    filtered_data = data[data['Total Fwd Packets'] <= 2500]

    # 分俩组
    benign_data = filtered_data[filtered_data['Label'] == 'BENIGN']
    portmap_data = filtered_data[filtered_data['Label'] == 'Portmap']

    # 散点图
    plt.scatter(benign_data['Flow Duration'], benign_data['Total Fwd Packets'], color='blue', label='BENIGN')
    plt.scatter(portmap_data['Flow Duration'], portmap_data['Total Fwd Packets'], color='red', label='Portmap')

    # 标签和标题
    plt.xlabel('Flow Duration')
    plt.ylabel('Total Fwd Packets')
    plt.title('Scatter Plot of Flow Duration vs Total Fwd Packets')
    plt.legend()

    plt.show()
