import pyttsx3
import os       
engine = pyttsx3.init('sapi5')               #-|
voices = engine.getProperty('voices')        # |
engine.setProperty('voice',voices[1].id)     # |
                                             # |->USING THIS COMMAND WILL LET YOUR PC TO TALK OR SPEAK TO YOU
def speak(audio):                            # |
    engine.say(audio)                        # |
    engine.runAndWait()

speak(" WELCOME USER")
print("\t\t\t\t\t W-E-L-C-O-M-E   U-S-E-R")
speak("I'm your virtusl assistant")
speak("version 4.5")
print("version 4.5v7")
speak("please wait till we compile all our resources")
print("compiling all resources***********************************************")
import time
time.sleep(2)


speak("processing")
print("processing///...")
speak("please wait")
import time
time.sleep(3)
print("please wait")
speak("Activating the main control head")
speak("setting an alternative connection ,  with alternative server  , nemesis")#product key-458557
print("loading all assets")
import time
time.sleep(2)
print("75%completed ------------------------------------------")
print("\t\t\t","A.N.I.M.U.S")
print("\t\t\t","       **      ")
time.sleep(0.300)
print("\t\t\t",  "**    **    **")
time.sleep(0.300)
print("\t\t"," **  **    **   **  **   **   **  **")
time.sleep(0.300)
mk = input("enter your name-")
speak(mk)
speak("welcome")
print("welcome",mk)
df =input("enter your location-")
speak(df)
speak("nice place")
print("location confirmed")

speak("how are you dear user")
rb=str(input("enter your statement:-"))




if rb == "fine":
    speak("wow")
    
elif rb == "good":
    speak("WOW! THAT'S really very good!")

elif rb =="hopeful":
    speak("BE hopeful in your life because, only hope can help u to , withstand with your certain conditions")

elif rb == "feeling sleepy":
    speak("go and take short nap of 30 minutes")

elif rb == "i am good":
    speak("wow! that's really very cool")

elif rb == "sad":
    speak("life sad hae bay!")

elif rb == "i am fine":
    speak("cool! bro., that's awesome,yaar")

elif rb == "i am well":
    speak("wowowow! that's awesome dude")

elif rb == "i am sad":
    speak("oh!!sorry to hear that!")
    if rb==rb:
        speak("don't be sad. this happens to , almost each and every person , in the society of young youth")
        speak("just enjoy your life, dont be a burden or take someone's burden")
        speak("remember  , you also have childhood , so be enjoyable , as you were in those days")

elif rb == "cool":
    speak("i often like to talk to those people , who are cool minded , and u r one of them")

elif rb == "well":
    speak("that's awesome")




print("1.VERIFICATION COMPLETED.................")
speak("VERIFICATION COMPLETED")
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
speak("today's date and time")
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
    print("your age is appropriate to operate  me")
    speak("Access accepted")
elif kl>15 and kl<=40:
    
    print("command accepted")
    print("processing for next steps")
elif kl==("11") and kl==("14"):
    
    print("teenager!!!")
    print("command accepted")
    print("processing for next steps")
else:
    print("ACCESS DENIED")
    print("quit the application ")

    
    print("\t\t\t","       **      ")
    time.sleep(5)
    print("\t\t\t",  "**    **    **")
    time.sleep(5)
    print("\t\t"," **  **    **   **  **  **")
    time.sleep(5)
    os.system("shutdown /s /t 1") 
    
print("\t\t\t HOTEL MANAGEMENT SYSTEM")

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
engine = pyttsx3.init('sapi5')               #-|
voices = engine.getProperty('voices')        # |
engine.setProperty('voice',voices[0].id)     # |
                                             # |->USING THIS COMMAND WILL LET YOUR PC TO TALK OR SPEAK TO YOU
def speak(audio):                            # |
    engine.say(audio)                        # |
    engine.runAndWait()

