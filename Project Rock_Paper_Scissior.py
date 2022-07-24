#!/usr/bin/env python
# coding: utf-8

# In[1]:



print("************ WELCOME IN THE GAME OF ROCK PAPER AND SCISSIOR **************")
print("********************** MADE BY MANOJ CHAUDHARI ***************************")
import random
while True:
    def gamewin(comp,you):
        if comp==you:
            return None
        elif comp == 'r':
            if you=='p':           
                return True
            elif you=='s':
                return False
        elif comp=='p':
            if you=='r':
                return False
            elif you=='s':
                return True
        elif comp=='s':
            if you=='r':
                return True
            elif you=='p':
                return False
    print("comp turn: Rock(r) Paper(p) or Scissior(s)?")
    randomNo=random.randint(1,3)

    if randomNo==1:
        comp='r'
    elif randomNo==2:
        comp='p'
    elif randomNo==3:
        comp='s'
    you=input("your turn :  Rock(r) Paper(p) or Scissior(s)\nYour turn : ")
    a=gamewin(comp,you)
    print(f"Computer Chose :  {comp}")
    print(f"You Chose :  {you}")
    if a==None:
        print("game is tie")
        print("---------------------------------------------")
    elif a:
        print("you win!")
        print("------------------------------------------")
    else:
        print("you Lose!")
        print("-----------------------------------------")
    ans=input("Do You Want To Play Continue Game\nIf es then press y : \nIf no then press n :  ")
    if ans=="n":
        break
    else:
        print("------ PLAY AGAIN --------")
print("********* THANK YOU ********")

