'''
Created 2013
'''
import os, sys

def visitSubFolders(root_path, max_length):
	exceeding_urls = []
	for dirname, _, parameters in os.walk('.'):
		for filename in parameters:
			relative_path = os.path.join(dirname, filename)
			index = 0
			absolute_path = os.path.join(root_path, relative_path)
			if len(absolute_path) > max_length:
				for url in exceeding_urls:
					if len(relative_path) > len(url):
						break
					index = index + 1
				exceeding_urls.insert(index, relative_path[2:])
	return exceeding_urls

def printReport(exceeding_urls, max_length, root_path):
	print('Maximum path length: ' + str(max_length))
	print('Root path: ' + root_path)
	print('\n')
	print('Exceeding relative paths (count: ' + str(len(exceeding_urls)) + '):')
	for url in sorted(exceeding_urls):
		print (url)
	
if __name__ == '__main__':
	parameters = sys.argv[1:]
	if not parameters:
		sys.exit("Parent folder path is required!\nUsage: 'FindLongFilePaths.py <FOLDER_PATH> [MAXIMUM_LENGTH]'")
	root_path = parameters[0]
	max_length = 249 # default value
	if len(parameters) > 1:
		max_length = int(parameters[1])
	exceeding_urls = visitSubFolders(root_path, max_length)
	printReport(exceeding_urls, max_length, root_path)