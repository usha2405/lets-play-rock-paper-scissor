import random


computer_wins=0
player1_wins=0
player2_wins=0
computer_wins=0
print("LETS PLAY ROCK PAPER SCISSOR!!")
co=int(input('How many players are there: '))

if (co==2):

    r=int(input("How many rounds would you like to play:"))
    print("ARE YOU BOTH READY")
    print("Enter \n 1.r for rock \n 2.p for paper \n 3.s for scissors ")

    for i in range(r):


        user1=input("Make your move player1:").lower()
        if user1=='quit' or user1=="q":
            break
        user2=input("Make your move player2:").lower()
        if user2=='quit' or user2=="q":
            break
        if (user1=='r'):
            if (user2=='r'):
                print("OOPS ITS A TIE")

            elif (user2=='p'):
                print("Player 2 gets a point")
                player2_wins+=1
            else:
                print("Player 1 gets a point")
                player2_wins+=1
        elif (user1=='p'):
            if (user2=='p'):
                print("OOPS ITS A TIE")
            elif (user2=='r'):
                print("Player 1 gets a point")
                player1_wins+=1
            else:
                print("Player 2 gets a point")
                player2_wins+=1
        elif (user1=='s') :
            if (user2=='s'):
                print("OOPS ITS A TIE")
            elif (user2=='r'):
                print("Player 1 gets a point")
                player1_wins+=1
            else:
                print("Player 2 gets a point")
                player2_wins+=1
        else:
            print('Choose accordingly')
    print(f"Player 1 scored:{player1_wins}")
    print(f"Player 2 scored:{player2_wins}")

    if(player1_wins>player2_wins):
        print('Player 1 is the winner')
    elif(player1_wins==player2_wins):
        print('OOPS its a tie!')
    else:
        print('Player 2 wins')


elif(co==1):

    print("ARE YOU  READY")
    print("Enter \n 1.r for rock \n 2.p for paper \n 3.s for scissors ")
    r=int(input("How many rounds would you like to play: "))

    for i in range(r):
        user1=input("Make your move player1:").lower()
        if user1=='quit' or user1=="q":
            break

        comp=''
        ran=random.randint(0,2)
        if (ran==0):
            comp ='r'
        elif (ran==1):
            comp ='p'
        if (ran==0):
            comp ='s'
        print("Computer's move: "+comp)

        if (user1=='r'):
            if (comp=='r'):
                print("OOPS ITS A TIE")
            elif (comp=='p'):
                print("Computer gets a point")
                computer_wins+=1
            else:
                print("Player 1 gets a point")
                player1_wins+=1
        elif (user1=='p'):
            if (comp=='p'):
                print("OOPS ITS A TIE")
            elif (comp=='r'):
                print("Player 1 gets a point")
                player1_wins+=1
            else:
                print("Computer gets a point")
                computer_wins+=1
        elif (user1=='s') :
            if (comp=='s'):
                print("OOPS ITS A TIE")
            elif (comp=='r'):
                print("Computer gets a point")
                computer_wins+=1
            else:
                print("Player 1 gets a point")
                player1_wins+=1
        else:
            print('Choose accordingly')
    print(f"Player 1 scored:{player1_wins}")
    print(f"Computer scored:{computer_wins}")


    if(player1_wins>computer_wins):
        print('player 1 is the winner')
    elif(player1_wins==computer_wins):
        print('its a tie')
    else:
        print('computer wins')

else:
    print("This game can be played by one or two players not more then that.")
print("Thank you for playing.\n See you again next time.")
