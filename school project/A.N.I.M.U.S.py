
#A SOFTWARE WHICH MAKES YOU TO DO POSSIBLE OPERATIONS IN A SINGLE PLATFORM
#best software for  logical operations
#_-=-=-=-=-=-A.N.I.M.U.S-=-=-=-=-===
#CREATOR-
#PRODUCT KEY - 458557
print("welcome to^^^^^^^A.N.I.M.U.S software^^^^^^^^^^^^")
print("version 4.5v3")
print("compiling all resources***********************************************")
print("processing///...")
print("please wait")
print("loading the assets")
import time
x = 0
while x<=4:
    x+=1
    time.sleep(0.300)
    print(x)
    pass
print("75%completed ------------------------------------------")
print("\t\t\t","A.N.I.M.U.S")
print("\t\t\t","       **      ")
time.sleep(0.300)
print("\t\t\t",  "**    **    **")
time.sleep(0.300)
print("\t\t"," **  **    **   **  **  **")
time.sleep(0.300)
mk = input("enter your name-")
print("welcome",mk,"boss")
df =input("enter your location-")
print("location confirmed")
sj = input("how are you ?  -")
if sj==("fine")or sj==("FINE"):
    print("you are capable for using the program")
else:
    print("it seems that you are not fine today")
    print("come tomorrow")
    print("restart  the application")
    print("quit")
    quit()
print("1.VERIFIATION COMPLETED.................")
print("loading today details____________________")
print("________________________________________________________________________________________________________________")

print("today date $ time")
from datetime import datetime
now = datetime.now()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
print(mm + "/"+ dd +"/"+yyyy+"   "+ hour+":"+mi+":"+ss)
import time
y = 0
while y<=3:
    y+=1
    time.sleep(1)
    print(y)
    pass
kl = int(input("enter your age to verify:-"))
if kl >40:
    print("you are right to us me")
elif kl>15 and kl<=40:
    print("command accepted")
    print("processing for next steps")
elif kl==("5") and kl==("14"):
    print("teenager!!!")
    print("command accepted")
    print("processing for next steps")
else:
    print("sorry!!!A.N.I.M.U.S restriction")
    print("this program not made for you")
    print("quit the application or i will destroy in 10 seconds")
    print("\t\t\t","       **      ")
    time.sleep(5)
    print("\t\t\t",  "**    **    **")
    time.sleep(5)
    print("\t\t"," **  **    **   **  **  **")
    time.sleep(5)
    quit()
print("\t\t\t\, A.N.I.M.U.S")
wd= input("enter your nickname-")
print("hello",wd,"smart")
qw = input("enter the product key-")
if qw==("458557"):
    print("command excuted")
    print("you are allowed")
else:
    print("error345@#")
    print("invalid answer")
    print("quit")
    quit()
print("synchronized 100%")
print("$%$^&&%$^&")
print("\t\t\t","ALL TYPES OF CODES")
print("_____________________________________________________________________________________________________________")
#________________________________________________________________________________________________________________
choice = 0
ch ="y"
#the display menu function
while(ch == "y"):
    print("select your options given below")
    print("__________________________________________________________________________________________________________")
    print("1.CARDS YOU MUST HAVE")
    print("2.GUESS ME IF YOU CAN")#ONCE YOU SELECT THIS ONE THEN YOU CAN'T EXIT
    print("3.3D GAME")
    print("4.GUESS ME IF YOU CAN PART-2")
    print("5.callender")
    print("6.PROGRAM TO CALCULATE ELECTRCITY BILL")
    print("7.MAGIC BALLS")
    print("8.FARENHEIT to CELSIUS CONVERTER")
    print("9.KILOMETRE TO METRE PERSECOND CONVERTER")
    print("10.QUIT()")
    choice = int(input("enter your choice:"))



    
    if (choice == 1):
        # Python program to shuffle a deck of card
        # importing modules
        import itertools, random
        # make a deck of cards
        deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
        # shuffle the cards
        random.shuffle(deck)
        # draw five cards
        print("You got:")
        for i in range(5):
            print(deck[i][0], "of", deck[i][1])
            
            
    elif (choice == 2):
        import guessme

        
    elif (choice == 3):
        import GAME3D
        
        
    elif (choice == 4):
        import game3
        
    elif (choice == 5):

        
        # Program to display calendar of the given month and year
        # importing calendar module
        import calendar
        yy = 2020  # year
        mm = 1    # month
        # To take month and year input from the user
        # yy = int(input("Enter year: "))
        # mm = int(input("Enter month: "))
        # display the calendar
        print(calendar.month(yy, mm))
    elif (choice == 6):
    
        
        #program for calculating electricity bill in Python
        units=int(input("please enter the number of units you consumed in a month:-"))
        if(units<=100):
            payAmount=units*1.5
            fixedcharge=25.00
        elif(units<=200):
            payAmount=(100*1.5)+(units-100)*2.5
            fixedcharge=50.00
        elif(units<=300):
            payAmount=(100*1.5)+(200-100)*2.5+(units-200)*4
            fixedcharge=75.00
        elif(units<=350):
            payAmount=(100*1.5)+(200-100)*2.5+(300-200)*4+(units-300)*5
            fixedcharge=100.00
        else:
            payAmount=0
            fixedcharge=1500.00
        Total=payAmount+fixedcharge;
        print("\nElecticity bill=%.2f" %Total)
    elif(choice == 7):
        import magicb#ONCE YOU SELECT THIS ONE YOU CANNOT GO TO OTHER CODES


        
    elif (choice == 8):
        Fahrenheit = int(input("Enter a temperature in Fahrenheit: "))
        Celsius = (Fahrenheit - 32) * 5.0/9.0
        print ("Temperature:", Fahrenheit, "Fahrenheit = ", Celsius, " C")

 
    elif(choice == 9):
        kmp = 0.621371192 
        kmh = int(input("Enter km/h: "))
        mph =  0.6214 * kmh
        print ("Speed:", kmh, "KM/H = ", mph, "MPH")


        
    elif(choice ==10):
        print("quit")
        print("\t\t\t","destroying in 0.1 seconds ")
        print("\t\t\t","A.N.I.M.U.S")
        import time
        z = 0
        while z<=9:
         z+=1
        time.sleep(1)
        print(z)
        pass
        quit()
    
        




        
        

        
         
 
