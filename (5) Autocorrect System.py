#Autocorrect System
word = input("Enter sentence: ")
word = word.upper()
#converting the sentence to uppercase
for term in word.split():
    if term.isalpha() == True:
        #for terms with only words
            file = open(f'{term[0]}.txt','r')
            for aw in file:
                if aw.strip() == term:
                    if term == word.split()[0]:
                        #for first term in list
                        print(aw.strip().title(), end = ' ')
                        break
                    else:
                        #for other terms in list
                        print(aw.strip().lower(), end = ' ')
                        break
    elif term.isdigit() == True:
        #for digits
        print(term, end = ' ')
    else:
        termlist = []
        file = open('puncsymb.txt','r')
        for char in term:
          if char.isalpha() == False:
           for aw in file:
            if aw.strip() == char:
                termlist = term.partition(char)
        for elem in termlist:
            if elem.isalpha() == True:
                file = open(f'{term[0]}.txt','r')
                for aw in file:
                    if aw.strip() == elem:
                            print(aw.strip().lower(), end = ' ')
                            break
            else:
                file = open('puncsymb.txt','r')
                for aw in file:
                    if aw.strip() == elem:
                        print(aw.strip(), end = '')
        print(end = ' ')
