import random 
us=0
cs=0
while True:
    userchoice=input("enter your choice:")
    print("your choice:",userchoice)
    compchoice =random.choice(["rock","paper","scissor"])
    print("computers choice:",compchoice)
    if userchoice==compchoice:
        print("its tie")
    elif(userchoice=="rock" and compchoice=="scissor")or(userchoice=="paper"and compchoice=="rock")or(userchoice=="scissor"and compchoice=="paper"):
        print("you win")
        us+=1
    else:
        print("computer wins")
        cs+=1
    print("score:")
    print("user:",us)
    print("computer:",cs)
    playagain=input("do you want to play again :")
    if playagain.lower()!="yes":
        print("well played")
        break    

    