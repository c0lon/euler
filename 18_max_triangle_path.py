#!/usr/bin/env python

# Find the maximum total from top to bottom of the triangle below:
# answer = 1074

import sys

TRIANGLE = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
]

def max_triangle_path(coords):
	global TRIANGLE

	# recursion
	'''i, j = coords
	if i == len(TRIANGLE) - 1:
		return TRIANGLE[i][j]
	else:
		choices = [
			max_triangle_path((i+1, j)),
			max_triangle_path((i+1, j+1))
		]
		return TRIANGLE[i][j] + max(choices)'''

	# iteration
	for i in range(len(TRIANGLE)-2, -1, -1):
		for j in range(len(TRIANGLE[i])):
			choices = [TRIANGLE[i+1][j], TRIANGLE[i+1][j+1]]
			TRIANGLE[i][j] += max(choices)

	return TRIANGLE[0][0]

def read_triangle(filename):
	global TRIANGLE

	TRIANGLE = []
	with open(filename, 'r') as f:
		for line in f.readlines():
			TRIANGLE.append([int(x) for x in line.split(' ')])

if __name__ == '__main__':
	if len(sys.argv) == 2:
		read_triangle(sys.argv[1])

	print(max_triangle_path((0,0)))