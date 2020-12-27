#!/usr/bin/python
# -*- coding:utf-8 -*-

#Q7.1

from numpy import *
import numpy as np

#make sure the output figures do not use the scientific notation
np.set_printoptions(precision=None, suppress=True)

#define a function for counting lines
def count_lines(file_path):
    #open the input file
    file = open(file_path)
    #read the data in the input file into a list(lines)
    alllines = file.readlines()
    lines = alllines[1:]
    #count the lines
    n = 0
    for line in lines:
        n += 1
    return n

#create matrix for input data storage
coordinates_input = zeros((count_lines('/Users/jaime/Desktop/blah/AY20_MBDS_questions/Question 7/Question 7.1/input_coordinates_7_1.txt'), 2))
index_input = zeros((count_lines('/Users/jaime/Desktop/blah/AY20_MBDS_questions/Question 7/Question 7.1/input_index_7_1.txt'), 1))

#define a function for reading input files
def read_input(file_path, input_matrix):
    #open the input file
    file = open(file_path)
    matrix = input_matrix
    #read the data in the input file into a list(lines)
    alllines = file.readlines()
    lines = alllines[1:]
    matrix_row = 0
    for line in lines:
        #clear the \n and \t in the file and pass the data to another list(list)
        list = line.replace('\n', '').replace('\t', ' ').split(' ')
        #write the data into the matrix
        matrix[matrix_row:] = list[0:]
        matrix_row += 1
    return matrix

#read the coordiantes input file
coordinates_input = read_input('/Users/jaime/Desktop/blah/AY20_MBDS_questions/Question 7/Question 7.1/input_coordinates_7_1.txt',
                            coordinates_input)
#create a list for index output storage
index_output = {}

L1 = 50
L2 = 57
i = 0
l1 = len(coordinates_input)
while l1:
    x1 = coordinates_input[i][0]
    x2 = coordinates_input[i][1]
    #calculate the index according to the mathematics equation
    index_output[i] = x1 + x2 * L1
    i += 1
    l1 -= 1

# write out the result
out_file = open('/Users/jaime/Desktop/blah/AY20_MBDS_questions/Question 7/Question 7.1/output_index_7_1.txt', 'w')
out_file.write('index' + '\n')
for m in range(len(coordinates_input)):
    out_file.write(str(int(index_output[m])) + '\n')
out_file.close()

#read the index input file
index_input = read_input('/Users/jaime/Desktop/blah/AY20_MBDS_questions/Question 7/Question 7.1/input_index_7_1.txt', index_input)
#create a matrix for coordinates output storage
coordinates_output = zeros((count_lines('/Users/jaime/Desktop/blah/AY20_MBDS_questions/Question 7/Question 7.1/input_index_7_1.txt'), 2))
j = 0
l2 = len(index_input)
while l2:
    # calculate the coordinates according to the mathematics equation
    x1 = index_input[j][0] % L1
    coordinates_output[j][0] = x1
    x2 = (index_input[j][0] - x1)/L1
    coordinates_output[j][1] = x2
    j += 1
    l2 -= 1

# write out the result
out_file = open('/Users/jaime/Desktop/blah/AY20_MBDS_questions/Question 7/Question 7.1/output_coordinates_7_1.txt', 'w')
out_file.write('x1 x2' + '\n')
for m in range(len(coordinates_output)):
    for n in range(len(coordinates_output[m])):
        out_file.write(str(int(coordinates_output[m][n])) + ' ')
    out_file.write('\n')
out_file.close()
