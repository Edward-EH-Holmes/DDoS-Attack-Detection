import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def AccTime3D(algorithms,accuracies,time_used):
    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')

    bar_positions = range(len(algorithms))

    for i, (algorithm, accuracy, time_used) in enumerate(zip(algorithms, accuracies, time_used)):
        ax.bar3d(bar_positions[i], accuracy, time_used, 0.5, 0.2, 0.2, label=algorithm)

    ax.set_xlabel('Algorithm')
    ax.set_ylabel('Accuracy')
    ax.set_zlabel('Time Used (seconds)')

    ax.legend()

    plt.show()