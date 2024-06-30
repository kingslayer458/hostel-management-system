import time
import pandas as pd
import mysql.connector
py=mysql.connector.connect(host='localhost',user='satyac',passwd='dbzsuperNo.1',database='Hotel')
mycursor=py.cursor()
#mycursor.execute('create table val (name varchar(40), phone varchar (10), mail varchar(2020), Total varchar(40))')
#mycursor.execute('ALTER TABLE vals ADD Total varchar(50)')  
total=0
while (1):
    print("1.Enter Customer Data")
        
    print("2.Calculate Room Rent")

    print("3.Calculate Food Purchased")

    print("4.Show total cost")

    print("5.EXIT")

    b=int(input("\nEnter the number of your choice:"))
    if (b==1):
        cont=1
        while cont==1:
            Hotel_name=input('Enter your name here:')
            time.sleep(1)
            Hotel_phno=int(input('Enter your phone no. here:'))
            time.sleep(1)  
            Hotel_mail=input('Enter your email-id here:')
            time.sleep(1)
            pd='INSERT INTO vals (name,phone,mail) VALUES(%s,%s,%s)'
            vs=(Hotel_name,Hotel_phno,Hotel_mail)
            mycursor.execute(pd,vs)
            py.commit()
            try_again=input('Insert another Data?(y/n):')
            if try_again=='y' or try_again=='Y':
                cont=1
            elif try_again=='n' or try_again=='N':
                cont=2
            else:
                print('Invalid input')
            mycursor.execute('SELECT * FROM val')
            myresult=mycursor.fetchall()
            for i in myresult:
                print(i)
        
    if (b==2):
        price=1
        print ("We have the following rooms for you:-")

        print ("1.  Class A---->4000")

        print ("2.  Class B---->3000")

        print ("3.  Class C---->2000")

        print ("4.  Class D---->1000")
        time.sleep(1)

        x=int(input("Enter the number of your choice Please->"))
        time.sleep(1)

        n=int(input("For How Many Days Do Wish To Stay:"))

        if(x==1):
            time.sleep(1)

            print ("you have chosen room Class A")

            price=4000*n

        elif (x==2):
            time.sleep(1)

            print ("you have chosen room Class B")

            price=3000*n

        elif (x==3):
            time.sleep(1)

            print ("you have chosen room Class C")

            price=2000*n

        elif (x==4):
            time.sleep(1)
            print ("you have chosen room Class D")

            price=1000*n

        else:

            print ("please choose a room")
        time.sleep(1)

        print ("Amount to be paid is:",price,"\n")
        total=total+price
        time.sleep(1)
        
    if (b==3):
        beil=1
        count=1
        while count==1:
            print("\t\t****WELCOME TO ABZ FOOD COURT****")
            menu={'FOOD':['Starters','Beverages','Breakfast','Lunch','Dinner','None'],
                           'PRICE':[100,50,150,300,250,'None']}
            beel=pd.DataFrame(menu, index=[1,2,3,4,5,6])
            print(beel)
            time.sleep(1)
            v=int(input('Enter the index:'))
            time.sleep(1)
            q=int(input('Enter Quantity:'))
            if v==1:
                time.sleep(1)
                print('You have ordered Starters')
                beil=beil+100*q
            elif v==2:
                time.sleep(1)
                print('You have ordered Beverages')
                beil=beil+50*q
            elif v==3:
                time.sleep(1) 
                print('You have ordered Breakfast')
                beil=beil+150*q
            elif v==4:
                time.sleep(1)
                print('You have ordered Lunch')
                beil=beil+300*q
            elif v==5:
                time.sleep(1)
                print('You have ordered Dinner')
                beil=beil+250*q
            elif v==6:
                time.sleep(1)  
                print('Thank you for Coming, Visit Again...')
                break;
            else:
                print('Appropriate option not selected...')
            time.sleep(1)      
            print('TOTAL FOOD COST:',beil,'Rs')
            a=input('Do you want to order again(y/n):')
            if a=='y' or a=='Y':
                count=1
            else:
                count=2
            total=total+beil
                
    if (b==4):
        print('\t\t\t****TOTAL BILL****')
        print('Total Bill is:',total)

        

    if (b==5):
        quit()









