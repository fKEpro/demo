
# csv

import csv

# reading csv file
with open('customers.csv', newline='') as csv_file:
    customers = csv.reader(csv_file, delimiter=',')
    for row in customers:
        print(', '.join(row))
csv_file.close()

print('------------')
# reading csv file with handling header
with open('customers.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['id'], row['full_name'], row['age'], row['country'])
csv_file.close()


# writing csv file
print('----------------')
print('writing csv file')
with open('cities.csv', 'w') as csv_file:
    fieldnames = ['id', 'name', 'country']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')

    writer.writeheader()
    for i in range(1,10):
        writer.writerow({'id': i, 'name': "city " + str(i), 'country': "country " + str(i)})

csv_file.close()
print('done')

