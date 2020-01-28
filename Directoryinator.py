import os
import shutil
import pathlib
import fnmatch
import ntpath

def findFile(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if fnmatch.fnmatch(dir, pattern):
                result.append(os.path.join(root, dir))
    return result

def path_leaf(path):
    head, tail = ntpath.split(path)
    # print(head or tail)
    return tail or ntpath.basename(head)

def moveFile(source, destination):
    newPath = destination + '\\' + path_leaf(source)
    # print(os.path.join(newPath))
    shutil.move(os.path.join(source), os.path.join(newPath))

DestinationPath = input("Please specify a directory to store the files: ")
path = input("Please specify a directory: ")
pattern = input("Please specify a pattern to look for: ")

result = findFile(pattern, path)

for x in range(len(result)):
    print(result[x])
    moveFile(result[x], DestinationPath)