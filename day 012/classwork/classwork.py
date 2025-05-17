# 1) შექმენით ფუნქცია, სადაც მოხმარებელს შემოატანინებთ რიცხვს და ამ რიცხვის გამყოფებს დააბრუნებს სიაში.
# user_number =int(input("enter your number"))
# def gamyofi(number):
#     my_num = []  
#     for num in range(2, number):
#         if number % num == 0:
#             my_num.append(num)
#     return my_num
# print(gamyofi(user_number))
# 2) შექმენით ფუნქცია, რომესლაც გადაეცემა მომხმარებლის შემოტანილი ტექსტი და დაითვლით ასო 'a'-ს რაოდენობას. (დიდადაც რომ იყოს დაწერილი ისიც რომ ჩაითვალოს).
# user_string = input("enter your str:")
# def str_a(String):
#     String = String.lower()
#     count = 0
#     for i in String:
#         if i == "a":
#             count += 1
#     return count
# print(str_a(user_string))


# 3) მომხმარებელს შემოატანინეთ რიცხვი და სიის სახით დააბრუნეთ ისეთი რიცხვები რომლებიც არ იყოფა მომხმარებლის შემოტანილ რიცხვზე.
user_number =int(input("enter your number"))
def gamyofi(number):
    my_num = []  
    for num in range(2, number):
        if number % num != 0:
            my_num.append(num)
    return my_num
print(gamyofi(user_number))

# 4) მომხმარებელს შემოატანინეთ ტექსტი და ამ ტექსტში დაითვალეთ რიცხვების რაოდენობა.

user_string = input("enter your str:")
def str_a(String):
    String = String.lower()
    count = 0
    for i in String:
        if i == user_string :
            count += 1
    return count
print(str_a(user_string))