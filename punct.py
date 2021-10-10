def punct(char):
    puncfile = ['.',',','!',':',';','"',"'",')','(','?','-','[',']','{','}',' ']
    for sym in puncfile:
        if str(char) == str(sym):
            print(char, end = '')
