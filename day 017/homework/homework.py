#  1. შექმენით ფუნქცია, რომელიც მომხმარებლის შემოტანილ სიტყვაში დაითვლის რამდენი განსხვავებული ასოსგან შედგება ეს სიტყვა.
aso = input("sityva")
def res(user_int):
    for i in len(user_int):
        return user_int
print(res(aso))
# 2. for loop & while loop - ის გამოყენებით მომხმარებლის შემოტანილ სიტყვას გადაუარეთ და გამოიტანეთ თითოეული ასო.
sityva = input("sityva")
def datvla(user_int):
    for i in len(user_int):
        return user_int
print(datvla(sityva))

sityva = input("sityva")
def datvla(user_int):
    while user_int == user_int:
        input("try again")
    return user_int
print(datvla(sityva))
# 3. შექმენით ფუნქცია, რომელიც მომხმარებლის შემოტანილ float ტიპის მონაცემს დაშლის. მაგალითად 30.7 რომ ავიღოთ, შედეგი ასეთი უნდა იყოს: '30 + 0.7 = 30.7' .
floot = float(input("enter your float"))
def flot(user_float):
    if user_float == int:
        return float(user_float)
print(flot(floot))


# 4. შექმენით ფუნქცია, რომელსაც გადაეცემა სია, თქვენი დავალებაა გამოიტანოთ ყველაზე დიდი რიცხვი. (max ფუნქცია არ გამოიყენოთ)
def list1(user_list):
    for i in range(1,user_list):
        return user_list
print(list1[1,2,3,4,5,6,7,8,9,10])

# Bonus: შექმენით ფუნქცია, სადაც მომხმარებელი ითამაშებს ჯეირანს მანამ სანამ სამჯერ არ წააგებს. 

user = input(" qva or furceli or makrateli: ")
comp = "qva" ,"makrateli " ,"furceli"
if user == "qva" and comp == "furceli":
elif user == "makrateli" and comp == "qva" :
else :
    print("game over")


