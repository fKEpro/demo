#my_artists = {"Sarah Brightman", "Guns N' Roses","Opeth", "Vixy and Tony"}
#auburns_artists = {"Nickelback", "Guns N' Roses", "Savage Garden"}
#print("All: {}".format(my_artists.union(auburns_artists)))
#print("Both: {}".format(auburns_artists.intersection(my_artists)))
#print("Either but not both: {}".format(
#my_artists.symmetric_difference(auburns_artists)))

#my_artists = {"Sarah Brightman", "Guns N' Roses",
#"Opeth", "Vixy and Tony"}
#bands = {"Guns N' Roses", "Opeth"}
#print("my_artists is to bands:")
#print("issuperset: {}".format(my_artists.issuperset(bands)))
#print("issubset: {}".format(my_artists.issubset(bands)))
#print("difference: {}".format(my_artists.difference(bands)))
#print("*"*20)
#print("bands is to my_artists:")
#print("issuperset: {}".format(bands.issuperset(my_artists)))
#print("issubset: {}".format(bands.issubset(my_artists)))
#print("difference: {}".format(bands.difference(my_artists)))
#集合


#all of the items in the argument

#s.issubset(t) and t.issuperset(s) are identical. 
#They will both return True if t contains all the elements in s .


from collections import KeysView, ItemsView, ValuesView
class DictSorted(dict):
  def __new__(*args, **kwargs):
    new_dict = dict.__new__(*args, **kwargs)
    new_dict.ordered_keys = []
    return new_dict
  def __setitem__(self, key, value):
    '''self[key] = value syntax'''
    if key not in self.ordered_keys:
      self.ordered_keys.append(key)
      super().__setitem__(key, value)
  def setdefault(self, key, value):
    if key not in self.ordered_keys:
      self.ordered_keys.append(key)
      return super().setdefault(key, value)
  def keys(self):
      return KeysView(self)
  def values(self):
      return ValuesView(self)
  def items(self):
      return ItemsView(self)
  def __iter__(self):
      '''for x in self syntax'''
      return self.ordered_keys.__iter__()

ds = DictSorted()
d = {}
ds['a'] = 1
ds['b'] = 2
print (ds.setdefault('c',3))
for k,v in ds.items():
    print(k,v)
    #versatile多功能
    队列
    堆栈
    堆
    