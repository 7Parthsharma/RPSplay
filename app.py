import random

choices = ['rock', 'paper','scissors']
player = None

computer = random.choice(choices)

while player not in choices:
    player = input('Rock, Paper, Scissors : ')

print('computer: ',computer)
print('player: ',player)

if player == computer :
    print("it's a draw")
elif player == 'paper' and computer=='rock':
    print("you win")
elif player == 'scissors' and computer == 'paper':
    print("you win")
elif player == 'rock' and computer == 'scissors':
    print("you win")

elif player == 'scissors' and computer == 'rock':
    print("you loose")
elif player == 'paper' and computer == 'scissors':
    print("you loose")
elif player == 'scissors' and computer =='rock':
    print("you loose")




