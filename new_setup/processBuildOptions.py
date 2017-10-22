from python_scripts.pickleOSXVersions import pickleOSXVersions
from python_scripts.fetchPlists import fetch_osx_plists
from python_scripts.processPlists import processPlists
from python_scripts.fetchSources import fetchSources
from pathlib import Path
import os
force_rebuild = False

buildCode = "14A389" #Choose an arbitrary OS X build to fetch sources

def make_folder(path):
    if Path(path).exists == False:
        os.mkdir(path)

def __main__():
    #Create necessary folders
    make_folder("temp")
    make_folder("temp/osx_plists")
    make_folder("temp/sources")
    make_folder("temp/tarballs")

    # If pickled versions already exist and you don't force rebuild, we skip this part
    if (not Path("osXVersions.p").is_file() ) or (not Path("macOsVersions.p").is_file() ) or force_rebuild:
        # Save list from python to pickle file
        pickleOSXVersions()

    # If pickled plists already exist and you don't force rebuild, we skip this part
    if (not Path("osxVersionsPlists.p").is_file()) or (not Path("macOsVersionsPlists.p").is_file()) or force_rebuild:
        # Download all pending plists from the list created before
        fetch_osx_plists()

    # If pickled buildList already exist and you don't force rebuild, we skip this part
    if (not Path("buildList.p").is_file()) or force_rebuild:
        # Create a build list relating versions and dependencies between them
        processPlists()

    # Download sources for desired build
    fetchSources(buildCode)

    # todo: Configure build

    # todo: Build

    return

__main__()