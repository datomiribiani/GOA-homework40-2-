# 6)მომხმარებელს შემოატანინე ათზე მაღალი რიცხვი,for loop ის გამოყენებით იპოვეთ 5 დან მომხმარებლის შემოტანილ რიცხვამდე ყველა რიცხვის ჯამი,იგივე გააკეთეთ while loop ითაც
num = int(input("enter your num"))
sum = 0
for i in range(10 , num):    
    sum += i
print(sum)



sum = 0
i = 10
while i < num :
    i += 1
    sum += i
print(sum)


