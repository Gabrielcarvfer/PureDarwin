#This script produces a pickle file containing a build list like the following
#
#buildList = { #  build code             plist       inherits
#             "SUFujiCascade16C67"    : ["os-x-10116","SUFujiAcker16B2659"],
#             "SUFujiAcker16B2659"  : ["os-x-10116","Fuji16A323"],
#             "Fuji16A323"          : ["os-x-1012" ,"SUGalaGlitz15G31"],
#             "SUGalaGlitz15G31"    : ["os-x-10116",""],
#             "14B25"               : ["os-x-10101",""],
#             "14A389"              : ["os-x-1010" ,""],
#             }

import pickle
from pathlib import Path
import plistlib

#Input files
mac_osx_versions_pickle = "./temp/macOsxVersionsPlists.p"
osx_versions_pickle = "./temp/osxVersionsPlists.p"
macos_versions_pickle = "./temp/macOsVersionsPlists.p"

#workFolder
workFolder = "./temp/osx_plists/"

#Output files
buildListFile = "./temp/buildList.p"

def processPlists():
    buildList = {}

    if (Path(mac_osx_versions_pickle).is_file() == False):
        raise Exception(osx_versions_pickle + " doesn't exist")

    mac_osx_versionsPlists = pickle.load(open(mac_osx_versions_pickle,'rb'))

    # Load osx plists and create the build_list structure
    for versionPlist in mac_osx_versionsPlists:
        with open(workFolder+versionPlist, 'rb') as f:
            plistDict = plistlib.load(f)
            buildList[plistDict["build"]] = plistDict



    if (Path(osx_versions_pickle).is_file() == False):
        raise Exception(osx_versions_pickle + " doesn't exist")

    osx_versionsPlists = pickle.load(open(osx_versions_pickle,'rb'))

    # Load osx plists and create the build_list structure
    for versionPlist in osx_versionsPlists:
        with open(workFolder+versionPlist, 'rb') as f:
            plistDict = plistlib.load(f)
            buildList[plistDict["build"]] = plistDict



    if (Path(macos_versions_pickle).is_file() == False):
        raise Exception(macos_versions_pickle + " doesn't exist")

    macos_versionsPlists = pickle.load(open(osx_versions_pickle,'rb'))

    # Download newer Mac OS X plists if not already downloaded
    for versionPlist in macos_versionsPlists:
        with open(workFolder+versionPlist, 'rb') as f:
            plistDict = plistlib.load(f)
            buildList[plistDict["build"]] = plistDict

    pickle.dump(buildList, open(buildListFile,"wb"))