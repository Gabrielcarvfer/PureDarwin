import wget
import pickle
import tarfile

from pathlib import Path

#Input files
buildListFile = "./temp/buildList.p"

#OutputDirectory
tarballsDir = "./temp/tarballs/"
sourcesDir = "./temp/sources/"

def tryTarballDownload(buildList, chosenBuild, project):
    projectFile = project + "-" + buildList[chosenBuild]["projects"][project]["version"] + ".tar.gz"
    # check if file already exists and download if it doesnt
    if (Path(tarballsDir+projectFile).is_file() == False):
        # catch exceptions
        try:
            projectUrl = "https://opensource.apple.com/tarballs/" + project + "/" + projectFile
            wget.download(projectUrl, tarballsDir + projectFile)
        except:
            print("Project " + project + " tarball couldnt be downloaded, falling back to previous build")
            if buildList[chosenBuild]["inherits"] :
                tryTarballDownload(buildList, buildList[chosenBuild]["inherits"], project)


def tryTarballExtract(buildList, chosenBuild, project):
    projectFile = project + "-" + buildList[chosenBuild]["projects"][project]["version"] + ".tar.gz"
    # check if file already exists and download if it doesnt
    if ((Path(tarballsDir+projectFile).exists() == True) and (Path(sourcesDir+project).exists() == False)):
       tar = tarfile.open(tarballsDir+projectFile)

       subdir_and_files = []
       for tarinfo in tar.getmembers():
           tarinfo.name = tarinfo.name[len(projectFile[:-7])+1:]

       tar.extractall(sourcesDir+project, members=tar.getmembers())
    else:
        if buildList[chosenBuild]["inherits"]:
            tryTarballExtract(buildList, buildList[chosenBuild]["inherits"], project)


def fetchSources(chosenBuild):
    if (Path(buildListFile).is_file() == False):
        raise Exception(buildListFile + " doesn't exist")

    buildList = pickle.load(open(buildListFile, "rb"))

    ##
    #   Each key must be appended to tarballs
    #       after that, append the key + "-" + version + .tar.gz and
    #           then download source from https://opensource.apple.com/tarballs/
    ##
    for project in buildList[chosenBuild]["projects"]:
        #recursively try to download project, and if its not available from latest version, try from the previous one
        tryTarballDownload(buildList, chosenBuild, project)

    for project in buildList[chosenBuild]["projects"]:
        #recursively try to download project, and if its not available from latest version, try from the previous one
        tryTarballExtract(buildList, chosenBuild, project)


