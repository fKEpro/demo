# ch16_01.py
# regular expression


import re

# pattern for numbers
p = re.compile('^[0-9]+$')
print(p.match('19023'))
print(p.match('0000'))
print(p.match('12.789'))
print(p.match('12b23'))

# search
message = 'Anna William <anna@email.com>'
match = re.search(r'[\w.-]+@[\w.-]+', message)
if match:
    print(match.group())


# search and replase
message = 'aaa : asasasw :: sasas:::'
p = re.compile('(:|::|:::)')
resutl = p.sub('<>', message)
print(resutl)