class hotelfarecal:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',address='',cindate='',coutdate='',rno=101):

        print ("\n\n*****WELCOME TO HEWING HOTEL*****\n")
        speak("Welcome to hewing hotel")

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
    def inputdata(self):
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter your check in date:")
        self.coutdate=input("\nEnter your checkout date:")
        speak("your room number")
        print("Your room no.:",self.rno,"\n")
        
    def roomrent(self):

        print ("We have the following rooms for you:-")

        print ("1.  type A---->rs 6000 PN\-")

        print ("2.  type B---->rs 5000 PN\-")

        print ("3.  type C---->rs 4000 PN\-")

        print ("4.  type D---->rs 3000 PN\-")
        speak("enter you choice please")

        x=int(input("Enter Your Choice Please->"))

        
        speak("For How Many Nights Did You Stay")


        n=int(input("For How Many Nights Did You Stay:"))
        

        if(x==1):

            speak("you have opted for room a")

            print ("you have opted room type A")
            

            self.s=6000*n

        elif (x==2):

            speak("you have opted for room b")

            print ("you have opted room type B")
            

            self.s=5000*n

        elif (x==3):
            speak("you have opted for room c")

            print ("you have opted room type C")
           

            self.s=4000*n

        elif (x==4):
            speak("you have opted for room d")
            print ("you have opted room type D")
        

            self.s=3000*n

        else:

            speak("please choose a room")

            print ("please choose a room")
            

        print ("your room rent is =",self.s,"\n")
        speak("your room rent ")

    def restaurentbill(self):
        speak("restaurant menu")

        print("*****RESTAURANT MENU*****")

        print("\n1.water----->Rs20","\n2.tea----->Rs10","\n3.breakfast combo--->Rs90","\n4.lunch---->Rs110","\n5.dinner--->Rs150","\n6.Exit")

 
        while (1):
            speak("enter your choice")

            c=int(input("Enter your choice:"))
            


            if (c==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+20*d

            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+10*d

            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+90*d

            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+110*d

            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+150*d

            elif (c==6):
                break;
            else:
                speak("invalid option")
                print("Invalid option")
                
                
        speak(" your Total food Cost")
        print ("Total food Cost=Rs",self.r,"\n")
        

    def	laundrybill(self):
        speak("laundry menu")
        print ("******LAUNDRY MENU*******")

        print ("\n1.Shorts----->Rs3","\n2.Trousers----->Rs4","\n3.Shirt--->Rs5","\n4.Jeans---->Rs6","\n5.Girlsuit--->Rs8","\n6.Exit")

        while (1):
            

            e=int(input("Enter your choice:"))

            if (e==1):
                f=int(input("Enter the quantity:"))
                self.t=self.t+3*f

            elif (e==2):
                f=int(input("Enter the quantity:"))
                self.t=self.t+4*f

            elif (e==3):
                f=int(input("Enter the quantity:"))
                self.t=self.t+5*f

            elif (e==4):
                f=int(input("Enter the quantity:"))
                self.t=self.t+6*f

            elif (e==5):
                f=int(input("Enter the quantity:"))
                self.t=self.t+8*f
            elif (e==6):
                break;
            else:

                print ("Invalid option")
                speak("invalid option")


        print ("Total Laundary Cost=Rs",self.t,"\n")
        speak("total laundary cost")


    def gamebill(self):
        print("******GAME MENU*******")
        speak("game menu")

        speak("games are listed below")
        print("\n1.Table tennis----->Rs60","\n2.Bowling----->Rs80","\n3.Snooker--->Rs70","\n4.Video games---->Rs90","\n5.Pool--->Rs50","\n6.Exit")



        while (1):
            speak("enter your choice")#USE CHOICE AS "6" TO AVOID FROM REPETITIVE OPTIONS

            
            g=int(input("Enter your choice:"))


            if (g==1):
                h=int(input("No. of hours:"))
                self.p=self.p+60*h

            elif (g==2):
                h=int(input("No. of hours:"))
                self.p=self.p+80*h

            elif (g==3):
                h=int(input("No. of hours:"))
                self.p=self.p+70*h

            elif (g==4):
                h=int(input("No. of hours:"))
                self.p=self.p+90*h

            elif (g==5):
                h=int(input("No. of hours:"))
                self.p=self.p+50*h

                print ("Total Game Bill=Rs",self.p,"\n")
            elif (g==6):
                break;

            else:

                print ("Invalid option")



        

    def display(self):
        print ("******HOSTEL BILL******")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.cindate)
        print ("Check out date",self.coutdate)
        print ("Room no.",self.rno)
        print ("Your Room rent is:",self.s)
        print ("Your Food bill is:",self.r)
        print ("Your laundary bill is:",self.t)
        print ("Your Game bill is:",self.p)

        self.rt=self.s+self.t+self.p+self.r

        print ("Your sub total bill is:",self.rt)
        print ("Additional Service Charges is",self.a)
        print ("Your grandtotal bill is:",self.rt+self.a,"\n")
        self.rno+=1

            

        

speak("given below is the list for calculating your bills")
speak("keep in your mind , only to type number")

def main():

    a=hotelfarecal()
    

    while (1):
        print("1.Enter Customer Data")
        
        print("2.Calculate rommrent")

        print("3.Calculate restaurant bill")

        print("4.Calculate laundry bill")

        print("5.Calculate gamebill")

        print("6.Show total cost")

        print("7.EXIT")

        b=int(input("\nEnter your choice:"))
        if (b==1):
            a.inputdata()

        if (b==2):

            a.roomrent()

        if (b==3):

            a.restaurentbill()

        if (b==4):

            a.laundrybill()

        if (b==5):

            a.gamebill()

        if (b==6):

            a.display()

        if (b==7):

            quit()



main()
