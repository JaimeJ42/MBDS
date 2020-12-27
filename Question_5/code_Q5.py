#!/usr/bin/python
# -*- coding:utf-8 -*-

#Q5

'''
According to the order of the number of colors from the most to the least, 
the colors are placed along the grid diagonal.
The even diagonal is placed after the odd diagonal is filled
'''

from numpy import *

matrix1 = zeros((5, 5))
for i in range(int(len(matrix1))):
    if i % 2 == 0:
        for j in range(int(len(matrix1))):
            if j % 2 == 0:
                matrix1[i][j] = 1
            elif j % 2 != 0:
                matrix1[i][j] = 2
    elif i % 2 != 0:
        for j in range(int(len(matrix1))):
            if j % 2 == 0:
                matrix1[i][j] = 2
            elif j % 2 != 0:
                matrix1[i][j] = 1

matrix2 = zeros((64, 64))
L = 64
N_blue = 1451
N_white = 1072
N_green = 977
N_yellow = 467
N_red = 139
n = 0

if n < L**2/2:
    for l in range(2 * L - 1):
        if l < L:
            i = l
            j = l - i
        elif l >= L:
            i = L - 1
            j = l - i
        if l % 2 == 0:
            while i >= 0 and j < L and n < N_blue:
                matrix2[i][j] = 1
                i -= 1
                j += 1
                n += 1
            while i >= 0 and j < L and n < (N_blue + N_white):
                matrix2[i][j] = 2
                i -= 1
                j += 1
                n += 1
if n >= L**2/2:
    for l in range(2 * L - 1):
        if l < L:
            i = l
            j = l - i
        elif l >= L:
            i = L - 1
            j = l - i
        if l % 2 != 0:
            while i >= 0 and j < L and n < (N_blue + N_white):
                matrix2[i][j] = 2
                i -= 1
                j += 1
                n += 1
            while i >= 0 and j < L and n < (N_blue + N_white + N_green):
                matrix2[i][j] = 3
                i -= 1
                j += 1
                n += 1
            while i >= 0 and j < L and n < (N_blue + N_white + N_green + N_yellow):
                matrix2[i][j] = 4
                i -= 1
                j += 1
                n += 1
            while i >= 0 and j < L and n < (N_blue + N_white + N_green + N_yellow + N_red):
                matrix2[i][j] = 5
                i -= 1
                j += 1
                n += 1

# write out the result
out_file = open('/Users/jaime/Desktop/blah/AY20_MBDS_questions/Question 5/output_question_5', 'w')
for m in range(len(matrix1)):
    for n in range(len(matrix1[m])):
        if matrix1[m][n] == 1:
            out_file.write('B ')
        elif matrix1[m][n] == 2:
            out_file.write('R ')
    out_file.write('\n')
out_file.write('\n')
for m in range(len(matrix2)):
    for n in range(len(matrix2[m])):
        if matrix2[m][n] == 1:
            out_file.write('B ')
        elif matrix2[m][n] == 2:
            out_file.write('W ')
        elif matrix2[m][n] == 3:
            out_file.write('G ')
        elif matrix2[m][n] == 4:
            out_file.write('Y ')
        elif matrix2[m][n] == 5:
            out_file.write('R ')
    out_file.write('\n')
out_file.close()
