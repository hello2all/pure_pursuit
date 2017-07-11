import json
import numpy as np
# import matplotlib.pyplot as plt

from scipy import interpolate

def get_waypoint_list(n=50): # n 

    with open('path1.json', 'r') as f_in:
        path = json.load(f_in)

    x = []
    y = []

    for point in path:
        x.append(point['x'])
        y.append(point['y'])

    tck, u = interpolate.splprep([x, y], s=0.0)
    x_f, y_f = interpolate.splev(np.linspace(0, 1, n), tck)

    waypoint_list = []
    for i in range(len(x_f)):
        waypoint_list.append([x_f[i] + 100, y_f[i] + 100])
    return waypoint_list

# waypoint_list = get_waypoint_list()
# a = np.array(waypoint_list)
# plt.plot(a[:,0] ,a[:,1],'+')
# plt.show()
# print(waypoint_list)