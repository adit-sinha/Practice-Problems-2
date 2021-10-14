#Hangman
import random
def let(word, wrg, inp):
    #MUST NOT INCLUDE PRINT STATEMENTS RETURN VALUE WRG USED IN MATHEMATICAL
    #OPERATION
    #pos variable used to go to position of letter in word
    #wrg resets after each attempt
  if inp.upper() in usedlist:
        wrg = -1
  else:
    if len(inp)>1:
        if inp.upper() not in word:
            wrg += 1
        else:
            n = 0
            for num in range(len(word)):
                #used to find position of input in the word using indexing
                if (word[num:len(inp)+num] == inp):
                    #converts n = num so that the next for loop appends the
                    #letters to the correct position
                    n = num
            for letinp in inp.upper():
                #appends each letter of the input into the template list
                #done when inp lies in word
                templist[n] = letinp 
                n+=1
            wrg = 0
    else:
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
            wrg = 0
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
        leftlist = ['A','B','C','D','E','F','G','H','I','J','K','L','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        print('| /|\ ')
        print('|* | *')
        print('| / \ ')
        for term in usedlist:
          if len(term) == 1:
            if term in leftlist:
              leftlist.remove(term)
        print(f'Letters left to guess: {",".join(leftlist)}')
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
usedlist = []
while word != temp.replace(' ','') and sum<5:
  #sum is the counter of the errors
  inp = input("Enter a letter: ")
  if inp.isspace() == True:
      print("Please provide a proper reply.")
      print(temp)
      man(sum)
  else:
    let(word, wrg,inp)

    temp = ' '.join(templist)
    print(temp)

    
    if let(word,wrg,inp)==1:
        print("Try again.")
        sum += let(word,wrg,inp)
    elif let(word,wrg,inp)==-1:
        print("You have already attempted this reply.")
        print(f'Used list of letters and phrases: {",".join(usedlist)}')
        usedlist.remove(inp.upper())
    usedlist.append(inp.upper())
    man(sum)
    if temp.replace(' ','') == word.strip():
        print('You have guessed the word correctly!')
