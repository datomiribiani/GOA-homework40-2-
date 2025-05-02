# 5)მომხმარებელს შემოატანინე რიცხვი,for loop ის გამოყენებით გამოიტანე თითოეული რიცხვი ერთიდან ამ რიცხვამდე,იგივე გააკეთეთ While loop-ით
num = int(input("enter your num"))
for i in range(1 , num):
    print(i)


i = 1
while i < num:
    i += 1
    print(i)
    