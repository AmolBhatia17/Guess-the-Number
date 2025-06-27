d={}
name=input("Enter Your Name")
import pickle
import random
import csv
from math import pow

def leaderboard():
        f=open("LEADERBOARD.csv","w",newline='')
        fields=["HIGH SCORE"]
        rows=[["Amol Bhatia","God Mode","70"],
              ["Amol Bhatia","Hard Mode","50"],
              ["Amol Bhatia","Medium Mode","60"],
              ["Amol Bhatia","Easy Mode","40"]]
        writer=csv.writer(f)
        writer.writerow(fields)
        for i in rows:
            writer.writerow(i)
        f.close()
        f=open("LEADERBOARD.csv","r")
        reader=csv.reader(f)
        for i in reader:
           print(i)
        f.close()
    
def store(n):
        f=open("GuessTheNumber.csv","a+",newline='')
        heading=["NAME","LUCK(%)","MODE"]
        reader=csv.reader(f)
        for row in reader:
            writer=csv.writer(f)
            if row[0]!="NAME":
                
                writer.writerow(heading)
        else:
            if int(X)==1:
                writer=csv.writer(f)
                stack=[name,n,"EASY MODE"]
                writer.writerow(stack)
                f.close()
            elif int(X)==2:
                writer=csv.writer(f)
                stack=[name,n,"MEDIUM MODE"]
                writer.writerow(stack)
                f.close()
            elif int(X)==3:
                writer=csv.writer(f)
                stack=[name,n,"HARD MODE"]
                writer.writerow(stack)
                f.close()
            elif int(X)==4:
                writer=csv.writer(f)
                stack=[name,n,"GOD MODE"]
                writer.writerow(stack)
                f.close()
            elif int(X)==5:
                writer=csv.writer(f)
                stack=["JAMES BOND","OO7","IMPLAUSIBLE MODE"]
                writer.writerow(stack)
                f.close()
            
def easypoint(lst_easy):
    pts=10
    for i in range(len(lst_easy)):
        pts-=3
    print("YOU HAVE A LUCK OF",(pts/10)*100,"%")
    return (pts/10)*100
def mediumpoint(lst_medium):
    pts=10
    for i in range(len(lst_medium)):
        pts-=2
    print("YOU HAVE A LUCK OF",(pts/10)*100,"%")
    return (pts/10)*100
def hardpoint(lst_hard):
    pts=10
    for i in range(len(lst_hard)):
        pts-=1
    print("YOU HAVE A LUCK OF",(pts/10)*100,"%")
    return (pts/10)*100
def godpoint(lst_god):
    pts=10
    if len(lst_god)==10:
        print("YOU HAVE A LUCK OF 0%")
        return (pts/10)*100
    else:
        for i in range(len(lst_god)):
                pts-=0.5
        print("YOU HAVE A LUCK OF",(pts/10)*100,"%")
        return (pts/10)*100

# UPDATION IN LEADERBOARD

def easy_update(name,p):
    f=open("LEADERBOARD.csv","w",newline='')
    fields=["HIGH SCORE"]
    rows=[["Amol Bhatia","God Mode","70"],
      ["Amol Bhatia","Hard Mode","50"],
      ["Amol Bhatia","Medium Mode","60"],
      [name,"Easy Mode",p]]
    writer=csv.writer(f)
    writer.writerow(fields)
    for i in rows:
        writer.writerow(i)
    f.close()
    f=open("LEADERBOARD.csv","r")
    reader=csv.reader(f)
    for i in reader:
           print(i)
    f.close()

def medium_update(name,p):
    f=open("LEADERBOARD.csv","w",newline='')
    fields=["HIGH SCORE"]
    rows=[["Amol Bhatia","God Mode","70"],
      ["Amol Bhatia","Hard Mode","50"],
      [name,"Medium Mode",p],
      ["Amol Bhatia","Easy Mode","40"]]
    writer=csv.writer(f)
    writer.writerow(fields)
    for i in rows:
        writer.writerow(i)
    f.close()
    f=open("LEADERBOARD.csv","r")
    reader=csv.reader(f)
    for i in reader:
           print(i)
    f.close()
def hard_update(name,p):
    f=open("LEADERBOARD.csv","w",newline='')
    fields=["HIGH SCORE"]
    rows=[["Amol Bhatia","God Mode","70"],
          [name,"Hard Mode",p],
          ["Amol Bhatia","Medium Mode","60"],
          ["Amol Bhatia","Easy Mode","40"]]
    writer=csv.writer(f)
    writer.writerow(fields)
    for i in rows:
        writer.writerow(i)
    f.close()
    f=open("LEADERBOARD.csv","r")
    reader=csv.reader(f)
    for i in reader:
        print(i)
    f.close()
