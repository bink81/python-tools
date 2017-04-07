'''
Created in 2017 by rm
'''
import os, sys

def findFiles(root_path):
	files_with_mixed_tests = []
	for dirname, _, parameters in os.walk(root_path):
		for filename in parameters:
			if ".java" not in filename:
				continue
			relative_path = os.path.join(dirname, filename)
			absolute_path = os.path.join(root_path, relative_path)
			lines = open(absolute_path, mode='r', encoding="ISO-8859-1")
			environment_type_annotations = set()
			for line in lines:
				##print(line)
				if "EnvironmentType.LOCAL" in line:
					environment_type_annotations.add("LOCAL")
				if "EnvironmentType.CLIENT" in line:
					environment_type_annotations.add("CLIENT")
				if "EnvironmentType.WEBSERVICE" in line:
					environment_type_annotations.add("WEBSERVICE")
				if "EnvironmentType.SERVER" in line:
					environment_type_annotations.add("SERVER")
				if "EnvironmentType.MOBILE_API" in line:
					environment_type_annotations.add("MOBILE_API")
			if len(environment_type_annotations) > 1:
				files_with_mixed_tests.append(absolute_path)
	return files_with_mixed_tests

def printReport(files_with_mixed_tests, root_path):
	print('Root path: ' + root_path)
	print('\n')
	print('Exceeding relative paths (count: ' + str(len(files_with_mixed_tests)) + '):')
	for url in sorted(files_with_mixed_tests):
		print (url)
	
if __name__ == '__main__':
	parameters = sys.argv[1:]
	if not parameters:
		sys.exit("Parent folder path is required!\nUsage: 'FindTestsWithMixedContext.py <FOLDER_PATH>'")
	root_path = parameters[0]
	files_with_mixed_tests = findFiles(root_path)
	printReport(files_with_mixed_tests, root_path)