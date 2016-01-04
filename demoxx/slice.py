monthList = ["January", "February", "March", "April", "May", "June", "July", \
"August", "September", "October","November", "December"]
wordCount = len(monthList)
halfCount = wordCount // 2
#Beginning slice 浮点型除法使用//
firstHalf = monthList[:halfCount]
print (firstHalf)
#End slice
secondHalf = monthList[halfCount : ]
print (secondHalf)
#Middle slice
wordCount = len(firstHalf)
middleStart = wordCount // 2
middleHalf = monthList[middleStart : middleStart+halfCount]
print (middleHalf)
#Negative Indices
print (monthList[-5 : -1])



