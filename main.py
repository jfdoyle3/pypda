## Python backend
##----------------
## Uncomment here the LCD Display
## and resources/init.py
## To enable Display


import resources
import os
import time


def main():
    dbName = "contacts"
    tblName = "names"
    field1 = "first"
    field2 = "last"
    keepDb = 1

    # Initalize LCD Display
    # lcd = resources.LCD(2, 0x27, True)

    # User Input
    menu = input("1) Add\n2) Read Record\n")
    
    if menu=="1":
        print("input record")
    if menu=="2":
        print("read record")
    fname=input("first: ")
    lname=input("last: ")
    
    print (f"{fname}, {lname}")

    # Use Try / Catch while using file usage.

    #  Create Database
    # resources.Database.create(dbName, tblName, field1, field2, keepDb)

    # Add / Insert Record
    
    #resources.Database.add_record(dbName, tblName, field1, field2, record1)

    # Read Database
    # resources.Database.read_record(dbName, tblName)

    # Output to LCD Display
    #    lcd.message(" record recorded")
    #    time.sleep(10)
    #    lcd.clear()

    # End of Line
    print("end of line")


if __name__ == "__main__":
    main()
