#!/usr/bin/env python


import sys


# returns: sum of the digits of any given number
def digit_sum(num):

	num = str(num)

	if (not num.isdigit()):
		print("<!> Error at 'digit_sum':", end='')
		print("<!> Given 'num' wasn't a number\n")
		sys.exit(0)

	sum = 0

	for c in num:
		c = ord(c) - 48  # chr(48) == 0 -> '1' - 48 = 49 - 48 = 1
		sum += c


	return sum


# Main Script:

max_sum = sys.argv[1]   # maximal sum of the digits of a grid coordinate

if ((not isinstance(max_sum, int)) or (max_sum < 0)):
	print("<!> Error at main script:")
	print("<!> Parsed max. sum wasn't an int or below 0")
	sys.exit(0)

max_sum = int(max_sum)


max_coord = 0   # maximum for both, the x and y coordinate. If exceeded the
                # sum of the digits of the coordinate will always be > max_sum

on_axes   = 0   # counts accessable points with either x, y coordinate == 0
inside    = 0   # counts accessable points with both, x and y != 0

		# therefore the sum of both represents all accessable points


# find the maximal coordinate
while True:
	xsum = digit_sum(max_coord)

	if (xsum > max_sum):
		break

	max_coord += 1


# count accessable positions
for x in range(0, max_coord):

	for y in range(0, max_coord):

		dsum = digit_sum(x) + digit_sum(y)

		if (dsum <= max_sum):    # (x, y) is an accessable point

			if ((x == 0) or (y == 0)):
				on_axes += 1
			else:
				inside += 1

if (max_sum == 0):
	print(1)
else:
	# calculate result for all 4 quadrants, which means:
	#    - mirror all points on the axes at the point of origin
	#    - quadruple the ones which aren't on axes
	#    - subtract 1 for (0,0) since it got mirrored
	result = (on_axes * 2) + (inside * 4) - 1
	print(result)
