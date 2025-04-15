# 4) მომხმარებელს შემოატანინე ორი სტრინგი და for loop-ის საშუალებით დაითვალე  ორივეში სიმბოლოების რაოდენობა. შემდეგ დაპრინტეთ არის თუ არა ერთმანეთის ტოლი სიმბოლოების რაოდენობა
name = input("enter your name:")
name1 = input("enter your name:")
count = 0 
for i in name:
    count = count + 1
    print(i, name == name1)


name = input("enter your name:")
name1 = input("enter your name:")
count = 0 
for i in name1:
    count = count + 1
    print(i, name == name1)

