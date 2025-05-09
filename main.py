## Python backend
##----------------
## Uncomment here the LCD Display
## and resources/init.py
## To enable Display


import resources
import os
import time


def mockData(dbName, tblName, field1, field2, numRecords):
    totalRecords= len(resources.Database.allRecords(dbName, tblName))
    startEntry=++totalRecords
    lastEntry=startEntry+int(numRecords)
    for record in range(startEntry, lastEntry):
        record = ("record", str(record))
        resources.Database.addRecord(dbName, tblName, field1, field2, record)

def buildDb():
    dbName = "pdadb"
    tblName = {"contacts":["first","last"],
               "rpg":["first","last"],
               "password":["name","password"]
               }
    

    # resources.Database.create(dbName, tblName, field1, field2)       

def main():
    newDb = 0

    # Initalize LCD Display
    # lcd = resources.LCD(2, 0x27, True)

    if newDb == 0:
        buildDb()
    '''
    # User Input
    menu = input("Record:\n1) Add\n2) Fetch All Records\n3) Get one record\n")

    if menu == "1":
        numRecords = input("How many records to add: ")
        mockData(dbName, tblName, field1, field2, numRecords)
    elif menu == "2":
        resources.Database.displayAllRecords(dbName, tblName)
    elif menu == "3":
        print("Getting a record")
    else:
        print("invalid input")
    # Use Try / Catch while using file usage.

    #  Create Database

    # Read Database
    # resources.Database.read_record(dbName, tblName)

    # Output to LCD Display
    #    lcd.message(" record recorded")
    #    time.sleep(10)
    #    lcd.clear()
    '''
    # End of Line
    print("end of line")


if __name__ == "__main__":
    main()
