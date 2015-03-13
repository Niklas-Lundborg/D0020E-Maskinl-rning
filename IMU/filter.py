#!/bin/python
#coding: utf8
import os, sys

# Filtration of data from data.txt

#	+---------------------------------------------------------------------------------------+
#	| Index of b	|   0    |   1    |   2    |   3   |   4   |   5   |   6  |   7  |   8  |
#	+---------------------------------------------------------------------------------------+
#	| Type of data	| accelx | accely | accelz | gyrox | gyroy | gyroz | magx | magy | magz |
#	+---------------------------------------------------------------------------------------+


def filter():
	count = 0
	file  = "data.txt"

	f = open(file, 'r')
	e = open("filter_file", 'w')

	array = []

	a = f.readline()
	a = f.readline()
	a = f.readline()
	for a in f:
		b = a.split(',')
		if len(b) > 1:
			c = int(b[1])
		#print c
		#array.append(c)
			e.write(str(c)+' ')
	f.close()
	e.close()
	return "ok"

print filter()


#f = open('myfile','w')
#f.write('hi there\n') # python will convert \n to os.linesep
#f.close()
