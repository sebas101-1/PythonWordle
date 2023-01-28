import random
from nltk.corpus import words
while True:
    pass
    lst = words.words()
    w=[]
    for t in range(len(lst)):
        if len(lst[t]) == 5:
            w.append((lst[t]).lower())
    index = random.randint(0, len(w)-1)
    fnl = []
    final = w[index]
    for i in range(len(w[index])):
        fnl.append(w[index][i])
    guess = ''
    results = ''
    first = False
    zed = False
    g=''
    finallst = ["X","X","X","X","X"]
    num = 0
    boo = False
    while(g != final):
        while(len(g)!=5 or boo == False):    
            g = input("guess ")
            g = g.lower()
            num+=1
            for fed in range(len(w)):
                if g == w[fed]:
                    boo = True
            if boo == False:
                print("Must be a real word")
            if g == "sebastien":
                print(final)
        guess = []
        for e in range(len(g)):
            guess.append(g[e])
        for z in range(len(guess)):
            for eba in range(len(fnl)):
                if guess[z] == fnl[eba] and eba == z:
                    fnl[eba] = '?'
                    finallst[z] = "?"
        for j in range(len(guess)):
            for k in range(len(fnl)):
                if fnl[k] == guess[j]:
                    fnl[k] = "<"
                    finallst[j] = "<"
            results = ''
        for dz in range(len(finallst)):
            if "<" == finallst[dz]:
                results = results+"🟧"
            elif finallst[dz] == "?":
                results = results+"✔️"
            else:
                    results = results+"❌"
        fnl = []
        for e in range(len(w[index])):
            fnl.append(w[index][e])
        print(results)
        results = ''
        if g != final:
            g = ''
            boo = False
        else:
            print("Good Job!!",num)
            num = 0
                        