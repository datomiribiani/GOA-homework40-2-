# 7)მომხმარებელს შემოატანინე 50 ზე მაღალი რიცხვი for loop გამოყენებით ერთიდან მომხმარებლის შემოტანილ რიცხვამდეე დაბეჭდეთ ყველა რიცხვი 5 step ის გამოყენებით,იგივე გაააკეთეთ while loop ითაც
num = int(input("enter your num"))
for i in range(0 , num , 5):    
    print(i)



i = 0 
while i < num :
    i += 5
    print(i)