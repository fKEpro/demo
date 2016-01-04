
# json

import json
import time


# construct json
data = {
    'name': 'anna',
    'sex': 'woman',
    'age': 20,
    'country': 'germany'
}
blog = {
    'title': 'my blog',
    'created': time.time(),
    'comments': [
        {'name':'user 1', 'comment': 'this is comment 1'},
        {'name':'user 2', 'comment': 'this is comment 2'},
        {'name':'user 3', 'comment': 'this is comment 3'}
    ]
}

# json object to json string
json_data = json.dumps(data)
json_data2 = json.dumps(blog)
print(json_data)
print(json_data2)

# decode json string to json object
# you define json string or load json string from file
json_o1 = json.loads(json_data)
json_o2 = json.loads(json_data2)

# iteration json values
print('----json_o1---')
print(json_o1['name'])
print(json_o1['sex'])
print(json_o1['age'])
print(json_o1['country'])

print('----json_o2---')
print(json_o2['title'])
created_s = time.strftime("%b %d %Y %H:%M:%S", time.gmtime(json_o2['created']))
print(created_s)
print('comments:')
for comment in json_o2['comments']:
    print('---',comment['name'],':',comment['comment'])


