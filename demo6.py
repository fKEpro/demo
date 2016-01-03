class Person:
  def __init__(self, name):
    
    self.name = name
    
  def sayHi(self):
    
    print ('Hello, my name is', self.name)
    
p = Person('Kunal')

p.sayHi()
#dir(模块)列出模块中所有函数

