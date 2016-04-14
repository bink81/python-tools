#
# New script that copies files openened by perforce to a remote folded. You can afterwards move the whole structure to replace a PSO web-server. 
# Usage:
#			 p4getCheckedOutFiles.py D:\MaconomySources\Main
# Author: Robert Marzeta, Date: 2009.06.29
import re, optparse, sys, string, os

def executeCommand(cmd):
	print '\n>Executing command: ', cmd
	os.system(cmd)

# Main
usage = ["usage: <FileURL> <JobName>, for example (current path should belong to the project ",
	 "p4getCheckedOutFiles.py D:\MaconomySources\Main"]

parser = optparse.OptionParser(usage = '\n'.join(usage))
(options, args) = parser.parse_args()

if len(args) <> 2:
	print "There should be 2 parameters <FileURL> <DESTINATIONDIR>)"
	sys.exit()
else:
	tempFile = 'c:\\p4OpenedFiles.txt'
	executeCommand('p4 opened > ' + tempFile)

	print '>Creating temporary file:', tempFile
	infile=open(tempFile, 'r')
	templateText=""
	newDir = 'c:\OpenedFiles'
	if not os.path.exists(newDir):
		executeCommand('mkdir '+newDir)
	executeCommand('del c:\OpenedFiles\*.* /S /Q')
	executeCommand('rmdir c:\OpenedFiles\ /S /Q')
	for line in infile.readlines():
		line = line[:line.find('#')]
		line = line.replace('//depot/Releases/Maconomy/12.0','')
		line = line.replace('/','\\')
		
		newDir = 'c:\OpenedFiles'+line[:line.rfind('\\')]
		if not os.path.exists(newDir):
			executeCommand('mkdir '+newDir)
		executeCommand('copy '+args[0]+line+' c:\OpenedFiles'+line)
		
	infile.close()
	print '>end.'
