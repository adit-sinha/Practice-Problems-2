#Top Trumps
import random
def compcardfun():
    global compcard
    print("Computer used:")
    print('------------------------')
    print(f'Name: {compcard[0]}')
    print(f'(1)Height: {compcard[1]}')
    print(f'(2)Brains: {compcard[2]}')
    print(f'(3)Dark Side: {compcard[3]}')
    print(f'(4)Jedi Powers: {compcard[4]}')
    print(f'(5)Battle Skills: {compcard[5]}')
    print(f'(6)Force Factor: {compcard[6]}')
    print('------------------------')

def usercardlistfun():
    global usercardlist
    cardno = 1
    print("Your cards: ")
    print('------------------------')
    for card in usercardlist:
        print(f'Card number: {cardno}')
        print()
        print(f'Name: {card[0]}')
        print(f'(1)Height: {card[1]}')
        print(f'(2)Brains: {card[2]}')
        print(f'(3)Dark Side: {card[3]}')
        print(f'(4)Jedi Powers: {card[4]}')
        print(f'(5)Battle Skills: {card[5]}')
        print(f'(6)Force Factor: {card[6]}')
        print('------------------------')
        cardno += 1

def compcardlistfun():
    global compcardlist
    cardno = 1
    print("Computer's cards: ")
    print('------------------------')
    for card in compcardlist:
        print(f'Card number: {cardno}')
        print()
        print(f'Name: {card[0]}')
        print(f'(1)Height: {card[1]}')
        print(f'(2)Brains: {card[2]}')
        print(f'(3)Dark Side: {card[3]}')
        print(f'(4)Jedi Powers: {card[4]}')
        print(f'(5)Battle Skills: {card[5]}')
        print(f'(6)Force Factor: {card[6]}')
        print('------------------------')
        cardno += 1
file = open('tt.txt','r')
cardlist = []
for line in file:
    cardlist.append(line.strip().split())
dupcardlist = cardlist


brainlist = []  #1
heightlist = [] #2
dslist = []     #3
jedilist = []   #4
battlelist = [] #5
fflist = []     #6

#---------------------------User---------------------------
usercardlist = []
compcardlist = []
numcard = int(input("How many cards would you like the user and the computer to have? (Max:15)"))
for num in range(numcard):
    addcard = random.choice(dupcardlist)
    usercardlist.append(addcard)
    dupcardlist.remove(addcard)
    
    addcompcard = random.choice(dupcardlist)
    compcardlist.append(addcompcard)
    dupcardlist.remove(addcompcard)

while len(usercardlist) != 0 and len(compcardlist) != 0:
    usercardlistfun()
    usercardno = int(input("Which card would you like to access? "))
    userproperty = int(input("Which property of the card would you like to access? (1/2/3/4/5/6)"))
    compcard = random.choice(compcardlist)
    usercard = usercardlist[usercardno-1]
    if float(usercard[userproperty]) > float(compcard[userproperty]) and len(usercardlist) != 0 and len(compcardlist) != 0:
        compcardfun()
        print("You win this round.")
        print("You get the computer's card.")
        usercardlist.append(compcard)
        compcardlist.remove(compcard)
    elif float(usercard[userproperty]) < float(compcard[userproperty]) and len(usercardlist) != 0 and len(compcardlist) != 0:
        compcardfun()
        print("You lose this round.")
        print("The computer gets your card.")
        usercardlist.remove(usercard)
        compcardlist.append(usercard)

if len(compcardlist) == 0:
    print('------------------------')
    print("You win the game!!!")
    print('------------------------')
else:
    print('------------------------')
    print("You lose the game.")
    print('------------------------')
