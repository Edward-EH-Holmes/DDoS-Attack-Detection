import matplotlib.pyplot as plt

parameters = ['Flow Duration', 'Total Fwd Packets']
correlations = [0.3443617391525116, 0.033579691492600455]
plt.bar(parameters, correlations, color=['blue', 'lightblue'])
plt.title('Correlation between Parameters and Label')
plt.xlabel('Parameters')
plt.ylabel('Correlation Coefficient')
plt.show()