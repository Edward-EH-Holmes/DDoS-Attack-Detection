import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 具体数据
data = [
    (114456999, 45, 'BENIGN'),
    (114347504, 56, 'BENIGN'),
    (36435473, 6, 'BENIGN'),
    (36434705, 6, 'BENIGN'),
    (36434626, 6, 'BENIGN'),
    (3, 2, 'BENIGN'),
    (2, 2, 'BENIGN'),
    (2, 2, 'BENIGN'),
    (114456999, 45, 'BENIGN'),
    (114347504, 56, 'BENIGN'),
    (36435473, 6, 'BENIGN'),
    (36434705, 6, 'BENIGN'),
    (36434626, 6, 'BENIGN'),
    (3, 2, 'BENIGN'),
    (2, 2, 'BENIGN'),
    (2, 2, 'BENIGN'),
    (28870362, 5, 'BENIGN'),
    (118365715, 40, 'Portmap'),
    (34435249, 6, 'BENIGN'),
    (34435196, 6, 'BENIGN'),
    (34425788, 6, 'BENIGN'),
    (221, 4, 'BENIGN'),
    (171, 5, 'BENIGN'),
    (258, 4, 'BENIGN'),
    (39233, 1, 'BENIGN'),
    (1, 2, 'BENIGN'),
    (1, 2, 'BENIGN'),
    (4, 3, 'BENIGN'),
    (509, 3, 'BENIGN'),
    (96, 1, 'BENIGN'),
    (4, 3, 'BENIGN'),
    (69, 1, 'BENIGN'),
    (60, 4, 'BENIGN'),
    (1, 2, 'BENIGN'),
    (4, 3, 'BENIGN'),
    (72, 3, 'BENIGN'),
    (169805, 4, 'Portmap'),
    (117049586, 18, 'BENIGN'),
    (9029034, 6, 'BENIGN'),
    (110, 4, 'BENIGN'),
    (2, 2, 'BENIGN'),
    (932, 5, 'BENIGN'),
    (61, 1, 'BENIGN'),
    (196, 4, 'BENIGN'),
    (126, 4, 'BENIGN'),
    (1, 2, 'BENIGN'),
    (1, 2, 'BENIGN'),
    (4, 3, 'BENIGN'),
    (99, 1, 'BENIGN'),
    (4, 3, 'BENIGN'),
    (91, 1, 'BENIGN'),
    (155801, 4, 'Portmap'),
    (1, 2, 'BENIGN'),
    (135798, 4, 'BENIGN'),
    (90305, 4, 'Portmap'),
    (9014948, 6, 'BENIGN'),
    (163, 2, 'Portmap'),
    (10226642, 33, 'Portmap'),
    (998, 1, 'Portmap'),
    (394087, 1, 'Portmap'),
    (21046, 2, 'BENIGN'),
    (65028406, 14, 'BENIGN'),
    (101748, 4, 'Portmap'),
    (112297650, 39, 'BENIGN'),
    (102968, 4, 'Portmap'),
    (117015302, 40, 'Portmap'),
    (112958286, 52, 'BENIGN'),
    (21070, 2, 'BENIGN'),
    (1643102, 32, 'BENIGN'),
    (217, 1, 'BENIGN'),
    (52811, 1, 'BENIGN'),
    (10927448, 23, 'Portmap'),
    (150268, 4, 'Portmap'),
    (15670970, 16, 'BENIGN'),
    (5384485, 5, 'BENIGN'),
    (21273, 2, 'BENIGN'),
    (21275, 2, 'BENIGN'),
    (21094, 2, 'BENIGN'),
    (21219, 2, 'BENIGN'),
    (117468529, 36, 'BENIGN'),
    (5362515, 5, 'BENIGN'),
    (119460593, 38, 'BENIGN'),
    (117470374, 36, 'BENIGN'),
    (21259, 2, 'BENIGN'),
    (21261, 2, 'BENIGN'),
    (21168, 2, 'BENIGN'),
    (76404152, 38, 'BENIGN'),
    (21270, 2, 'BENIGN'),
    (129463, 16, 'BENIGN'),
    (117188224, 24, 'BENIGN'),
    (21090, 2, 'BENIGN'),
    (21100, 2, 'BENIGN'),
    (21154, 2, 'BENIGN'),
    (65859, 2, 'BENIGN'),
    (21086, 2, 'BENIGN'),
    (21356, 2, 'BENIGN'),
    (21256, 2, 'BENIGN'),
    (21374, 2, 'BENIGN'),
    (21024, 2, 'BENIGN'),
    (21005, 2, 'BENIGN'),
    (21131, 2, 'BENIGN'),
    (21186, 2, 'BENIGN'),
    (20992, 2, 'BENIGN'),
    (21078, 2, 'BENIGN'),
    (21135, 2, 'BENIGN'),
    (1, 2, 'BENIGN'),
    (174, 2, 'BENIGN'),
]

benign_data = [d for d in data if d[2] == 'BENIGN']
portmap_data = [d for d in data if d[2] == 'Portmap']

benign_x = [d[0] for d in benign_data]
benign_y = [d[1] for d in benign_data]

portmap_x = [d[0] for d in portmap_data]
portmap_y = [d[1] for d in portmap_data]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(benign_x, benign_y, zs=0, zdir='z', s=20, c='b', depthshade=True, label='BENIGN')
ax.scatter(portmap_x, portmap_y, zs=0, zdir='z', s=20, c='r', depthshade=True, label='Portmap')


ax.set_xlabel('Flow Duration')
ax.set_ylabel('Total Fwd Packets')
ax.set_zlabel('Label')
ax.set_title('3D Scatter Plot')

plt.legend()

plt.show()