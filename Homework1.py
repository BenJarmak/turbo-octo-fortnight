import numpy as np

def findNearestEuclidean(vector, test_data, k=1, threshold=0, distance_scale=0.0, individual_scale=0):
    # 90% accurate on training data with k=1 and threshold = 0
    # 80.6% accurate on training data with k=3 and threshold = 0
    # 80.8% accurate on training data with k=3 and threshold = 25
    # 90.2% accurate on training data with k=1 and threshold = 25
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
            if distances[k][0]/distances[0][0] < distance_scale:
                continue
            found_neighbors.append(distances[k][1][-1])
        return max(found_neighbors, key=found_neighbors.count)


def findNearestManhattan(vector, test_data, k=1, threshold=0, distance_scale=0):
    # 91.8% accuracy with binarized data at a threshold of 25 and k=1
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
            if distances[k][0]/distances[0][0] < distance_scale:
                continue
            found_neighbors.append(distances[k][1][-1])
        return max(found_neighbors, key=found_neighbors.count)


def findNearestMinkowski(vector, test_data, p=1, k=1, threshold=0, distance_scale=0):
    # 91.8% with p=5 and all other values default
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
            if distances[k][0]/distances[0][0] < distance_scale:
                continue
            found_neighbors.append(distances[k][1][-1])
        return max(found_neighbors, key=found_neighbors.count)

def findNearestMahalanobis(vector, test_data, cov_matrix, p=1, k=1, threshold=0, distance_scale=0):
    # 91.8% with p=5 and all other values default
    distances = []
    for line in test_data:
        line = np.matrix(line)
        vector = np.matrix(vector)
        difference = line-vector
        a = difference * cov_matrix
        b = difference.T
        print(a*b)
        # distance = (np.transpose(vector - line)*cov_matrix*(vector-line)**0.5)
        # distances.append([distance**(1/p), line])
    if k == 1:
        return min(distances)[1][-1]
    else:
        distances.sort(key=lambda x: x[0])
        found_neighbors = []
        for i in range(k):
            if distances[k][0]/distances[0][0] < distance_scale:
                continue
            found_neighbors.append(distances[k][1][-1])
        return max(found_neighbors, key=found_neighbors.count)

def stripExtraneous(test_data):
    pass
    # returns the test data with initial and ending columns stripped from it


def binarize(test_data, threshold=25):
    for i in range(len(test_data)):
        for j in range(len(test_data[i])-1):
            if test_data[i][j] < threshold:
                test_data[i][j] = 0
            else:
                test_data[i][j] = 1
    return test_data
    # returns the test data with binarized data. Under a certain threshold = 0, above = 1


def findCorrelation(test_data):
    pass
    # takes in the test data and solves for the correlation of the indicies on the outcome





#  reads the test data in
test = open('train.txt')

#  Cleans the data and then separates the test and training data
testdata = []
traindata = []
count = 0
for line in test:
    line_data = []
    brokenline = line.split(' ')
    brokenline[-1] = brokenline[-1].strip('\n')
    for val in brokenline:
        try:
            line_data.append(int(val))
        except ValueError:
            pass  # Cleansing empty and newline characters

    count += 1
    if count <= 150:
        testdata.append(line_data)
    elif 150 < count <= 200:
        traindata.append(line_data)

    if count == 200:
        count = 0

success = 0
newarray = [np.array(picture[:-1]).reshape((28, 28)) for picture in testdata]
print (newarray[0])
# testdata = binarize(testdata, threshold=25)
# traindata = binarize(traindata, threshold=25)
# for vector in traindata:
#     nearest_neighbor = findNearestMahalanobis(vector, testdata, test_cov)
#     print(vector[-1], nearest_neighbor)
#     if vector[-1] == nearest_neighbor:
#         success += 1
# print(success, success/len(traindata))

# binarized_testdata = binarize(testdata)
# binarized_traindata = binarize(traindata)
# for vector in binarized_traindata:
#     if vector[-1] == findNearestEuclidean(vector, binarized_testdata)[1][-1]:
#         success += 1
# print(success, success/len(traindata))

# -----Validation Testing---------------
# validationfile = open('validate.txt')
# validationdata=[]
#
# for line in validationfile:
#     line_data = []
#     brokenline = line.split(' ')
#     brokenline[-1] = brokenline[-1].strip('\n')
#     for val in brokenline:
#         try:
#             line_data.append(int(val))
#         except ValueError:
#             pass  # Cleansing empty and newline characters
#     validationdata.append(line_data)
#
# success = 0
# for vector in validationdata:
#     if vector[-1] == findNearestEuclidean(vector, testdata)[1][-1]:
#         success += 1
#
# print(success, success/len(validationdata))

# binarized_testdata = binarize(testdata)
# binarized_traindata = binarize(traindata)
# for vector in binarized_traindata:
#     if vector[-1] == findNearestEuclidean(vector, binarized_testdata)[1][-1]:
#         success += 1

