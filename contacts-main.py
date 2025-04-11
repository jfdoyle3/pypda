## Python backend
import resources
import os


def main():
    dbName="contacts"
    tblName="names"
    field1="first"
    field2="last"
    keepDb=0

 # Check if DB is already created.
#     path = f'{dbName}.db'
#     
#     if not os.path.exists(path):
#          db = open(f"{dbName}.db", "w+")
#          print("new db created")
#     
#     if keepDb==1:
#         print("db data kept-closing - returning")
# 
#         
#     elif keepDb==0:
#         os.remove(path)
#         db = open(f"{dbName}.db", "w+")
#         print("db data reset")

        
    resources.Database.create(dbName,tblName,field1,field2,keepDb)
    
    record1=("Boo","Hoo")
    resources.Database.add_record(dbName,tblName,field1,field2,record1)
#     record2=("Boo","Hoo")
#     resources.Database.add_record(dbName,tblName,field1,field2,record2)
#     record3=("Boo","Boo")
#     resources.Database.add_record(dbName,tblName,field1,field2,record3)
    
    print("end of line")
#     
#     try:
#         with sqlite3.connect('contacts.db') as conn:
#             # add  a project
#             contact = ('first','last')
#             contact_id = add_contact(conn, contacts)
#             print(f'Created a project with the id {project_id}')
# 
# 
#     except sqlite3.Error as e:
#         print(e)

if __name__ == '__main__':
    main()



# try:
#    
#     
#     # Connect to DB and create a cursor
#     sqliteConnection = sqlite3.connect('.\db\contacts.db')
#     cursor = sqliteConnection.cursor()
#     print('DB Init')
#  
#     # Write a query and execute it with cursor
#     query = ''' INSERT INTO contacts(First_Name,Last_Name)
#               VALUES(?,?) '''
#     cursor.execute(query,contacts)
#     return cursor.lastrowid
#  
#     # Fetch and output result
#     result = cursor.fetchall()
#     print('Results---> '.format(result))
#  
#     # Close the cursor
#     cursor.close()
#  
# # Handle errors
# except sqlite3.Error as error:
#     print('Error occurred - ', error)
#  
# # Close DB Connection irrespective of success
# # or failure
# finally:
#    
#     if sqliteConnection:
#         sqliteConnection.close()
#         print('SQLite Connection closed')
