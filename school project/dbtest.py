import mysql.connector as msqlcon

mydb = msqlcon.connect(
        host = "localhost",
        user = "root",
        password = "12345678",
        database = "manoj"
    )
cont = 1
mycursor = mydb.cursor()
while cont == 1:
    student_name = input("Please Enter Your Name : ")
    clas = input("Please Enter Your class : ")
    section = input("Please Enter Your section : ")
student_class = clas+section

    #Inserting Data into MySQl 
sql = "INSERT INTO students (name, class) VALUES (%s, %s)"
val = (student_name, student_class)
mycursor.execute(sql, val)

mydb.commit()


    #Printing out data from MySQL
mycursor.execute("SELECT * FROM students")

myresult = mycursor.fetchall()
for x in myresult:
    print(x)
    


try_again = input("Insert Another Data(y/n) : ")

if try_again == 'n':
    cont = 0
if try_again == 'y':
    cont = 1
else:
    print("incorrect value")
        
  

    
