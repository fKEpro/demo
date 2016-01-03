import os
filePath = "input.txt"
wordList = []
wordCount = 0
#Read lines into a list
file = open(filePath, 'rU')
for line in file:
  for word in line.split():
    wordList.append(word)
    wordCount += 1
print (wordList)
print ("Total words = %d" % wordCount)

#判断行数
lineCount = len(open(filePath, 'rU').readlines())
print( "文件 %s 有 %d lines." % (filePath,lineCount))



#遍历目录树

#import os
#path = "/home"
#tree = os.walk(path)

#def printFiles(dirList, spaceCount):
  #for file in dirList:
    #print ("/".rjust(spaceCount+1) + file)
#def printDirectory(dirEntry):
    #print (dirEntry[0] + "/")
    #printFiles(dirEntry[2], len(dirEntry[0]))
    #tree = os.walk(path)
#for directory in tree:
    #printDirectory(directory)


#重命名
#import os
#oldFileName = "/home/kuio/demo/output.txt"
#newFileName = "/home/kuio/demo/output1.txt"
##Old Listing
#for file in os.listdir("/home/kuio/demo/"):
  #if file.startswith("output"):
    #print (file)
##Remove file if the new name already exists
  #if os.access(newFileName, os.X_OK):
    #print ("Removing " + newFileName)
    #os.remove(newFileName)
##Rename the file
#os.rename(oldFileName, newFileName)
##New Listing
#for file in os.listdir("/home/kuio/demo/"):
  #if file.startswith("output"):
    #print (file)


import os
emptyDirs = []
path = "/trash/*"
"""
定义函数
"""
def deleteFiles(dirList, dirPath):
  for file in dirList:
    print ("Deleting " + file)
    os.remove(dirPath + "/" + file)

def removeDirectory(dirEntry):
  print ("Deleting files in " + dirEntry[0])
  deleteFiles(dirEntry[2], dirEntry[0])
  emptyDirs.insert(0, dirEntry[0])

#Enumerate the entries in the tree
tree = os.walk(path)
for directory in tree:
    removeDirectory(directory)
#Remove the empty directories
for dir in emptyDirs:
    print ("Removing " + dir)
    os.rmdir(dir)

#输出指定格式文件
import os
path = "/home/kuio/demo"
pattern = "*.py;*.txt"
#Print files that match to file extensions
def printFiles(dirList, spaceCount, typeList):
  for file in dirList:
    for ext in typeList:
      if file.endswith(ext):
        print("/".rjust(spaceCount+1) + file)
        break
#Print each sub-directory
def printDirectory(dirEntry, typeList):
    print (dirEntry[0] + "/")
    printFiles(dirEntry[2], len(dirEntry[0]),typeList)
#Convert pattern string to list of file extensions
extList = []
for ext in pattern.split(";"):
  extList.append(ext.lstrip("*"))
#Walk the tree to print files
for directory in os.walk(path):
  printDirectory(directory, extList)
  
#创建tar文件进行各种操作

