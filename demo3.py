import sys # Used for the sys.exit function
target_int = input("How many integers? ")
try:
  target_int = int(target_int)
except ValueError:
  sys.exit("You must enter an integer")

ints = list()


count = 0
# Keep asking for an integer until we have the required number
while count < target_int:
  new_int = input("Please enter integer {0}: ".format(count + 1))
isint = False
try:
  new_int = int(new_int)
except:
  print("You must enter an integer")
# Only carry on if we have an integer. If not, we’ll loop again
# Notice below I use ==, which is diff erent from =. The single equals is an
# assignment operator whereas the double equals is a comparison operator.
if isint == True:
# Add the integer to the collection
  ints.append(new_int)
# Increment the count by 1
  count += 1


  print("Using a for loop")
for value in ints:
  print(str(value))
# Or with a while loop:
  print("Using a while loop")
# We already have the total above, but knowing the len function is very
# useful.
  total = len(ints)
  count = 0

while count < total:
  print(str(ints[count]))
count += 1