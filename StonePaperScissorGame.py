import random
while True:
    comp=random.randint(1,3)
    player=int(input("Enter 1 for stone, 2 for paper, 3 for scissor: "))
    print("Computer:",comp)
    print("Player:",player)
    
    if comp==player:
        print("Match Draw")
    elif (player==1 and comp==3) or (player==2 and comp==1) or (player==3 and comp==2):
        print("You Win :)")
    else:
        print("You Lose :(")

    print("Enter '0' to continue or any other letter to end")
    if input()=="0":
        continue
    else:
        exit()
