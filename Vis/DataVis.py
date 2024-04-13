import matplotlib.pyplot as plt

import pandas as pd

def DataVis(rawdata):

    # 读取CSV文件
    data = pd.read_csv(rawdata)

   # 筛选出Total Fwd Packets小于等于2500的数据
    filtered_data = data[data['Total Fwd Packets'] <= 2500]

    # 分成两个组
    benign_data = filtered_data[filtered_data['Label'] == 'BENIGN']
    portmap_data = filtered_data[filtered_data['Label'] == 'Portmap']

    # 绘制散点图
    plt.scatter(benign_data['Flow Duration'], benign_data['Total Fwd Packets'], color='blue', label='BENIGN')
    plt.scatter(portmap_data['Flow Duration'], portmap_data['Total Fwd Packets'], color='red', label='Portmap')

    # 添加标签和标题
    plt.xlabel('Flow Duration')
    plt.ylabel('Total Fwd Packets')
    plt.title('Scatter Plot of Flow Duration vs Total Fwd Packets')
    plt.legend()

    # 显示图形
    plt.show()
