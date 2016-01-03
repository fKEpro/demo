import linecache
filePath = "output.txt"
print (linecache.getline(filePath, 1))
print (linecache.getline(filePath, 15))
linecache.clearcache()