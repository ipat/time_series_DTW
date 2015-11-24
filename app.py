import numpy as np
import matplotlib.pyplot as plt
import math

def DTW(train_array, test_array):
	distance_matrix = np.empty((len(train_array)+1, len(test_array)+1, ))

	distance_matrix[0, :] = 9999999
	distance_matrix[:, 0] = 9999999

	distance_matrix[0,0] = 0

	for i in range(1, len(train_array) + 1):
		for j in range(1, len(train_array) + 1):
			cost = math.fabs(train_array[i - 1] - test_array[j - 1])
			a = distance_matrix[i-1, j]
			b = distance_matrix[i, j-1]
			c = distance_matrix[i-1,j-1]
			if a > b:
				if b > c:
					min_val = c
				else:
					min_val = b
			elif a > c:
				min_val = c
			else:
				min_val = a

			
			smallest = distance_matrix[i - 1, j - 1]

			distance_matrix[i, j] = cost + min_val

	return distance_matrix[len(train_array), len(test_array)]



data = np.genfromtxt("data/Lightning7_TRAIN",delimiter="")

train_answer = data[:, 0]
train_data = data[:, 1:]

data = np.genfromtxt("data/Lightning7_TEST",delimiter="")

test_answer = data[:, 0]
test_data = data[:, 1:]

current_test_data = []
current_test_answer = 0
current_train_data = []
current_train_answer = 0
distance_matrix = []

min_dist = 9999999
test_series_length = test_data[0].shape[0]
current_test_data = test_data[1]
current_test_answer = test_answer[1]
# Calculate distance between test data and each train data
for i in range(0, len(train_data)):
	current_train_data = train_data[i]
	current_train_answer = train_answer[i]
	dist = DTW(current_train_data, current_test_data)
	if  dist < min_dist:
		min_dist = dist
		answer = current_train_answer

print "Trained Answer : " + str(answer)
print "Real Answer: " + str(current_test_answer)

