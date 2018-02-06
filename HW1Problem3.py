import numpy as np
import sys

def findNearestEuclidean(vector, test_data, k=1, threshold=0, distance_scale=0.0, individual_scale=0.0):
    distances = []
    for line in test_data:
        distance = 0
        for i in range(len(vector)-1):
            if vector[i] < threshold:
                vector[i] = 0
            if line[i] < threshold:
                line[i] = 0
            if individual_scale != 0:
                # print((vector[i] - line[i])**2)
                d = (vector[i] - line[i])**2
                if d < individual_scale:
                    pass
                    # distance += 0.5*(vector[i] - line[i])**2
                else:
                    distance += 2*d
            else:
                distance += (vector[i] - line[i])**2
        distances.append([np.sqrt(distance), line])
    if k == 1:
        return min(distances)[1][-1]
    else:
        distances.sort(key=lambda x: x[0])
        found_neighbors = []
        for i in range(k):
            if distances[i][0]/distances[0][0] < distance_scale:
                continue
            found_neighbors.append(distances[i][1][-1])
        return max(found_neighbors, key=found_neighbors.count)


def findNearestManhattan(vector, test_data, k=1, threshold=0, distance_scale=0):
    distances = []
    for line in test_data:
        distance = 0
        for i in range(len(vector)-1):
            if vector[i] < threshold:
                vector[i] = 0
            if line[i] < threshold:
                line[i] = 0
            distance += abs(vector[i] - line[i])
        distances.append([distance, line])
    if k == 1:
        return min(distances)[1][-1]
    else:
        distances.sort(key=lambda x: x[0])
        found_neighbors = []
        for i in range(k):
            if distances[0][0] == 0:
                return distances[0][1][-1]
            if distances[i][0] < distance_scale:
                return distances[i][1][-1]
            found_neighbors.append(distances[i][1][-1])
        return max(found_neighbors, key=found_neighbors.count)


def findNearestMinkowski(vector, test_data, p=1, k=1, threshold=0, distance_scale=0):
    distances = []
    for line in test_data:
        distance = 0
        for i in range(len(vector)-1):
            if vector[i] < threshold:
                vector[i] = 0
            if line[i] < threshold:
                line[i] = 0
            distance += abs(vector[i] - line[i])**p
        distances.append([distance**(1/p), line])
    if k == 1:
        return min(distances)[1][-1]
    else:
        distances.sort(key=lambda x: x[0])
        found_neighbors = []
        for i in range(k):
            if distances[i][0]/distances[0][0] < distance_scale:
                continue
            found_neighbors.append(distances[i][1][-1])
        return max(found_neighbors, key=found_neighbors.count)

def findNearestMahalanobis(vector, test_data, cov_matrix, p=1, k=1, threshold=0, distance_scale=0):
    # Not fully implemented
    distances = []
    for line in test_data:
        line = np.matrix(line)
        vector = np.matrix(vector)
        difference = line-vector
        a = difference * cov_matrix
        b = difference.T
        # distance = (np.transpose(vector - line)*cov_matrix*(vector-line)**0.5)
        # distances.append([distance**(1/p), line])
    if k == 1:
        return min(distances)[1][-1]
    else:
        distances.sort(key=lambda x: x[0])
        found_neighbors = []
        for i in range(k):
            if distances[i][0]/distances[0][0] < distance_scale:
                continue
            found_neighbors.append(distances[i][1][-1])
        return max(found_neighbors, key=found_neighbors.count)


def binarize(test_data, threshold=25):
    for i in range(len(test_data)):
        for j in range(len(test_data[i])-1):
            if test_data[i][j] < threshold:
                test_data[i][j] = 0
            else:
                test_data[i][j] = 1
    return test_data
    # returns the test data with binarized data. Under a certain threshold = 0, above = 1

#  reads the test data in
# train_path = input("Enter the training data's relative path: ")
try:
    test = open('train.txt')
except:
    test_path = input('train.txt was not found. Please type in its relative filepath: ')
    test = open(test_path)

# validate_path = input("Enter the validation data's relative path: ")
# validation = open('validate.txt')
try:
    with open(sys.argv[1], 'r') as my_file:
        validation = (my_file.read())
except:
    validation_path = input('test.txt was not found. Please type in its relative filepath: ')
    validation = open(validation_path)

#  Cleans the data and then separates the test and training data
traindata = []
for line in test:
    line_data = []
    brokenline = line.split(' ')
    brokenline[-1] = brokenline[-1].strip('\n')
    for val in brokenline:
        try:
            line_data.append(int(val))
        except ValueError:
            pass  # Cleansing empty and newline characters
    traindata.append(line_data)

validationdata = []
for line in validation:
    line_data = []
    brokenline = line.split(' ')
    brokenline[-1] = brokenline[-1].strip('\n')
    for val in brokenline:
        try:
            line_data.append(int(val))
        except ValueError:
            pass  # Cleansing empty and newline characters
    validationdata.append(line_data)

success = 0
traindata = binarize(traindata, threshold=25)
validationdata = binarize(validationdata, threshold=25)
for vector in validationdata:
    nearest_neighbor = findNearestManhattan(vector, traindata, k=5)
    print(vector[-1], nearest_neighbor)
    if vector[-1] == nearest_neighbor:
        success += 1
print(success, success/len(validationdata))
