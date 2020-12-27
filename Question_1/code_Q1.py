#!/usr/bin/python
# -*- coding:utf-8 -*-

#Q1

'''
For the (m-1, n-1) point in the lower right corner of the matrix m * n, 
the length of the path from (0, 0) to this point is compared with the minimum path from (0, 0) to the point (m-1, n-2). 
If the target path is greater than this value, it means that the path arrives at (m-1, n-1) point through (m-2, n-1),
instead of (m-1, n-2).
min_length for (m-2, n-1) < max_length for (m-2, n-1) = min_length for (m-1, n-2) < max_length for (m-1, n-1)
'''

from numpy import *
import sys

sys.setrecursionlimit(1000000)

operation = []

def findpath(m, n, i, j, target_len):
    max_len = sum(list(range(1, m + 1))) + m * (n - 1)
    min_len = sum(list(range(1, m + 1))) + (n - 1)
    #D_pre_min_len = sum(list(range(1, m))) + (n - 1)
    R_pre_min_len = sum(list(range(1, m + 1))) + (n - 2)

    if target_len > max_len or target_len < min_len:
        return str('No valid operation')
    else:
        if i > 0 and j > 0:
            if (target_len - m) > R_pre_min_len:
                operation.insert(0, 'R')
                target_len -= m
                n -= 1
                j -= 1
                findpath(m, n, i, j, target_len)
            elif (target_len - m) < R_pre_min_len:
                operation.insert(0, 'D')
                target_len -= m
                m -= 1
                i -= 1
                findpath(m, n, i, j, target_len)
            elif (target_len - m) == R_pre_min_len:
                operation.insert(0, 'R')
                target_len -= m
                n -= 1
                j -= 1
                findpath(m, n, i, j, target_len)

        elif i == 0 and j != 0:
            operation.insert(0, 'R')
            target_len -= m
            n -= 1
            j -= 1
            findpath(m, n, i, j, target_len)

        elif i != 0 and j == 0:
            operation.insert(0, 'D')
            target_len -= m
            m -= 1
            i -= 1
            findpath(m, n, i, j, target_len)
        return operation

# write out the result
out_file = open('/Users/jaime/Desktop/blah/AY20_MBDS_questions/Question 1/output_question_1', 'w')
out_file.write('65 ' + "".join(findpath(9, 9, 8, 8, 65)) + '\n')
operation.clear()
out_file.write('72 ' + "".join(findpath(9, 9, 8, 8, 72)) + '\n')
operation.clear()
out_file.write('90 ' + "".join(findpath(9, 9, 8, 8, 90)) + '\n')
operation.clear()
out_file.write('110 ' + "".join(findpath(9, 9, 8, 8, 110)) + '\n')
operation.clear()
out_file.write('\n')

out_file.write('87127231192 ' + "".join(findpath(90000, 100000, 89999, 99999, 87127231192)) + '\n')
operation.clear()
out_file.write('5994891682 ' + "".join(findpath(90000, 100000, 89999, 99999, 5994891682)) + '\n')
operation.clear()
out_file.close()
