import random
print('Snake - water-gun')
n= int(input('Enter number of rounds: '))
options = ['s','w','g']
round=1 
#count of computer wins
comp_win =0
user_win=0
while round <=n:
    print(f"Round:{round}\nSnake - 's'\nWater -'w'\nGun -'g'")
    try:
        player = input("choose your options:  ")
    except EOFError as e:
        print(e)
        #control of bad inputs
        if player != 's' and player !='g' and player !='w':
print("invalid input,try again")
continue

computer = random.choice(options)
if computer == 's':
if player == 'w':
    comp_win += 1
elif player == 'g':
    user_win += 1

elif computer =='w':
    
    if player == 's':
        comp_win += 'w':
        user_win +=1 

        if user_win> comp_win
        print("congratulations!!You wonnn")
    elif comp_win> user_win:
        print("you lose!!")
    else:
        print("Match Draw!!")