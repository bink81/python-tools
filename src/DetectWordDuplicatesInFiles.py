'''
Created 2014
'''
import sys, re, collections

def fetchLinesFromFile(file_names):
	lines = []
	for file_name in file_names:
		with open(file_name) as f:
			lines += f.readlines()
	return lines

def countWords(lines):
	wordMap = {}
	for line in lines:
		words = re.compile('\w+').findall(line)
		
		for word in words:
			word = word.lower()  # # we also want capitalised repetitions
			if word in wordMap:
				wordMap[word] = wordMap[word] + 1
			else:
				wordMap[word] = 1
	return wordMap

def groupDuplicatedWords(wordMap):
	groupedWordMap = {}
	for word in wordMap.keys():
		if wordMap[word] > 1:
			count = wordMap[word]
			if not count in groupedWordMap:
				groupedWordMap[count] = []
			groupedWordMap[count].append(word)
	return groupedWordMap	

def printWords(groupedWordMap):
	sortedWordMap = collections.OrderedDict(sorted(groupedWordMap.items()))
	print('Count : Words (lower-cased)')
	for count in sortedWordMap:
		print(str(count) + "     : " + ', '.join(groupedWordMap[count]))

if __name__ == '__main__':
	parameters = sys.argv[1:]
	if not parameters:
		sys.exit("Missing: a file URL.\nUsage: 'DetectWordDuplicatesInFiles.py <FILE_URL1> <FILE_URL2> <FILE_URL...>'")
	lines = fetchLinesFromFile(parameters)
	
	wordMap = countWords(lines)
	groupedWordMap = groupDuplicatedWords(wordMap)
	printWords(groupedWordMap)