#!/usr/bin/env python
import wget
import plistlib
from pathlib import Path

buildOpt = "14A389"

buildList = { #  build code             plist
             "SUGalaGlitz15G31"    : "os-x-10116",
             "SUGalaFiesta15F34"   : "os-x-10115",
             "SUGalaExpo15E65"     : "os-x-10114",
             "SUGalaDance15D21"    : "os-x-10113",
             "SUGalaCarnival15C50" : "os-x-10112",
             "15B42"               : "os-x-10111", #15C50 changed to SUGalaCarnival15C50
             "15A284"              : "os-x-1011" ,
             "14F27"               : "os-x-10105",
             "14E46"               : "os-x-10104",
             "14D136"              : "os-x-10103",
             "14C109"              : "os-x-10102",
             "14B25"               : "os-x-10101",
             "14A389"              : "os-x-1010" ,
             }

#Download plist from https://opensource.apple.com/plist/ + build + .plist
#   if it doesnt exist yet
plistFile = buildList[buildOpt] + ".plist"

if (Path(plistFile).is_file() == False):
    plistFile = wget.download("https://opensource.apple.com/plist/" + plistFile)

#Load specified plist
with open(plistFile, 'rb') as f:
    plistDict = plistlib.load(f)

##
#   Each key must be appended to tarballs
#       after that, append the key + "-" + version + .tar.gz and
#           then download source from https://opensource.apple.com/tarballs/
##
for project in plistDict["projects"]:
    projectFile = project + "-" + plistDict["projects"][project]["version"] + ".tar.gz"

    #check if file already exists and download if it doesnt
    if (Path(projectFile).is_file() == False):
        #catch exceptions
        try:
            projectUrl = "https://opensource.apple.com/tarballs/" + project + "/" + projectFile
            wget.download(projectUrl)
        except:
            print("Project "+ project + " tarball couldnt be downloaded, falling back to previous build")
            #TODO: download source from previous build and try again

#Extract source to folder

#Then build
