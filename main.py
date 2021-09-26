import os
import sys


def getListOfFiles(dirName):
    listOfFiles = os.listdir(dirName)
    allFiles = list()

    for entry in listOfFiles:
        if dirName != ".":
            fullPath = os.path.join(dirName, entry)
        else:
            fullPath = entry
        if os.path.isdir(fullPath) and entry != "venv" and entry != ".idea":
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

if __name__ == '__main__':
    dirName = "."
    if len(sys.argv) > 1:
        dirName = sys.argv[1]
        os.chdir(dirName)
    listOfFiles = getListOfFiles(".")
    filename = os.path.basename(os.getcwd()) + ".m3u"
    playlist = open(filename, "w")

    for elem in listOfFiles:
        playlist.write(elem + "\n")

    playlist.close()

    playlist = open(filename, "r")
    print(playlist.read())