#  1) მომხმარებელს შეეკითხეთ ორი რიცხვი შემდეგ კი შექმენით ფუნქცია რომელსაც არგუმენტად გადასცემთ ამ ორ რიცხვს ხოლო ფუნქცია დააბრუნებს ამ ორი რიცხვის ჯამს, 
# ასევე გააკეთე ასეთი 4 ფუნქცია სხვადასხვა მათემატიკური მოქმედებებისთვის, გამოიყენეთ პარამეტრები და არგუმენტად გადაეცით მომხარებლის შემოტანილი რიცხვები
num = input(int("ennter your num"))
num1 = input(int("ennter your num"))
def number(num , num1):
    return num + num1
print(number(num, num1))

num = input(int("ennter your num"))
num1 = input(int("ennter your num"))
def number(num , num1):
    return num * num1
print(number(num, num1))


num = input(int("ennter your num"))
num1 = input(int("ennter your num"))
def number(num , num1):
    return num / num1
print(number(num, num1))

num = input(int("ennter your num"))
num1 = input(int("ennter your num"))
def number(num , num1):
    return num ** num1
print(number(num, num1))
# 2)  შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვებით სავსე სია ამ ფუნქციამ კი უნდა დააბრუნოს ამ სიის რიცხვების ჯამი
def sum(list1):
    sum1 = 0
    for i in list1 :
        sum1 += i
    return sum1
print(sum[1,23,24,2,4,34,23,2,2,54,67,87,878,432,4])

# 3) შექმენით ფუნქცია რომელსაც გადაეცემა არგუმენტად რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ლუწია ეს რიცხვი თუ კენტი
def sum(number):
    if number % 2  == 0 : 
        print("LUWI")
    else :
        print("kenti")
print(sum(4))
print(sum(7))
# 4) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ეს რიცხვი დადებითია თუ უარყოფითი
def sum(number):
    if number < 0 : 
        print("uaryofiti")
    else :
        print("dadebiti")
print(sum(12))
print(sum(-9))
# 5) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვი შემდეგ კი ფუნქციამ უნდა დაგვიბრუნოს მისი საპირისპირო რიცხვი 
def uaryofa(number):
    return number * -1
print(uaryofa(12))        


# 7)კომენტარის სახით აღწერეთ ყვეელაფერი ფუნქციის შესახებ,რატომ ვიყენებთ და რატომ არის კარგი მისი გამოყენება რაში გვეხმარება და ასე შემდეგ,ასვევე დაწერეთ როგორ ვქმნით მას და რა მნიშვნელობები გადაეცემა მას

# ფუნქცია ბევრამეში გვეხმარება მაგალითად ადვილი კოდისწერა და კომპიუტერს ბევრი ხარჯი არ ექნება არ გადაიტვირთება