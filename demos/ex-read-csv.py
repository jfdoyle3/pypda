## Python backend
import csv
with open('.\contacts\contacts-melissa.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print(', '.join(row))
