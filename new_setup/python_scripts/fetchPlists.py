import wget
from pathlib import Path
import pickle

#Input files
mac_osx_versions_file = "./temp/macOsXVersions.p"
osx_versions_file = "./temp/osXVersions.p"
macos_versions_file = "./temp/macOsVersions.p"

#Plist output folder
plistsDir = "./temp/osx_plists/"

#Output files
mac_osx_versions_pickle = "./temp/macOsxVersionsPlists.p"
osx_versions_pickle = "./temp/osxVersionsPlists.p"
macos_versions_pickle = "./temp/macOsVersionsPlists.p"

#Download all plists from versions listed in pickeOSXVersions.py
def fetch_osx_plists():
    #output lists
    mac_osx_versionsPlists = []
    osx_versionsPlists = []
    macos_versionsPlists = []

    # Check if osx versions pickle exist, if exist process else raise exception
    if (Path(mac_osx_versions_file).is_file() != False):
        osx_versions = pickle.load(open(mac_osx_versions_file, "rb"))
        # Download old Mac OS X plists if not already downloaded
        for version in osx_versions:
            plistFile = "mac-os-x-" + version + ".plist"
            osx_versionsPlists.append(plistFile)
            if (Path(plistsDir + plistFile).is_file() == False):
                plistFile = wget.download("https://opensource.apple.com/plist/" + plistFile, plistsDir + plistFile)
    else:
        raise Exception(osx_versions_file + " doesn't exist")

    pickle.dump(osx_versionsPlists, open("./temp/macOsXVersionsPlists.p", "wb"))




    #Check if osx versions pickle exist, if exist process else raise exception
    if (Path(osx_versions_file).is_file() != False):
        osx_versions = pickle.load(open(osx_versions_file, "rb"))
        #Download old Mac OS X plists if not already downloaded
        for version in osx_versions:
            plistFile = "os-x-" + version + ".plist"
            osx_versionsPlists.append(plistFile)
            if (Path(plistsDir + plistFile).is_file() == False):
                plistFile = wget.download("https://opensource.apple.com/plist/" + plistFile, plistsDir + plistFile)
    else:
        raise Exception(osx_versions_file + " doesn't exist")

    pickle.dump(osx_versionsPlists, open("./temp/osXVersionsPlists.p","wb"))




    #Check if macOs versions pickle exist, if exist process else raise exception
    if (Path(macos_versions_file).is_file() != False):
        macos_versions = pickle.load(open(macos_versions_file, "rb"))
        #Download newer Mac OS X plists if not already downloaded
        for version in macos_versions:
            plistFile = "macos-" + version + ".plist"
            macos_versionsPlists.append(plistFile)
            if (Path(plistsDir + plistFile).is_file() == False):
                plistFile = wget.download("https://opensource.apple.com/plist/" + plistFile, plistsDir + plistFile)
    else:
        raise Exception(macos_versions_file + " doesn't exist")

    pickle.dump(macos_versionsPlists, open("./temp/macOsVersionsPlists.p","wb"))
