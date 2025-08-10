def points(games):
    total =0
    for i in games:
        x = int(i[0])
        y = int(i[2])
        if x > y:
            total +=3
        elif x==y:
            total +=1
        return total