def god_update(name,p):
    f=open("LEADERBOARD.csv","w",newline='')
    fields=["HIGH SCORE"]
    rows=[[name,"God Mode",p],
          ["Amol Bhatia","Hard Mode","50"],
          ["Amol Bhatia","Medium Mode","60"],
          ["Amol Bhatia","Easy Mode","40"]]
    writer=csv.writer(f)
    writer.writerow(fields)
    for i in rows:
        writer.writerow(i)
    f.close()
    f=open("LEADERBOARD.csv","r")
    reader=csv.reader(f)
    for i in reader:
        print(i)
    f.close()


while True:
    header=[]
    stack=[]
    lst_easy=[]
    lst_medium=[]
    lst_hard=[]
    lst_god=[]
    print()
    print('''                PRESS 1 FOR EASY LEVEL       [RANGE(1-50)]
                PRESS 2 FOR MEDIUM LEVEL     [RANGE(1-100)]
                PRESS 3 FOR HARD LEVEL       [RANGE(1-700)]
                PRESS 4 FOR GOD MODE         [RANGE(1-1500)]
                PRESS 5 FOR IMPLAUSIBLE MODE [""THE DEVELOPER
                                              FORGET TO MENTION THE RANGE
                                              TRY TO CRAKE THE PATTERN]""''') 
    print("PRESS 0 FOR INSTRUCTIONS")
    print("PRESS C FOR CREDITS")
    print("PRESS L FOR LEADERBOARD")
    X=input()
    if X.upper()=="C":
        print('''THIS GAME IS MADE BY 'AMOL BHATIA' IN PYTHON ''')
    elif X.upper()=="L":
            leaderboard()

    elif int(X)==1:#easy
        a=random.randint(1,50)
        for i in range(5,0,-1):
              num=int(input("Guess the Number"))
              if num==a:
                  print(name,"Won")
                  result=easypoint(lst_easy)
                  store(result)
                  if result>40:
                          p=result
                          easy_update(name,p)
                          print()
                          print("CONGRATULATIONS!!YOUR NAME IS IN THE LEADERBOARD")
                  else:
                          print("Amol Bhatia is undefeted")
                  break
                          
              elif num!=a:
                  if num>a:
                      print("Number is less than", num)
                      print(i-1 ,"TRIES REMAIN")
                      lst_easy.append(num)
                  elif num<a:
                      print("Number is Greater than",num)
                      print(i-1, "TRIES REMAIN")
                      lst_easy.append(num)
              if i==1:
                  print("NUMBER IS ",a)
                  print("GAME OVER BETTER LUCK NEXT TIME HEHE")
                  result=easypoint(lst_easy)
                  store(result)
                  print()
        retry=input(" WANT TO TRY AGAIN [Y/N]")
        if retry.upper()=="N":
            print('''THANK YOU FOR PLAYING
                    ~AMOL BHATIA''')
            break
    elif int(X)==2:#medium
        a=random.randint(1,100)
        for i in range(5,0,-1):
              num=int(input("Guess the Number"))
              if num==a:
                  print("I'M CLAPPING VIRTUALLY")
                  print(name,"Won")
                  result=mediumpoint(lst_medium)
                  store(result)
                  if result>=60:
                          p=result
                          medium_update(name,p)
                          print()
                          print("CONGRATULATIONS!!YOUR NAME IS IN THE LEADERBOARD")
                  else:
                          print("Amol Bhatia is undefeted")

                  break
              elif num!=a:
                  if num>a:
                      print("Number is less than", num)
                      print(i-1 ,"TRIES REMAIN")
                      lst_medium.append(num)
                  elif num<a:
                      print("Number is Greater than",num)
                      print(i-1, "TRIES REMAIN")
                      lst_medium.append(num)
              if i==1:
                print("NUMBER IS ",a)
                print("GAME OVER BETTER LUCK NEXT TIME HEHE")
                result=mediumpoint(lst_medium)
                store(result)
                print()
        retry=input(" WANT TO TRY AGAIN [Y/N]")
        if retry.upper()=="N":
                  print('''THANK YOU FOR PLAYING
                           ~AMOL BHATIA''')
                  break
    elif int(X)==3:#hard
        a=random.randint(1,700)
        for i in range(10,0,-1):
              num=int(input("Guess the Number"))
              if num==a:
                  print("I CAN SMELL YOU HACKED MY SOURCE CODE")
                  print(name,"Won")
                  result=hardpoint(lst_hard)
                  store(result)
                  if result>=50:
                          p=result
                          hard_update(name,p)
                          print()
                          print("CONGRATULATIONS!!YOUR NAME IS IN THE LEADERBOARD")
                  else:
                          print("Amol Bhatia is undefeted")
                  
                  break
              elif num!=a:
                  if num>a:
                      print("Number is less than", num)
                      print(i-1 ,"TRIES REMAIN")
                      lst_hard.append(num)
                  elif num<a:
                      print("Number is Greater than",num)
                      print(i-1, "TRIES REMAIN")
                      lst_hard.append(num)
              if i==1:
                print("NUMBER IS ",a)
                print("GAME OVER BETTER LUCK NEXT TIME HEHE :)")
                result=hardpoint(lst_hard)
                store(result)
                print()
        retry=input(" WANT TO TRY AGAIN [Y/N]")
        if retry.upper()=="N":
                  print('''THANK YOU FOR PLAYING
                    ~AMOL BHATIA''')
                  break
    elif int(X)==4:#god mode
        a=random.randint(1,1500)
        for i in range(10,0,-1):
              num=int(input("Guess the Number"))
              if num==a:
                  print("ARE YOU A MIND READER",name.upper(),"??")
                  result=godpoint(lst_god)
                  store(result)
                  if result>=70:
                          p=result
                          god_update(name,p)
                          print()
                          print("CONGRATULATIONS!!YOUR NAME IS IN THE LEADERBOARD")
                  else:
                          print("Amol Bhatia is undefeted")

                  break
              elif num!=a:
                  if num>a:
                      print("Number is less than", num)
                      print(i-1 ,"TRIES REMAIN")
                      lst_god.append(num)
                  elif num<a:
                      print("Number is Greater than",num)
                      print(i-1, "TRIES REMAIN")
                      lst_god.append(num)
              if i==1:
                print("NUMBER IS ",a)
                print("GAME OVER BETTER LUCK NEXT TIME HEHE :)")
                result=godpoint(lst_god)
                store(result)
                print()
        retry=input("WANT TO TRY AGAIN [Y/N]")
        if retry.upper()=="N":
                  print('''THANK YOU FOR PLAYING
                        ~AMOL BHATIA''')
                  break
    elif int(X)==5: #implausible
        l=len(name)
        if l==1 or l==2:
            a=random.randint(1,int(pow(l,4)))
            for i in range(5,0,-1):
                  num=int(input("Guess the Number"))
                  if num==a:
                      print("Answer is correct but enter a CORRECT name!!!")
        elif l<=4:
            a=random.randint(1,int(pow(l,4)))
            for i in range(5,0,-1):
                  num=int(input("Guess the Number"))
                  if num==a:
                      print("HOW THAT'S EVEN POSSIBLE")
                      print("I THINK JAMES BOND IS PLAYING") 
                      print("SCORE NOT DEFINED FOR SUCH GUESSES")
                      store(5)
                      print()
                      print("Your Name Is Saved")
                      break
                  elif num!=a:
                      if num>a:
                          print("Number is less than", num)
                          print(i-1 ,"TRIES REMAIN")
                      elif num<a:
                          print("Number is Greater than",num)
                          print(i-1, "TRIES REMAIN")
                  if i==1:
                    print("NUMBER IS.....", "ERROR(4^4) :(")
                    print("GAME OVER BETTER LUCK NEXT TIME")
                    print("HINT: THE RANGE IS YOUR NAME LENTH RAISED......ERROR(4^4) :(")
                    print()
            retry=input(" WANT TO TRY AGAIN [Y/N]")
            if retry.upper()=="N":
                      print('''THANK YOU FOR PLAYING
                        ~AMOL BHATIA''')
                      break
        elif l>4:
            a=random.randint(1,int(pow(l,4)))
            for i in range(7,0,-1):
                  num=int(input("Guess the Number"))
                  if num==a:
                      print("HOW THAT'S EVEN POSSIBLE")
                      print("I THINK JAMES BOND IS PLAYING") 
                      print("SCORE NOT DEFINED FOR SUCH GUESSES")
                      store(5)
                      print()
                      print("Your Name Is Saved")
                      break
                  elif num!=a:
                      if num>a:
                          print("Number is less than", num)
                          print(i-1 ,"TRIES REMAIN")
                      elif num<a:
                          print("Number is Greater than",num)
                          print(i-1, "TRIES REMAIN")
                  if i==1:
                    print("NUMBER IS ", "ERROR(4^4) :(")
                    print("GAME OVER BETTER LUCK NEXT TIME")
                    print("HINT: THE RANGE IS HIDDEN IN YOUR NAME LENGTH")
                    print()
            retry=input(" WANT TO TRY AGAIN [Y/N]")
            if retry.upper()=="N":
                      print('''THANK YOU FOR PLAYING
                        ~AMOL BHATIA''')
                      break
    elif int(X)==0:
        print(''' For Easy Mode
            * Range{1-50} 
            * 5 turns
            * -30 of 100 for each incorrct guess''')
        print(''' For Medium Mode
            * Range{1-100}
            * 5 turns
            * -20 of 100 for each incorrct guess''')
        print(''' For Hard Mode
            * Range{1-700}
            * 10 turns
            * -10 of 100 for each incorrct guess''')
        print(''' For God Mode
            * Range{1-1500}
            * 10 turns
            * -5 of 100 for each incorrct guess''')
        print()
        print("All your Score is saved in the excel file named GuessTheNumber.csv :)")
        print("ENJOY THE GAME :)")

    else:
        print("YOU NEED SOME PATIENCE")
        print("READ THE OPTIONS CAREFULLY")









































        
        

                  

