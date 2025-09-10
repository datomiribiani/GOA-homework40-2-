def mychar(user1):
    intg = []
    str1 = []
    for i in user1:
        if type(i) == int(i):
            intg.append(i)
        if type(i) == str(i):
            str1.append(i)
            return sorted(intg(True)),  sorted(str1(True , key=len)) 
print(mychar([4,3,2,1,6,5,8,9,'sdada','dddddsewee']))

def surnames(user1):
    name = []
    surnames = []
    for i in user1:
        name.append(i.split(' ')[0])
        surnames.append(i.split(' ')[1])
    return name , surnames

print(surnames(["dato miribiani" , 'andria shanava' ,'goga chlauri']))


