## Database Manager
import sqlite3
import os

class Database:
    def __init__(self,dbName,tblName,field1,field2,keepDb):
        self.dbName=dbName
        self.tblName=tbleName
        self.field1=field1
        self.field2=field2
        self.keepDb=keepDb

    def create(dbName,tblName,field1,field2,keepDb):
        
        # Check DB exists and option to keep or destroy and renew DB
        path = f'{dbName}.db'

        if not os.path.exists(path) and keepDb==1:
            keepDb=2
            db = open(f"{dbName}.db", "w+")
            
        if keepDb==1:
            return
        elif keepDb==0:
            os.remove(path)
            db = open(f"{dbName}.db", "w+")

        # Create Table and Fields
        conn = sqlite3.connect(f'{dbName}.db')        
        cur = conn.cursor()

        cur.execute(f"DROP TABLE IF EXISTS {tblName}")

        table = f"""CREATE TABLE {tblName} (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            {field1} CHAR(25) NOT NULL,
                            {field2} CHAR(25)
                            );"""

        cur.execute(table)

        print("Table is Ready")

        conn.close()
        db.close()

    def add_record(dbName,tblName,field1,field2,record):

        conn = sqlite3.connect(f'{dbName}.db')
        
        sql = f''' INSERT INTO {tblName} ({field1},{field2})
                  VALUES(?,?) '''
        
        cur = conn.cursor()

        cur.execute(sql,record)

        conn.commit()
        
        print(f"record: {cur.lastrowid} inserted")
        
        conn.close() 