## Python backend
import resources
import os


def main():
    dbName="contacts"
    tblName="names"
    field1="first"
    field2="last"
    keepDb=1
    
# Use Try / Catch while using file usage.
        
    resources.Database.create(dbName,tblName,field1,field2,keepDb)
    
    record1=("Boo","Hoo")
    resources.Database.add_record(dbName,tblName,field1,field2,record1)
    
    print("end of line")


if __name__ == '__main__':
    main()

