#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
This scripts finds files of equal sizes in a directory tree.

Created 2014
'''
import os, sys

def visitSubFolders(root_path, text_file):
	encountered_sizes = {}
	delimiter = ','
	file_count_in_directories = {}
	for dirpath, _, filenames in os.walk(root_path):
		for filename in filenames:
			relative_url = os.path.join(dirpath, filename)
			full_url = os.path.join(root_path, relative_url)
			size = os.path.getsize(full_url)
			if size in encountered_sizes:
				if dirpath in file_count_in_directories:
					new_file_count = file_count_in_directories[dirpath] + 1
					file_count_in_directories[dirpath] = new_file_count
				else:
					file_count_in_directories[dirpath] = 1
					if text_file:
						text_file.write('\n')
				file_count = file_count_in_directories[dirpath]
				if file_count > 0:
					length_equality_record = str(size) + delimiter + filename + delimiter + relative_url + delimiter + encountered_sizes[size]
					print(length_equality_record)
					if text_file:
						text_file.write(length_equality_record)
			else:
				encountered_sizes[size] = relative_url

if __name__ == '__main__':
	parameters = sys.argv[1:]
	if not parameters:
		sys.exit("Parent folder path is required!\nUsage: 'FindEqualFileSizes.py <FOLDER_PATH>'")
	root_path = parameters[0]
	print('Root path: ' + root_path)
	text_file = None
	if len(parameters) > 1:
		log_file = parameters[1]
		text_file = open(log_file, "w", encoding='UTF-8')
		print('Log file: ' + log_file)
	visitSubFolders(root_path, text_file)