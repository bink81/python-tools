#!/usr/bin/env python

import sys
import os
import shutil
import stat

programpath = os.path.abspath(sys.path[0])
sys.path.append(os.path.join(programpath,"Lib"))
from optparse import OptionParser
import PackingUnits
import SPULib
import OsLib

parser = OptionParser(usage="%prog [-f] [-q] FILENAME APPLICATIONHOME",
    description="Compile, stamp and install FILENAME into the Maconomy application at APPLICATIONHOME",
    version="%prog 0.1.0")

parser.add_option("-s", "--sources", dest="sourcefolder",
                  help="root of sources", metavar="SOURCES")
parser.add_option("--solution", dest="solution",
                  help="install as part of SOLUTION e.g. MCS", metavar="SOLUTION")
parser.add_option("-i", "--industryaccelerator", dest="accelerator",
                  help="install as part of SOLUTION e.g. MCS", metavar="IA")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

parser.print_version()
(options, args) = parser.parse_args()
if len(args)<2:
    parser.error("Both FILENAME and APPLICATIONHOME must be specified")
    parser.print_help()

filename=args[0]
if os.path.isabs(filename):
    source=filename
else:
    source=os.path.join(os.getcwd(),filename)
if not os.path.exists(source):
    parser.error("%s does not exist" % source)

homefolder=args[1]
if not os.path.exists(homefolder):
    parser.error("%s does not exist" % homefolder)

root = source[:source.find("CustomInstallation")+18]

if options.verbose:
    print "source", source
    print "filename" ,filename
    print "homefolder", homefolder
    print "root", root
    print filename, source, homefolder
    print str(options)

if options.solution:
    spuSolutions = [options.solution]
else:
    spuDefinition = PackingUnits.getSPUDefinition(spuDefFile=os.path.join(root, PackingUnits.getSPUDefinitionBasename()))
    spuSolutions = [spdef[0] for spdef in spuDefinition]


if source.find("CustomInstallation"):
    relativePath = source[source.find("CustomInstallation")+19:]
    if options.solution:
        destination = os.path.join(homefolder, "Solutions", options.solution, "Setup", relativePath) 
    else:
        destination=os.path.join(homefolder, source[source.find("CustomInstallation"):]) 
    #FIXME: Find the "Proper" solution
    SPULib.standalone = True
    SPULib.setFunctions()
    SPULib.logfile = "d:\Temp\Temp.txt"
    tempfolder=r"D:\Temp\tempsolution"
    
    
    destination=os.path.join(tempfolder, "Solutions", relativePath) 
    os.makedirs(os.path.split(destination)[0])
    shutil.copy(source, destination)
    os.chmod(destination, stat.S_IWRITE)

    SPULib.restructureSpuFiles(tempfolder, spuSolutions) #, fileList=[relativePath])
    OsLib.move(tempfolder, homefolder, treeMove=True)
elif source.find("IA."):
    destination=os.path.join(homefolder, source[source.find("IA."):])

#os.chmod(destination, stat.S_IWRITE)

