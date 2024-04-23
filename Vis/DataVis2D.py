import matplotlib.pyplot as plt
import numpy as np

def DataVis2D(algorithms, accuracies, time_used, precision_rate, recall_rate, f1_score):
    '''
    algorithms = ['Gaussian Naive Bayes', 'Gradient Boosting', 'Random Forest']
    accuracy = [0.979968179, 0.995618039, 0.995774538]
    time_used = [0.09989119, 1.81551099, 1.84958458]
    precision_rate = [0.935483871, 0.975062344, 0.983627204]
    recall_rate = [0.187096774, 0.840860215, 0.839784946]
    f1_score = [0.311828, 0.903002, 0.906032]
    '''
    # Plot
    x = np.arange(len(algorithms))
    width = 0.15
    fig, ax = plt.subplots(figsize=(10, 6))
    bar1 = ax.bar(x - 2*width, accuracies, width, label='Accuracy')
    bar2 = ax.bar(x - width, time_used, width, label='Time Used')
    bar3 = ax.bar(x, precision_rate, width, label='Precision Rate')
    bar4 = ax.bar(x + width, recall_rate, width, label='Recall Rate')
    bar5 = ax.bar(x + 2*width, f1_score, width, label='F1 Score')
    ax.set_ylabel('Scores')
    ax.set_title('Model Evaluation')
    ax.set_xticks(x)
    ax.set_xticklabels(algorithms)
    ax.legend()
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()