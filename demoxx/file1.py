#open file
inPath = "input.txt"
outPath = "output.txt"
#Open a file for reading
file = open(inPath, 'rU')
if file:
# read from file here (see Reading an Entire File
# later in this chapter for more info)
  file.close()
else:
  print ("Error Opening File.")
#Open a file for writing
  file = open(outPath, 'wb')
if file:
# write to file here (see Writing a File later
# in this chapter for more info)
  file.close()
else:
  print ("Error Opening File.")

#read file 
filePath = "input.txt"
#Read entire file into a buffer
buffer = "Read buffer:\n"
buffer += open(filePath, 'rU').read()
print (buffer)
#Read lines into a buffer
buffer = "Readline buffer:\n"
inList = open(filePath, 'rU').readlines()
print (inList)
for line in inList:
  buffer += line
print (buffer)
#Read bytes into a buffer
buffer = "Read buffer:\n"
file = open(filePath, 'rU')
while(1):
    bytes = file.read(5)
    if bytes:
      buffer += bytes
    else:
      break
      print (buffer)