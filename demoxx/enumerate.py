import sys
filename = sys.argv[0]
with open(filename) as file:
  for index, line in enumerate(file):
    print("{0}: {1}".format(index+1, line), end='')
print("\n")


contents = "Some file contentsdksakjdklsfsad\nnsnfdjsfkdsf\ndjsjdskjdksjds\n\
dhdhhhhjdhsjdhjs"
file = open("filename", "w")
file.write(contents)
file.close()