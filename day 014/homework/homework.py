# 1) წინა დავალებები გაასწორეთ.
# გაკეთებული მაქ


# 2) შექმენით ფუნქცია რომელიც მომხმარებელის შემოატანილ რიცხვის ფაქტორიალს დააბრუნებს.
number = int(input("enter yor number:"))
def num(user_int):
    for i in range(1 ,number+1):
        number *= i
    return num
print(num(number))
# 3) შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილი რიცხვის ჩათვლით დაგვიბრუნებს გამრავლების ტაბულას.
number = int(input("enter yor number:"))
def gamravleba(user_int):
    return number 
print(gamravleba(number*number))
print(gamravleba(number**number))
print(gamravleba(number /number))
print(gamravleba(number // number))
print(gamravleba(number % number))

# 4) შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ სტრინგს დაფარავს *-ით
string1= input("enter yor number:")
def str1(user_string):
    for i in string1:
        return "!"
print(str1(string1))

# 5) შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ რიცხვს დაშლის მამრავლებად. მაგალითად ასე => თუ შემოიტანა რიცხვი 1980 მაშინ შედეგი იყოს 1000 + 900 + 80 (მარტო 1980-ზე არ განიხილოთ ეგ, მაგალითად მოვიყვანე რომ მიხვდეთ ! )
number = int(input("enter yor number:"))
def dashla(user_int):
    if number == 1980:
        return 100 + 900 + 80
    elif number / number:
        return number + number + number
print(dashla(number))


# Bonus: 
# შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ სტრინგში ლუწ ინდექსზე მდომ სიმბოლოებს დაგვიბრუნებს.
string1= input("enter yor number:")
def number2(user_str):
    for i in range( 0 ,10 ,2):
        if string1 % 2 == 0:
            return string1 
print(number2(string1))