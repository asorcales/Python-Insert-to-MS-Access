import pyodbc
import os
 
def printOperation():
    printLine();
    print('       Choose School ID Operation')
    printLine();
    print('1. Add Another Record\n')
    print('2. Search All\n')
    print('3. Search one Record\n\n')

def printLine():
    print('------------------------------------------------------')


def AddNewRecord():

    #conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\IT\Documents\Database2.accdb;UID=username;PWD=Password;')
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\IT\Documents\Database2.accdb;')
    cursor = conn.cursor()

    print ('###############################################################################\n')

    LastName = input(" Please input your Last Name: ")

    print ('###############################################################################\n')

    FirstName = input(" Please input your First Name: ")

    print ('###############################################################################\n')

    Gender = input(" Please input your Gender: ")

    print ('###############################################################################\n')


    # Insert New Personal Information 
    #cursor.execute("Select ID, FirstName, LastName From Contacts WHERE FirstName = 'Liezl' ")
    #cursor.execute("Insert into Contacts(LastName,FirstName,Gender) values ('Bigboy', 'Dela Cruz', 'Male')")
    cursor.execute("Insert into Contacts(LastName,FirstName,Gender) values (?,?,?)", [LastName, FirstName, Gender])


#sql="""INSERT INTO STAFF(FIRST_NAME) VALUES('%/s')""" % STAFF_First


    cursor.commit()

    print('Personal Information Successfully Saved')

printOperation();
         
while True:
        operation = input('Enter operation 1:Add 2: Search All 3: Search per record:  ')
        if operation == '1':
            printLine();
            print('\t1. Add New Personal Information')
            printLine();
            AddNewRecord();
            os.system('cls')
            #break
        elif operation == '2':
            printLine();
            print('\t2. COUNT CHARACTER')
            printLine();
            break
        elif operation == '3':
            printLine();
            print('\t3. PERCENTAGE OF CHARACTER')
            printLine();
            break
        else:
            print('Invalid input!')


    

#except:

 #   print('Personal Information not Saved')

 
#for row in cursor.fetchall():
 #   print (row.ID, row.LastName)
