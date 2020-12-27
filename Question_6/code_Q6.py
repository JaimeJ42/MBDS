#!/usr/bin/python
# -*- coding:utf-8 -*-

# Q6

'''
The basic idea of the code is counting the total number of intersections between the ray from the given point and 
the line formed between two vertices of the polygon.
If the given point is inside the polygon, the total number of intersections should be an even number,
if outside, the number should be an odd number.
If the given point coincides with the vertices of the polygon or is on the edge of the polygon,
it is also considered as inside point.
'''

from numpy import *
import numpy as np

#make sure the output figures do not use the scientific notation
np.set_printoptions(precision=None, suppress=True)

#create matrix for input data storage
polygon_matrix = zeros((10, 2))
points_matrix = zeros((10, 2))
judge_list = {}

#define a function for reading input files
def read_input(file_path, input_matrix):
    #open the input file
    file = open(file_path)
    matrix = input_matrix
    #read the data in the input file into a list(lines)
    lines = file.readlines()
    matrix_row = 0
    for line in lines:
        #clear the \n and \t in the file and pass the data to another list(list)
        list = line.replace('\n', '').split(' ')
        #write the data into the matrix
        matrix[matrix_row:] = list[0:2]
        matrix_row += 1
    return matrix

#read the polygon and points input files
polygon_matrix = read_input('/Users/jaime/Desktop/blah/AY20_MBDS_questions/Question6/input_question_6_polygon',
                            polygon_matrix)
points_matrix = read_input('/Users/jaime/Desktop/blah/AY20_MBDS_questions/Question 6/input_question_6_points',
                           points_matrix)

i = 0
l = len(points_matrix)
while l:
    px = points_matrix[i][0]
    py = points_matrix[i][1]
    cross_count = 0

    for j in range(len(polygon_matrix) - 1):
        x1 = polygon_matrix[j][0]
        y1 = polygon_matrix[j][1]
        x2 = polygon_matrix[j + 1][0]
        y2 = polygon_matrix[j + 1][1]

        #if the given point coincides with the vertex of the polygon, take it as inside point
        if (px == x1 and py == y1) or (px == x2 and py == y2):
            judge_list[i] = 'inside'

        #if the ray from the given point intersects the line formed between two vertices of the polygon
        elif (py > y1 and py <= y2) or (py <= y1 and py > y2):
            #calculate the x position of the intersection
            cross_x = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            #if the given point is on the edge of the polygon, take it as inside point
            if cross_x == px:
                judge_list[i] = 'inside'
            #if not, count the number of intersections
            if cross_x > px:
                cross_count += 1
    #if the total number of intersections is an even number, the point is outside the polygon
    if cross_count % 2 == 0:
        judge_list[i] = 'outside'
    #otherwise, the point is inside the polygon
    else:
        judge_list[i] = 'inside'

    i += 1
    l -= 1

# write out the result
out_file = open('/Users/jaime/Desktop/blah/AY20_MBDS_questions/Question 6/output_question_6', 'w')
for m in range(len(points_matrix)):
    for n in range(len(points_matrix[m])):
        out_file.write(str(int(points_matrix[m][n])) + ' ')
    out_file.write(judge_list[m] + '\n')
out_file.close()
