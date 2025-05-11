## Database Manager
import sqlite3
import os


class Database:
    def __init__(self, dbName, tblName, field1, field2):
        self.dbName = dbName
        self.tblName = tbleName
        self.field1 = field1
        self.field2 = field2
        
    def createDb(dbName):

        # Check DB exists and option to keep or destroy and renew DB
        path = f"{dbName}.db"
        db = open(f"{dbName}.db", "w+")

        print("file is Ready")
        
    def genTables(dbName, tblName, field1, field2):

        # Create Table and Fields
        conn = sqlite3.connect(f"{dbName}.db")
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

    def addRecord(dbName, tblName, field1, field2, record):

        conn = sqlite3.connect(f"{dbName}.db")

        sql = f""" INSERT INTO {tblName} ({field1},{field2})
                  VALUES(?,?) """

        cur = conn.cursor()

        cur.execute(sql, record)

        conn.commit()

        print(f"record: {cur.lastrowid} inserted")

        conn.close()

    def allRecords(dbName, tblName):

        conn = sqlite3.connect(f"{dbName}.db")

        cur = conn.cursor()

        sql = f"""SELECT * FROM {tblName} """

        cur.execute(sql)

        rows = cur.fetchall()
        

        conn.close()
        return rows

    def oneRecord(dbName, tblName, record):

        conn = sqlite3.connect(f"{dbName}.db")

        cur = conn.cursor()

        sql = f"""SELECT * FROM {tblName} """

        cur.execute(sql)

        rows = cur.fetchall()

        for row in rows:
            print(row)

        conn.close()

    def displayAllRecords(dbName, tblName):

        conn = sqlite3.connect(f"{dbName}.db")

        cur = conn.cursor()

        sql = f"""SELECT * FROM {tblName} """

        cur.execute(sql)

        rows = cur.fetchall()

        for row in rows:
            print(row)

        conn.close()
