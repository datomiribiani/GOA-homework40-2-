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
player1 = input("plauer1 :")
player2 = input("plauer2 :")
def play_game(first,second):
    player1_score = 0
    player2_score = 0
    while player1_score < 3 and player2_score < 3:
        player1_choice = input(first, "qva , makrateli , qagaldi:")
        player2_choice = input(second, "qva , makrateli , qagaldi:")
        
        if player1_choice == player2_choice:
            print("fre")
        elif (player1_choice == "qva" and player2_choice == "makrateli") or (player1_choice == "makrateli" and player2_choice == "qagaldi")or (player1_choice == "qagaldi" and player2_choice == "qva"):
            print(first, "igebs") 
            player1_score += 1
        else:
            print(second , "igebs")
            player2_score +=1 

        print("score - " + first + ":" + player1_score + ":"+ player2_score )

print(play_game(player1,player2))