import random
l=["rock","scissor","paper"]

while True:
    ucount=0
    Ccount=0
    uc=int(input('''
game start
1 yes
2 no | exit   

please enter number.....
    
    '''))
    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
1 rock
2 scissor
3 paper                 
            '''))
            if userinput==1:
                uchoice="rock"
            elif userinput==2:
                uchoice="scissor"
            elif userinput==3:
                uchoice="paper"
            Cchoice=random.choice(l)
            print(uchoice)
            print(Cchoice)
            if Cchoice==uchoice:
                print("computer value",Cchoice)
                print("userinput",uchoice)
                print("game draw")
                ucount=ucount+1
                Ccount=Ccount+1
            elif (uchoice=="rock" and Cchoice=="scissor") or (uchoice=="scissor"and Cchoice=="paper") or (uchoice=="paper" and Cchoice=="rock"):
                print("computer value", Cchoice)
                print("userinput", uchoice)
                print("you win")
                ucount=ucount+1
            else:
                print("computer value", Cchoice)
                print("userinput", uchoice)
                print("computer win")
                Ccount = Ccount + 1

            if ucount==Ccount:
                print("final game draw")
                print("user score",ucount)
                print("computer count",Ccount)
            elif ucount>Ccount:
                print("final you win the game")
                print("user score",ucount)
                print("computer count",Ccount)

            else:
                print("final win the computer")
                print("user score",ucount)
                print("computer count",Ccount)

    else:
        break



