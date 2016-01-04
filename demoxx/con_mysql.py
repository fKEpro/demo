
# database mysql
# mysql driver for python
# https://dev.mysql.com/downloads/connector/python/
# sudo pip3 install --allow-external mysql-connector-python mysql-connector-python


import mysql.connector
from datetime import datetime


def create_data(conn):
    cursor = conn.cursor()
    print('inserting data...')
    for i in range(1,5):
        insert_product = ("INSERT INTO product "
                   "(name, code, price, quantity, created) "
                   "VALUES (%s, %s, %s, %s, %s)")
        data_product = ("product " + str(i), "F029" + str(i), i*0.21, i, datetime.now())
        cursor.execute(insert_product, data_product)
        product_id = cursor.lastrowid
        print('inserted with id=',product_id)

    conn.commit()
    cursor.close()
    print('done')


def read_data(conn):
    print('reading data....')
    selected_id = 0
    cursor = conn.cursor()
    query = "SELECT idproduct, name, code, price, quantity, created FROM product"
    cursor.execute(query)
    for (id, name, code, price, quantity, created) in cursor:
        print("{}, {}, {}, {}, {}, {:%d %b %Y %H:%M:%S}".format(
                id, name, code, price, quantity, created))
        if selected_id <= 0:
            selected_id = id

    cursor.close()
    print('done')

    return selected_id


def update_data(conn, id):
    print('updating data with idproduct=', id, '...')
    cursor = conn.cursor()
    query = "UPDATE product SET name=%s, code=%s, price=%s, quantity=%s, created=%s where idproduct=%s"
    name = 'updated-name'
    code = 'F9999'
    price = 0.99
    quantity = 10
    created = datetime.now()
    cursor.execute(query, (name, code, price, quantity, created, id))
    conn.commit()
    cursor.close()
    print('done')


def delete_data(conn, id):
    print('deleting data on idproduct=', id, '...')
    cursor = conn.cursor()
    query = "DELETE FROM product where idproduct = %s "
    cursor.execute(query, (id,))
    conn.commit()
    cursor.close()
    print('done')


def delete_all(conn):
    print('deleting all data....')
    cursor = conn.cursor()
    query = "DELETE FROM product"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    print('done')


print('connecting to mysql server...')
cnx = mysql.connector.connect(user='pyuser',
                              password='password123',
                              host='127.0.0.1',
                              database='pydb')
print('connected')

create_data(cnx)
selected_id = read_data(cnx)
update_data(cnx, selected_id)
read_data(cnx)
delete_data(cnx, selected_id)
read_data(cnx)
delete_all(cnx)

cnx.close()
print('closed connection')

