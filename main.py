## Python backend
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
    fname=input("first: ")
    lname=input("last: ")
    
    if fname=="" & lname=="":
	record1 = ("Boo", "Hoo")
    else:
        record1=(fname,lname)

    # Use Try / Catch while using file usage.

    #  Create Database
    # resources.Database.create(dbName, tblName, field1, field2, keepDb)

    # Add / Insert Record
    
      resources.Database.add_record(dbName, tblName, field1, field2, record1)

    # Read Database
    resources.Database.read_record(dbName, tblName)

    # Output to LCD Display
    #    lcd.message(" record recorded")
    #    time.sleep(10)
    #    lcd.clear()

    # End of Line
    print("end of line")


if __name__ == "__main__":
    main()
