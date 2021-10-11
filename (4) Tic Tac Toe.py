def board():
  print(" --- --- ---")
  print("|   |   |   |")   
  print(" --- --- ---")
  print("|   |   |   |") 
  print(" --- --- ---")
  print("|   |   |   |")  
  print(" --- --- ---")
const1 = 0
a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "
while const1 == 0:
  if a == b and b == c and c == "X":
    print("Player 1 wins")
    const1 = 1
    break
  elif d == e and e == f and f == "X":
    print("Player 1 wins")
    const1 = 1
    break
  elif g == h and h == i and i == "X":
    print("Player 1 wins")
    const1 = 1
    break
  elif a == d and d == g and g == "X":
    print("Player 1 wins")
    const1 = 1
    break
  elif b == e and e == h and h == "X":
    print("Player 1 wins")
    const1 = 1
    break
  elif c == f and f == i and i == "X":
    print("Player 1 wins")
    const1 = 1
    break
  elif a == e and e == i and i == "X":
    print("Player 1 wins")
    const1 = 1
    break
  elif c == e and e == g and g == "X":
    print("Player 1 wins")
    const1 = 1
    break
  elif a == b and b == c and c == "O":
    print("Player 2 wins")
    const1 = 1
    break
  elif d == e and e == f and f == "O":
    print("Player 2 wins")
    const1 = 1
    break
  elif g == h and h == i and i == "O":
    print("Player 2 wins")
    const1 = 1
    break
  elif a == d and d == g and g == "O":
    print("Player 2 wins")
    const1 = 1
    break
  elif b == e and e == h and h == "O":
    print("Player 2 wins")
    const1 = 1
    break
  elif c == f and f == i and i == "O":
    print("Player 2 wins")
    const1 = 1
    break
  elif a == e and e == i and i == "O":
    print("Player 2 wins")
    const1 = 1
    break
  elif c == e and e == g and g == "O":
    print("Player 2 wins")
    const1 = 1
    break
  elif a != " " and b != " " and c != " " and d != " " and e != " " and f != " " and g != " " and h != " " and i != " ":
    print("The game is a draw!")
    const1 = 1
    break
  else:
    print("You are the 1st player.")
    print("Your symbol will be X")
    const2 = 0
    while const2==0:
      inprow1 = int(input("Which row would you like"))
      if inprow1 == 1:
        incol1 = int(input("Which column would you like"))
        if incol1 == 1 and a == " ":
            a = 'X'
            const2=1
            break
        elif incol1 == 2  and b == " ":
            b = 'X'
            const2=1
            break
        elif incol1 == 3  and c == " ":
            c = 'X'
            const2=1
            break
        elif incol1 == 1 and a != " ":
            print("There is already a symbol there!")
        elif incol1 == 2 and b != " ":
            print("There is already a symbol there!")
        elif incol1 == 3  and c != " ":
            print("There is already a symbol there!")
        else:
          print("Invalid Reply.")
      elif inprow1 == 2:
        incol1 = int(input("Which column would you like"))
        if incol1 == 1  and d == " ":
            d = 'X'
            const2=1
            break
        elif incol1 == 2  and e == " ":
            e = 'X'
            const2=1
            break
        elif incol1 == 3  and f == " ":
            f = 'X'
            const2=1
            break
        elif incol1 == 1 and d != " ":
            print("There is already a symbol there!")
        elif incol1 == 2 and e != " ":
            print("There is already a symbol there!")
        elif incol1 == 3  and f != " ":
            print("There is already a symbol there!")
        else:
          print("Invalid Reply.")
      elif inprow1 == 3:
        incol1 = int(input("Which column would you like"))
        if incol1 == 1 and g == " ":
            g = 'X'
            const2=1
            break
        elif incol1 == 2 and h == " ":
            h = 'X'
            const2=1
            break
        elif incol1 == 3 and i == " ":
            i = 'X'
            const2=1
            break
        elif incol1 == 1 and g != " ":
            print("There is already a symbol there!")
        elif incol1 == 2 and h != " ":
            print("There is already a symbol there!")
        elif incol1 == 3  and i != " ":
            print("There is already a symbol there!")
        else:
          print("Invalid Reply.")
      else:
        print("Invalid Reply.")
    print(" --- --- ---")
    print("| {} | {} | {} |".format(a,b,c))   
    print(" --- --- ---")
    print("| {} | {} | {} |".format(d,e,f)) 
    print(" --- --- ---")
    print("| {} | {} | {} |".format(g,h,i))  
    print(" --- --- ---")
  if a == b and b == c and c == "X":
    print("Player 1 wins")
    const1 = 1
    break
  elif d == e and e == f and f == "X":
    print("Player 1 wins")
    const1 = 1
    break
  elif g == h and h == i and i == "X":
    print("Player 1 wins")
    const1 = 1
    break
  elif a == d and d == g and g == "X":
    print("Player 1 wins")
    const1 = 1
    break
  elif b == e and e == h and h == "X":
    print("Player 1 wins")
    const1 = 1
    break
  elif c == f and f == i and i == "X":
    print("Player 1 wins")
    const1 = 1
    break
  elif a == e and e == i and i == "X":
    print("Player 1 wins")
    const1 = 1
    break
  elif c == e and e == g and g == "X":
    print("Player 1 wins")
    const1 = 1
    break
  elif a == b and b == c and c == "O":
    print("Player 2 wins")
    const1 = 1
    break
  elif d == e and e == f and f == "O":
    print("Player 2 wins")
    const1 = 1
    break
  elif g == h and h == i and i == "O":
    print("Player 2 wins")
    const1 = 1
    break
  elif a == d and d == g and g == "O":
    print("Player 2 wins")
    const1 = 1
    break
  elif b == e and e == h and h == "O":
    print("Player 2 wins")
    const1 = 1
    break
  elif c == f and f == i and i == "O":
    print("Player 2 wins")
    const1 = 1
    break
  elif a == e and e == i and i == "O":
    print("Player 2 wins")
    const1 = 1
    break
  elif c == e and e == g and g == "O":
    print("Player 2 wins")
    const1 = 1
    break
  elif a != " " and b != " " and c != " " and d != " " and e != " " and f != " " and g != " " and h != " " and i != " ":
    print("The game is a draw!")
    const1 = 1
    break
  else:
    print("You are the 2nd player.")
    print("Your symbol will be O")
    const3 = 0
    while const3==0:
      inprow2 = int(input("Which row would you like"))
      if inprow2 == 1:
        incol2 = int(input("Which column would you like"))
        if incol2 == 1 and a == " ":
            a = 'O'
            const3 = 1
            break
        elif incol2 == 2 and b == " ":
            b = 'O'
            const3 = 1
            break
        elif incol2 == 3  and c == " ":
            c = 'O'
            const3 = 1
            break
        elif incol2 == 1 and a != " ":
            print("There is already a symbol there!")
        elif incol2 == 2 and b != " ":
            print("There is already a symbol there!")
        elif incol2 == 3  and c != " ":
            print("There is already a symbol there!")
        else:
          print("Invalid Reply.")
      elif inprow2 == 2:
        incol2 = int(input("Which column would you like"))
        if incol2 == 1  and d == " ":
            d = 'O'
            const3 = 1
            break
        elif incol2 == 2  and e == " ":
            e = 'O'
            const3 = 1
            break
        elif incol2 == 3 and f == " ":
            f = 'O'
            const3 = 1
            break
        elif incol2 == 1 and d != " ":
            print("There is already a symbol there!")
        elif incol2 == 2 and e != " ":
            print("There is already a symbol there!")
        elif incol2 == 3  and f != " ":
            print("There is already a symbol there!")
        else:
          print("Invalid Reply.")
      elif inprow2 == 3:
        incol2 = int(input("Which column would you like"))
        if incol2 == 1 and g == " ":
            g = 'O'
            const3 = 1
            break
        elif incol2 == 2 and h == " ":
            h = 'O'
            const3 = 1
            break
        elif incol2 == 3 and i == " ":
            i = 'O'
            const3 = 1
            break
        elif incol2 == 1 and g != " ":
            print("There is already a symbol there!")
        elif incol2 == 2 and h != " ":
            print("There is already a symbol there!")
        elif incol2 == 3  and i != " ":
            print("There is already a symbol there!")
        else:
          print("Invalid Reply.")
      else:
        print("Invalid Reply.")
    print(" --- --- ---")
    print("| {} | {} | {} |".format(a,b,c))   
    print(" --- --- ---")
    print("| {} | {} | {} |".format(d,e,f)) 
    print(" --- --- ---")
    print("| {} | {} | {} |".format(g,h,i))  
    print(" --- --- ---")


