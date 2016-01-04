class WeirdSortee:
  def __init__(self, string, number, sort_num):
     self.string = string
     self.number = number
     self.sort_num = sort_num
  def __lt__(self, object):
    if self.sort_num:
      return self.number < object.number
      return self.string < object.string

  def __repr__(self):
    return"{}:{}".format(self.string, self.number)



a = WeirdSortee('a',4,True)
b = WeirdSortee('b',4,True)
c = WeirdSortee('d',100,True)
d = WeirdSortee('c',4,True)
l = [a,b,c,d]
l.sort()
print (l)

l = ["hello","HJDAD","Hdasjd"]
l.sort()
l
print(l)

from operator import itemgetter

l = [('h', 4), ('n', 6), ('o', 5), ('p', 1), ('t', 3), ('y', 2)]

l.sort(key=itemgetter(1))

print(l)
#将值设为键 按值排序



