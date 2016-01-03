
# Below is a function called modify_string,
# that will be called original in the scope
# indented with 4 spaces under the function
# scope.
def modify_string(original):
  original += " that has been modified."

def modify_string_return(original):
  original += " that has been modified."
# However, we can return our local copy to the caller. The function
# ends as soon as the return statement is used, regardless of where it
# is in the function.
  return original
test_string = "This is a test string"
modify_string(test_string)
print(test_string)
test_string = modify_string_return(test_string)
print(test_string)
#如果可迭代对象为空则all函数的返回值为True
#any相反
#memoryview 查看对象在内存中的地址
