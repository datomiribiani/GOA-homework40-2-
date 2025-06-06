# 1)შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვების სია,თქვენი დავვალებაა იპოვოთ ამ სიიდან ყველაზე პატარა და ყველაზე დიდი რიცხვები
def min_max(list1):
    for i in list1:
        list1.min(i)
        list1.max(i)
    return list1
print(min_max[1,2,3,4,6,7,9,10])
# 2)შექმენით ფუნქცია,რომელსაც გადაეცემა სტრინგებით სავსე სია,რომელი სტრინგის სიგრძეც მეტია 6 ზე დააბრუნეთ ეს სტრინგები ოღონდ შემოტრიალებული და პირველი ასო ქონდეთ დიდი(CAPITALIZE)
str2 = input("enter str :")
def str1(user_str):
    for i in user_str:
        if len(user_str) > 6:
            user_str.capitalize(i)
    return user_str
print(str1(str2))
# 3)შექმენით ფუნქცია რომელსაც გადაეცემა ერთი მთლიანი წინადადება,თქვენი დავალებაა ამ წინადადებაში მყოფი სიტყვები ჩაამატოთ სიაში(გამოიყენეთ შესაბამისი ფუნქცია)და შემდეგ ეს სია დაუბრუნოთ ისევ ერთ მთლიან სტრინგად(წინადადებად) მაგრამ სტრინგად დაბრუნების დროს ეს სიტყვები გამოყავით ერთმანეთისაგან @ ამ ნიშნით და ასევე ყველა სიტყვის პირველი ასო იყოს დიდი(CAPIRALIZE)





# 4)1 დან 100 მდე გამოიტანეთ მხოლოდ კენტი რიცხვები,შეასრულეთ while loop / for loop ორივეთი
def odd(user_odd):
    for i in range(1,101,3):
        return user_odd
print(odd(100))

def odd(odd1):
    result = 1
    while result <= 100:
        result += 2
    return result
print(odd(100))

# 5)1 დან 50 მდე გამოიტანეთ მხოლოდ ის რიცხვები რომლებიც იყოფიან 5 ზეც და 3 ზეც,შეასრულეთ while loop / for loop ორივეთი
def k(user_k):
    result = 0
    for i in range(1,50):
        if i == 5 and i == 3:
            result += 1
    return result
print(k(50))

def w(user_w):
    result = 0
    while result != 5 and result != 3:
        result +=1
    return result
print(w(50))


# 6)ტერმინალში 100 ჯერ გამოიტანეთ hello,შეასრულეთ while loop / for loop ორივეთი
def hello1(user_hello):
    for i in user_hello:
        return "hello"
print(hello1("hello"))

def hello2(user_hello):
    while user_hello != "hello" :
        input("try again")
    return user_hello
print(hello2("hello"))
# 7)შექმენით ფუნქცია რომელსაც გადაეცემა სია,თქვენი დავალებაა იპოვოთ ამ სიაში მხოლოდ ლუწ ინდექსზე მდგომი ელემენტების საშუალო არითმეტიკული


