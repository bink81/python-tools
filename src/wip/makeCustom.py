#!/usr/bin/env python

import sys
import os
from optparse import OptionParser
import shutil

parser = OptionParser(usage="%prog [-q] FILENAME APPLICATIONHOME",
    description="Copy FILENAME into the custom folder in Maconomy application at APPLICATIONHOME",
    version="%prog 0.1.0")

parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

parser.print_version()
(options, args) = parser.parse_args()
if len(args)<2:
    parser.error("Both FILENAME and APPLICATIONHOME must be specified")
    parser.print_help()

fileURL=args[0]
if not os.path.exists(fileURL):
    parser.error("%s does not exist" % fileURL)

applicationDir=args[1]
if not os.path.exists(applicationDir):
    parser.error("%s does not exist" % applicationDir)

if options.verbose:
    print ("fileURL:"+fileURL)
    print ("applicationDir:"+ applicationDir)
    print (str(options))

relativePath = ""
if fileURL.find("MaconomyDir"):
    relativePath = fileURL[fileURL.find("MaconomyDir"):]
elif fileURL.find("Portal"):
    relativePath = fileURL[fileURL.find("Portal"):]

if relativePath != "":
    destination = os.path.join(applicationDir, "CustomInstallation", relativePath)
    os.makedirs(os.path.split(destination)[0])
    shutil.copy(fileURL, destination)
    os.chmod(destination, stat.S_IWRITE)

