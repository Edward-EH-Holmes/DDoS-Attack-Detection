import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def DataVis3D(algorithms, accuracies, time_used, precision_rate, recall_rate, f1_score):
    '''
    models = ['Gaussian Naive Bayes', 'Gradient Boosting', 'Random Forest']
    accuracies = [0.979968179, 0.995618039, 0.995774538]
    times_used = [0.09989119, 1.81551099, 1.84958458]
    precisions = [0.935483871, 0.975062344, 0.983627204]
    recalls = [0.187096774, 0.840860215, 0.839784946]
    f1_scores = [0.311828, 0.903002, 0.906032]
    '''

    fig = plt.figure(figsize=(12, 10))

    ax = fig.add_subplot(111, projection='3d')

    markers = ['o', '^', 's']

    for i, algorithm in enumerate(algorithms):
        ax.scatter(accuracies[i], time_used[i], precision_rate[i], 
                marker=markers[i], 
                label=algorithm, 
                facecolors='none', edgecolors='blue')

    for i, algorithm in enumerate(algorithms):
        offset = -0.002
        ax.text(accuracies[i], time_used[i] - offset, precision_rate[i] - offset,
                f"F1: {f1_score[i]:.3f}\nRecall: {recall_rate[i]:.3f}",
                fontsize=10, ha='center', va='center')

    ax.set_xlabel('Accuracy')
    ax.set_ylabel('Time Used (seconds)')
    ax.set_zlabel('Precision Rate')

    ax.legend()

    ax.set_xlim(0.9, 1.0)
    ax.set_ylim(0, 2.5)
    ax.set_zlim(0.9, 1.0)
    plt.show()