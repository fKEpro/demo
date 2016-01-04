numbers = ('1','2','3','4','5','6','7','8','9','0')

letters = ('a','b','c','d','e','f')

punct = ('.', '!', '?')

charSetDict = {numbers:[], letters:[], punct:[]}

def display_cset (cset):

  for x in cset.items():
    
    if x[0] == numbers:
      
      print ("Numbers:")
      
    elif x[0] == letters:
      
      print ("Letters:")
      
    elif x[0] == punct:
      
      print ("Puctuation:")
      
    else:
      
      print ("Unknown:")
      
      print (x[1])

#Add new values to keys

cSet = input("Insert characters: ")

for c in cSet:
  
  for x in charSetDict.keys():
    
    if c in x:
      
      charSetDict[x].append(c)
      
      break;


display_cset(charSetDict)

#Add new key and value

charSetDict["Special"] = ['%', '$', '#']

display_cset(charSetDict)

#Change value for existing key

charSetDict["Special"] = '><'

display_cset(charSetDict)


validkeys = (1,2,3)
keyGenDict={'keys':[1,2,3],1:'blue',2:'fast',3:'test','key':2}
print (keyGenDict.keys())
print (keyGenDict.values())


validkeys = (1,2,3)
keyGenDict={'keys':[1,2,3],1:'blue',2:'fast',
3:'test','key':2}
def show_key (key):
  if(key in validkeys):
    keyVal = (keyGenDict["keys"])[key-1]
    print ("Key = " + keyGenDict[keyVal])
  else:
      print("Invalid key")
#Retrieving dictionary key list
      print (keyGenDict.keys())
#Retrieving dictionary value list
      print (keyGenDict.values())
#Retrieving dictionary key and value list
      print (keyGenDict.items())
#Retrieve value from key
val = keyGenDict["key"]
show_key(val)
keyGenDict["key"] = 1
val = keyGenDict["key"]
show_key(val)

myDictionary = {'color':'blue', 'speed':'fast','number':1, 5:'number'}
print (myDictionary)
#Swap keys for values
swapDictionary = {}
for key, val in myDictionary.items():
  swapDictionary[val] = key
  print (swapDictionary)