import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def nearest_euclidean(vector, k=3):
    distances = []
    data = [[5.5, 0.5, 4.5, 2],
            [7.4, 1.1, 3.6, 0],
            [5.9, 0.2, 3.4, 2],
            [9.9, 0.1, 0.8, 0],
            [6.9, -0.1, 0.6, 2],
            [6.8, -0.3, 5.1, 2],
            [4.1, 0.3, 5.1, 1],
            [1.3, -0.2, 1.8, 1],
            [4.5, 0.4, 2.0, 0],
            [0.5, 0.0, 2.3, 1],
            [5.9, -0.1, 4.4, 0],
            [9.3, -0.2, 3.2, 0],
            [1.0, 0.1, 2.8, 1],
            [0.4, 0.1, 4.3, 1],
            [2.7, -0.5, 4.2, 1]]

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
        for i in range(0, k):
            found_neighbors.append(distances[i][1])
        return max(found_neighbors, key=found_neighbors.count)


def nearest_euclidean_regression(vector, k=3):
    distances = []
    data = [[5.5, 0.5, 4.5, 2],
            [7.4, 1.1, 3.6, 0],
            [5.9, 0.2, 3.4, 2],
            [9.9, 0.1, 0.8, 0],
            [6.9, -0.1, 0.6, 2],
            [6.8, -0.3, 5.1, 2],
            [4.1, 0.3, 5.1, 1],
            [1.3, -0.2, 1.8, 1],
            [4.5, 0.4, 2.0, 0],
            [0.5, 0.0, 2.3, 1],
            [5.9, -0.1, 4.4, 0],
            [9.3, -0.2, 3.2, 0],
            [1.0, 0.1, 2.8, 1],
            [0.4, 0.1, 4.3, 1],
            [2.7, -0.5, 4.2, 1]]

    for i in range(len(data)):
        distance = 0
        for j in range(len(vector)):
            distance += (vector[j] - data[i][j])**2
        distances.append([np.sqrt(distance), data[i][-1]])
    if k == 1:
        return min(distances)[1]
    else:
        distances.sort(key=lambda x: x[0])
        found_neighbors = 0
        for i in range(k):
            found_neighbors += distances[i][0]
        return found_neighbors / k

print('The K=3 NN Classification for the first list is: ', nearest_euclidean([4.1, -0.1, 2.2]))
print('The K=3 NN Classification for the second list is: ', nearest_euclidean([6.1, 0.4, 1.3]))

print('The K=3 NN Regression for the first list is: ', nearest_euclidean_regression([4.1, -0.1, 2.2]))
print('The K=3 NN Regression for the second list is: ', nearest_euclidean_regression([6.1, 0.4, 1.3]))
