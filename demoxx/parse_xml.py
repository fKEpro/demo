# ch12_04.js
# xml

import xml.etree.ElementTree as Et

# load xml file and iterate
xml_tree = Et.parse('products.xml')
products = xml_tree.getroot()
print(products.tag)
for product in products:
    print(' ',product.tag, ' name=',product.get('name'))
    for product_item in product:
        print('   ',product_item.tag, '=',product_item.text)

# finding specific data
print('----------')
for code in products.iter('code'):
    print(code.text)

# construct xml and save into a file
print('construct xml file')
users = Et.Element('users')
for i in range(1, 5):
    user = Et.SubElement(users, 'user')
    user.set('name', "User " + str(i))

    user_item = Et.SubElement(user, 'age')
    user_item.text = str(i * 3)

    user_item2 = Et.SubElement(user, 'id')
    user_item2.text = "1203" + str(i)


print('write into xml file')
tree = Et.ElementTree(users)
tree.write("users.xml")
