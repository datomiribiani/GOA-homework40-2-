# 4) მომხმარებელს შემოატანინეთ რიცხვი და ამ რიცხვის ყველა გამყოფები დაპრინტეთ სათითაოდ
num = int(input("enter your number"))
for i in range(1,num + 1):
    if num % i == 0 :
        print(i)  

