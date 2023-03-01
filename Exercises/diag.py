
import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    # Write your code here
    left_diagonal = 0
    right_diagonal = 0
    for i in range(len(arr)):
        left_diagonal += arr[i][i]
        print(left_diagonal)
        right_diagonal += arr[i][len(arr)-1-i]
        print(right_diagonal)
    return abs(left_diagonal - right_diagonal)

if __name__ == '__main__':

    arr = [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
    print(arr)
    print(diagonalDifference(arr))

