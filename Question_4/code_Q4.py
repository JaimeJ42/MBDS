#!/usr/bin/python
# -*- coding:utf-8 -*-

#Q4

'''
How label work:
Use a center-symmetric matrix, structure matrix, to distinguish features(non-zero numbers) and background(zero).
In this case the structure matrix used is [[0,1,0],[1,1,1],[0,1,0]](4-connectivity).
The center of the structure matrix will traverse the elements in the array,
 to find out whether the surrounding elements belong to the same feature/are connected or not.
Elements belonging to the same feature will be labeled with the same integer.
Once an element is found to be not connected to the current feature, num_features(counter) plus one.
Elements belonging to the different features would be labeled with a different integer.
num_features shows the total number of features in the matrix.
'''

from scipy.ndimage.measurements import label
from numpy import *
import numpy as np

#make sure the output figures do not use the scientific notation
np.set_printoptions(precision=None, suppress=True)

#create a matrix for input data storage
in_matrix = zeros((10, 20), dtype=float)

#open the input file
file = open('/Users/jaime/Desktop/blah/AY20_MBDS_questions/Question 4/input_question_4')
#read the data in the input file into a list(lines)
lines = file.readlines()
in_matrix_row = 0
for line in lines:
    # clear the \n and \t in the file and pass the data to another list(list)
    list = line.replace('\n', '').replace('\t', ' ').split(' ')
    # write the data into the matrix
    in_matrix[in_matrix_row:] = list[0:20]
    in_matrix_row += 1

#convert the matrix into array, cause the input of label should be array
a = np.array(in_matrix)

b = np.transpose(a)

#label the array
labeled_array, num_features = label(b)

c = np.transpose(labeled_array)

#write out the labeled matrix
out_matrix = zeros((10, 20))
for i in range(len(c)):
    for j in range(len(c[i])):
        out_matrix[i][j] = c[i][j]

#save as a .txt file
np.savetxt('/Users/jaime/Desktop/blah/AY20_MBDS_questions/Question 4/output_question_4', out_matrix, delimiter=' ', fmt='%.0f')
