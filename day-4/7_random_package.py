import random as r #imports whole package
#or
#import random import randint , shuffle
#random package imports a lot of functions
#.randint(start, stop) will give u a random no between start and stop including both of them
print(r.randint(1,6)) #or r.randint

players = ['dylan','clinton','harsh']
for player in players:
    roll=r.randint(1,6)
    print(player,' rolled a ',roll)

#.shuffle(list) mixes the order of the list randomly

chores = ['dishes','laundry','dust','take out the dog']
r.shuffle(chores)
print('this is the order in which')
for chore in chores:
    print(chore)

#.choice returns a random item from a list

game = ['rock','papers','scissors']
while True:
    my_choice = input('rock, paper, scissors, SHOOT : ')
    computer = r.choice(game)
    print('computer chose ', computer)
    win = input('did u win(y/n) ')
    if win == 'y':
        print('nice work')
        break