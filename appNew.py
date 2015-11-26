import numpy as np
import matplotlib.pyplot as plt
import math

def DTW(train_array, test_array, w_a, w_b, w_c):
	distance_matrix = np.empty((len(train_array)+2, len(test_array)+2, ))

	distance_matrix[0, :] = 9999999
	distance_matrix[:, 0] = 9999999
	distance_matrix[1, :] = 9999999
	distance_matrix[:, 1] = 9999999

	# distance_matrix[0,0] = 0
	distance_matrix[1,1] = 0

	for i in range(2, len(train_array) + 2):
		for j in range(2, len(train_array) + 2):
			# cost = math.fabs(train_array[i - 1] - test_array[j - 1])
			a = math.fabs(train_array[i - 4] - test_array[j - 2]) + distance_matrix[i-2, j]
			b = math.fabs(train_array[i - 2] - test_array[j - 2]) + distance_matrix[i, j-2]
			c = math.fabs(train_array[i - 2] - test_array[j - 4]) + distance_matrix[i-1,j-1]
			if a > b:
				if b > c:
					min_val = c
				else:
					min_val = b
			elif a > c:
				min_val = c
			else:
				min_val = a
			

			distance_matrix[i, j] = min_val

	return distance_matrix[len(train_array), len(test_array)]


for w_a in range(1, 4):
	for w_b in range(1, 4):
		for w_c in range(1,4):
			data = np.genfromtxt("data/Beef_TRAIN",delimiter="")

			train_answer = data[:, 0]
			train_data = data[:, 1:]

			data = np.genfromtxt("data/Beef_TEST",delimiter="")

			test_answer = data[:, 0]
			test_data = data[:, 1:]

			current_test_data = []
			current_test_answer = 0
			current_train_data = []
			current_train_answer = 0
			distance_matrix = []

			accuracy = 0

			for test_num in range(0, len(test_answer)):
				min_dist = 9999999
				test_series_length = test_data[test_num].shape[0]
				current_test_data = test_data[test_num]
				current_test_answer = test_answer[test_num]
				# Calculate distance between test data and each train data
				for i in range(0, len(train_data)):
					current_train_data = train_data[i]
					current_train_answer = train_answer[i]
					dist = DTW(current_train_data, current_test_data, w_a, w_b, w_c)
					if  dist < min_dist:
						min_dist = dist
						answer = current_train_answer

				print "Trained Answer : " + str(answer)
				print "Real Answer: " + str(current_test_answer)
				print "------------------------------------"

				if int(answer) == int(current_test_answer):
					accuracy += 1
				print "Current Accuracy : " + str(accuracy) + "/" + str(len(test_answer))
				print "===================================="
			
			print "Weight(a,b,c): " + str(w_a) + ", " + str(w_b) + ", " + str(w_c)
			print "Accuracy : " + str(accuracy) + "/" + str(len(test_answer))
			print "===================================="



# print "Accuracy : " + str(accuracy / len(test_answer))

