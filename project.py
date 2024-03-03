import random

target = random.randint(1,100)

while True:
    userchoice = input("Guess the target number or QUIT : ")
    if(userchoice == "QUIT"):
        break
    userchoice = int(userchoice)
    if(userchoice==target):
        print("Success, correct  guess!!")
        break
    elif(userchoice<target):
        print("Too low!! Try Again")
    else:
        print("Too Big!! Try Again")
        
        
print("GAME IS OVER! THANKS FOR PLAYING.")


















































































