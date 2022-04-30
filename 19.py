def game(k,h):
    if (h==2) and (k >= 69):
        return True
    if (h==2) and (k < 69):
        return False
    if (h==1) and (k >= 69):
        return False
    h += 1
    return game(k+1,h) or game (k*2,h)
for x in range (1,68):
    if game(x,0):
        print(x)
        break