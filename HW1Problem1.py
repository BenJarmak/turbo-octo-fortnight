import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def nearest_euclidean(vector, k=1):
    distances = []
    data = [[0, 0, 1], [2, 2, 2], [4, 0, 3]]
    # data = [[0, 0, 1], [1, 1, 1], [-1, 1, 2]]

    for i in range(len(data)):
        distance = 0
        for j in range(len(vector)):
            distance += (vector[j] - data[i][j])**2
        distances.append([np.sqrt(distance), data[i][-1]])
    if k == 1:
        return min(distances)[1]
    else:
        distances.sort(key=lambda x: x[0])
        found_neighbors = []
        for i in range(k):
            found_neighbors.append(distances[i][1][-1])
        return max(found_neighbors, key=found_neighbors.count)

def nearest_euclidean_modified(vector, k=1):
    distances = []
    data = [[0, 0, 1], [2, 2, 2], [4, 0, 3]]
    # data = [[0, 0, 1], [1, 1, 1], [-1, 1, 2]]

    for i in range(len(data)):
        distance = 0.5*((vector[0] - data[i][0])**2) + ((vector[1] - data[i][1])**2)
        distances.append([np.sqrt(distance), data[i][-1]])
    if k == 1:
        return min(distances)[1]
    else:
        distances.sort(key=lambda x: x[0])
        found_neighbors = []
        for i in range(k):
            found_neighbors.append(distances[k][1][-1])
        return max(found_neighbors, key=found_neighbors.count)



colors = {'1': 'Red',
          '2': 'Green',
          '3': 'Blue'}
incrementals = np.arange(-3, 3, .1)
x = []
for increment in incrementals:
    x.append(incrementals)
y = []
for increment in incrementals:
    y_values = []
    for i in range(len(incrementals)):
        y_values.append(increment)
    y.append(y_values)

plt.figure(1)
for i in range(len(x)):
    x_point = incrementals[i]
    for j in range(len(y)):
        color = colors[str(nearest_euclidean([x_point, y[j][0]]))]
        plt.scatter(x_point, y[j][0], color=color)
plt.xlim(-2, 4)
plt.ylim(-2, 4)
red_legend = mpatches.Patch(color='Red', label='KNN Value = 1')
green_legend = mpatches.Patch(color='Green', label='KNN Value = 2')
blue_legend = mpatches.Patch(color='Blue', label='KNN Value = 3')
plt.title('d=sqrt((x1-z1)^2 + (x2-z2)^2)')
plt.legend(handles=[red_legend, green_legend, blue_legend], loc='upper right')
#
plt.figure(2)
for i in range(len(x)):
    x_point = incrementals[i]
    for j in range(len(y)):
        color = colors[str(nearest_euclidean_modified([x_point, y[j][0]]))]
        plt.scatter(x_point, y[j][0], color=color)
plt.xlim(-2, 4)
plt.ylim(-2, 4)
red_legend = mpatches.Patch(color='Red', label='KNN Value = 1')
green_legend = mpatches.Patch(color='Green', label='KNN Value = 2')
blue_legend = mpatches.Patch(color='Blue', label='KNN Value = 3')
plt.legend(handles=[red_legend, green_legend, blue_legend], loc='upper right')
# plt.legend(handles=[red_legend, green_legend], loc='upper right')

plt.title('d=sqrt(0.5(x1-z1)^2 + (x2-z2)^2)')
plt.show()
