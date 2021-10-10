#Encoding the Matrix
from punct import punct

numline = int(input("Enter no. of lines of code you wish to enter: "))
codelist = []
for linenum in range(1, numline+1):
    term = input(f"Enter line {linenum}:")
    codelist.append(term)

for line in codelist:
    for numchar in range(len(line)):
       for line in codelist:
         if line[numchar].isalpha() == True:
             print(line[numchar], end='')
         else:
             punct(line[numchar])   
       print(end = ' ')
    break
        
        
