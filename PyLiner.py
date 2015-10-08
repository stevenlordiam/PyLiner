#!/usr/bin/python

import os
import sys
import argparse

VERSION = '0.0.2'

def count_line(filepath):
	file_line_number = 0
	for file_line in open(filepath).xreadlines():
		file_line_number += 1
	return file_line_number

def print_line_number(path, file_type):
	file_count = 0
	line_count = 0
	for root, subFolder, files in os.walk(path):
		for file in files:
			if file.endswith("."+file_type):
				file_count += 1
				line_count += count_line(os.path.join(root, file))
	print "Total file number: " + str(file_count)
	print "Total line of number: " + str(line_count)

if "__main__" == __name__:
	parser = argparse.ArgumentParser(description = 'A Python tool that helps you to see how many lines of code you have written in the current project directory or user-defined path')

	parser.add_argument('-p','--path', action='store', type = str, required = False, default=os.getcwd(),
                   help='specify the path to count lines, default is current directory')

	parser.add_argument('-t','--type', action='store', type = str, required = False, default='java',
                   help='specify the file type to count lines, default is Java, you can also use py, cpp to specify your file type')

	parser.add_argument('-v', '--version', action='version', version=VERSION)

	args = parser.parse_args()
	count_path = args.path
	file_type = args.type

	print_line_number(count_path, file_type) # get current directory line number