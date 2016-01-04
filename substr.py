input('prompt')
searchStr = "Red Blue Violet Green Blue Yellow Black"
print ("%s" %  searchStr.find("Red"))
print (format(searchStr.rfind("Blue")))
question = "What is the air speed velocity of an unlaiden swallow?"
print (question)
#遍历指定格式的文件
import os
for f in os.listdir('/home/'):
  if f.endswith('.py'):
    print ("Python file: " + f)
  elif f.endswith('.txt'):
    print ("Text file: " + f)

import string
badSentence = "\t\tThis sentence has problems.     "
badParagraph = "\t\tThis paragraph \nhas even \more \nproblems.!?"

#Strip trailing spaces
print ("Length = " + str(len(badSentence)))
print ("Without trailing spaces = " +  str(len(badSentence.rstrip(' '))))

#Strip tabs
print ("\nBad:\n" + badSentence)
print ("\nFixed:\n" + badSentence.lstrip('\t'))

#print searchStr.find("Blue")
#print searchStr.find("Teal")
#print searchStr.index("Blue")
#print searchStr.index("Blue",20)
#print searchStr.rindex("Blue")
#print searchStr.rindex("Blue",1,18)

#format
chapters = {1:5, 2:46, 3:52, 4:87, 5:90}
hexStr = "3f8"
#Right justif           方向对齐
print ("Hex String: " + hexStr.upper().rjust(8,'0'))
print
for x in chapters:
  print ("Chapter " + str(x) + \
    str(chapters[x]).rjust(15,'.'))
#Left justify
print ("\nHex String: " + hexStr.upper().ljust(8,'0'))
#String format
for x in chapters:
  print ("Chapter %d %15s" % (x,str(chapters[x])))

import string
values = [5, 3, 'blue', 'red']
s = string.Template("Variable v = $v")
for x in values:
  print (format(s.substitute(v=x)))