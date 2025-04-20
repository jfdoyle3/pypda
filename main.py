## Python backend
import resources
import os
import time
# from LCD import LCD

def main():
    dbName="contacts"
    tblName="names"
    field1="first"
    field2="last"
    keepDb=1
    
    lcd=resources.LCD(2,0x27,True)
# Use Try / Catch while using file usage.
    
    
    resources.Database.create(dbName,tblName,field1,field2,keepDb)
    
    record1=("Boo","Hoo")
    resources.Database.add_record(dbName,tblName,field1,field2,record1)
    lcd.message(" record recorded")
    time.sleep(10)
    lcd.clear()
    print("end of line")


if __name__ == '__main__':
    main()





