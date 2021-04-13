"""
author Blogostef
WBS
2021
"""


import sys
import os
import re

def convertFileToString(fileName):
    text_file = open(fileName,"r")
    string = text_file.read()
    text_file.close()
    return string


def convertStringToFile(string, fileName):
    text_file = open(fileName,"w")
    text_file.write(string)
    text_file.close()


def removeEmptyLine(string):
    string = os.linesep.join([s for s in string.splitlines() if s])
    return string

def removeMetaData(string):
    # regEx = re.compile("NOTE Confidence:||WEBVTT||NOTE language|[0-9]{2}:[0-9]{2}:[0-9]{2}|
    result = ""
    regEx = re.compile("NOTE Confidence:|WEBVTT|NOTE language|NOTE duration|([0-9]{2}:){2}[0-9]{2}.[0-9]{3}|[0-9-a-f]{8}-([0-9-a-f]{4}-){3}[0-9-a-f]{8}")
    for line in string.splitlines():
        if not regEx.match(line):
            result = result + line
    return result

def removeLineBreaks(string):
    return string

def main(fileNameS):
    if len(fileNameS)>1:
        fileName = fileNameS[1]
        print(fileName)
        text = convertFileToString(fileName)
        text = removeEmptyLine(text)
        text = removeMetaData(text)
        convertStringToFile(text, fileName+"converted")

if __name__ == "__main__":
    main(sys.argv)
