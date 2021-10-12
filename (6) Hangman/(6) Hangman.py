#Hangman
import random
def let(word, wrg, inp):
    #pos variable used to go to position of letter in word
    pos = 0
    if inp.upper() not in word:
        #.upper used to avoid case sensitivity
            wrg += 1
    else:
            for letter in word:
                if inp.upper() == letter:
                    #[pos] used for indexing
                    templist[pos] = letter
                pos += 1
    #wrg used to keep track of incorrect attempts
    return wrg 

def man(wrg):
    #prints board
    print('''|--!
|  O''')
    if wrg <=2:
        if wrg == 0:
          print('|  |  ')
        elif wrg == 1:
          print('| /| ')
        elif wrg == 2:
          print('| /|\  ')
    elif wrg == 3:
        print('| /|\ ')
        print('|* | *')
    elif wrg == 4:
        print('| /|\ ')
        print('|* | *')
        print('| / \ ')
    elif wrg == 5:
        print('| /|\ ')
        print('|* | *')
        print('|_/ \_')
        print("You lose.")
        print(f"The word was {word}")
    
#wordlist.txt contains all known words           
file = open('wordlist.txt', 'r')
word = random.choice(file.readlines())
word = word.strip()
#word.strip() removes extra spaces
temp = len(word)*'_ '
#temp is the template
templist = temp.split()

print(temp)
sum = 0
wrg = 0
while word != temp.replace(' ','') and sum<5:
    #sum is the counter of the errors
    inp = input("Enter a letter: ")
    let(word, wrg,inp)
    temp = ' '.join(templist)
    print(temp)
    sum += let(word,wrg,inp)
    man(sum)
    if temp.replace(' ','') == word.strip():
        print('You have guessed the word correctly!')
