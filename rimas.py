def rima(pal1,pal2):
    conta=0
    flag = 1
    print("Palavra1: ",pal1,"Cumprimento palavra1: ",len(pal1))
    print("Palavra2: ",pal2,"Cumprimento palavra2: ",len(pal2))
    for c,d in zip(reversed(pal1),reversed(pal2)):
        if(c==d and flag == 1):
            print(c,"e igual a ",d)
            conta+=1
        else:
            flag = 0
    if(conta <= 1):
        print("nao rima")
    elif(conta >= 3):
        print("rima perfeita")
        
            