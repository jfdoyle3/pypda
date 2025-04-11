## CSV Class

import csv
with open('.\contacts\contacts-melissa-name.csv', newline='') as csvfile:
 contacts = csv.reader(csvfile, delimiter=',')
next(contacts) # Skips headers
for row in contacts:
    print(', '.join(row))
