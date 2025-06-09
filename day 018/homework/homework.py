# 1)შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვების სია,თქვენი დავვალებაა იპოვოთ ამ სიიდან ყველაზე პატარა და ყველაზე დიდი რიცხვები
def min_max(list1):
    return min(list1),max(list1)
print(min_max([1,2,3,4,6,7,9,10]))
# 2)შექმენით ფუნქცია,რომელსაც გადაეცემა სტრინგებით სავსე სია,რომელი სტრინგის სიგრძეც მეტია 6 ზე დააბრუნეთ ეს სტრინგები ოღონდ შემოტრიალებული და პირველი ასო ქონდეთ დიდი(CAPITALIZE)
str2 = input("enter str :")
def str1(list1):
    list2 = []
    for i in list1:
        if len(i) > 6:
            list2.append(i[::-1].capitalize())
    return list2 
print(str1(["fgrfgfdsf","fefdsf"]))
# 3)შექმენით ფუნქცია რომელსაც გადაეცემა ერთი მთლიანი წინადადება,თქვენი დავალებაა ამ წინადადებაში მყოფი სიტყვები ჩაამატოთ სიაში(გამოიყენეთ შესაბამისი ფუნქცია)და შემდეგ ეს სია დაუბრუნოთ ისევ ერთ მთლიან სტრინგად(წინადადებად) მაგრამ სტრინგად დაბრუნების დროს ეს სიტყვები გამოყავით ერთმანეთისაგან @ ამ ნიშნით და ასევე ყველა სიტყვის პირველი ასო იყოს დიდი(CAPIRALIZE)
def joinn(user):
    new_user = user.split()
    New = []
    for i in new_user:
        New.append(i.capitalize())
    return '@'.join(New)
print(joinn("heelo user124 bye"))

# 4)1 დან 100 მდე გამოიტანეთ მხოლოდ კენტი რიცხვები,შეასრულეთ while loop / for loop ორივეთი
def odd():
    for i in range(1,100,2):
        print(i)
odd()

def odd(odd1):
    result = 1
    while result <= 100:
        result += 2
        print(result)
print(odd())


# 5)1 დან 50 მდე გამოიტანეთ მხოლოდ ის რიცხვები რომლებიც იყოფიან 5 ზეც და 3 ზეც,შეასრულეთ while loop / for loop ორივეთი
def k(user_k):
    result = 0
    for i in range(1,50):
        if i % 5 == 0 and i % 3 == 0:
            print(i)
print(k())

def w(user_w):
    result = 0
    while result % 5 == 0 and result % 3 == 0:
        result +=1
        print(result)
print(w())


# 6)ტერმინალში 100 ჯერ გამოიტანეთ hello,შეასრულეთ while loop / for loop ორივეთი
def hello1(user_hello):
    for i in range(100):
        print(user_hello)        
print(hello1("hello"))

def hello2(user_hello):
    result = 0
    while result <= 100:
        result +=1
        print (user_hello)     
print(hello2("hello"))
# 7)შექმენით ფუნქცია რომელსაც გადაეცემა სია,თქვენი დავალებაა იპოვოთ ამ სიაში მხოლოდ ლუწ ინდექსზე მდგომი ელემენტების საშუალო არითმეტიკული
def even_index(number):
    even = []
    for num in number:
        if number.index(num) %2 ==0:
            even.append(num)
    return sum(even) / len(even) 

