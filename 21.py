def game(k,h):
    if ((h==2) or (h==4)) and (k >=69):
        return True
    if (h==4) and (k < 69):
        return False
    if (h<4) and (k >= 69):
        return False
    h +=1
    if h == 1 or h == 3:
        return game(k+1,h) and game(k*2,h)
    if h == 2 or h ==4:
        return game(k+1,h) or game(k*2,h)

for x in range (1,68):
    if game(x,0):
        print(x)
        break