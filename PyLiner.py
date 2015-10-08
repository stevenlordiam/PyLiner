#!/usr/bin/python

import os
import sys

VERSION = '0.0.1'

def count_line(filepath):
	file_line_number = 0
	for file_line in open(filepath).xreadlines():
		file_line_number += 1
	return file_line_number


def print_line_number(path):
	count = 0
	lines = 0
	for root, subFolder, files in os.walk(path):
		for file in files:
			if file.endswith(".java"):
				count += 1
				lines += count_line(os.path.join(root, file))
	print "Total file number: " + str(count)
	print "Tocal line of number: " + str(lines)

if "__main__" == __name__:
	print_line_number(os.getcwd()) # get current directory line number