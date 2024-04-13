import matplotlib.pyplot as plt

def AccTime2D(algorithms,accuracies,time_used):
    plt.figure(figsize=(10, 6))
    bar_width = 0.35
    plt.bar([i for i in range(len(algorithms))], accuracies, color='b', label='Accuracy', width=bar_width)
    time_used_positions = [i + bar_width for i in range(len(algorithms))]
    plt.bar(time_used_positions, time_used, color='orange', label='Time Used', width=bar_width)
    plt.legend()
    plt.xticks([i + bar_width / 2 for i in range(len(algorithms))], algorithms, rotation=45)
    plt.ylabel('Values')
    plt.show()