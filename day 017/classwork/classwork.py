# 1)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი -->"ალექსანდრე",თქვენი დავალებაა ეს სტრინგი გახლიჩოთ ასო ე ზე 
def str1(user_str):
    user_str.split("e")
    return user_str
print(str1("aleqsandre"))

# 2)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგი -- > "ჰიდროელექტროსადგური" და რიცხვი პარამეტრად,თქვენი დავალებააა დააბრუნოთ ეს სტრინგი 0 დან იმ ინდექსმდე რა რიცხვსაც შემოიტანს მომხმარებელი
num = int(input("enter num"))
def str_num(user_str , user_num):
    return str_num[0:user_num ]

print(str_num("hidroeleqtrosadguri" ,num ))

# 3)შექმენით ფუნქცია რომელსაც გადაეცემა სია,თქვენი დავალებაა გადაააქციოთ ეს სიაერთ დიდ სტრინგად და ეს სიტყვები ერთმანეთსგან გამოყავით სფეისებით,გამოიყენე შესაბამის ფუნქცია გაიხსენეთ
def split(list1):
    return "".join(list1)
print(split["gamarjoba" , "salami"])

# 4)შექმენით ფუნქცია რომესლაც გადაეცემათ სტრინგი,თქვენი დავალებაა შეამოწმოთ თუ ამ სტრინგის პირველი ასო იქნება uppercase ანუ დიდი მაგ შემთხვევაში დააბრუნეთ True სხვა შემთხვევეაში დააბრუნეთ False
def str3(user_str1):
    if user_str1 == user_str1.capitalize:
        return True
    else:
        return False
    

# 5)შექმენით ფუნქცია რომელსაც გადაეცემა სია,თქვენი დავალებაა შეამოწმოთ თუ ამ სიის რომელიმე ელემენტის სიგრძე ნაკლებია 5 ზე ამოშალეთ ეს ელემენტები სიიდან და დააბრუნეთ ძველი სიასადაც აღარ გვექნება ამოშლილი სიტყვები რომელთა სიგრძეც ნაკლები იყო 5 ზე
def list3(user_list):
    list2 = []
    if user_list <= 5:
        user_list.remove(user_list)
        list2.append(user_list)
    return list2
print(list3[1,2,3,4,5])


# 6)შექმენით ფუნქცია რომელსაც გადაეცემა სია -- >["kaxi" , "ana" ,"Aleqsandre", "ia" , "Giorgi" , "Iamze" , "beqa"],თქვენი დავალებაა შეამოწმოთ თუ ამ სიიდან თითოეული ელემენტი იწყება დიდ ასოზე ანუ არის capitalize() ეს ელემენტები ადაამატოთ ახალ სიაში და დააბრუნოთ ეს ახალი სია სადაც მოთავსებული გვექნება დიდი ასოთი დაწყებული სიტყბვები
def list1(user_list):
    result = []
    if user_list == user_list.capitalize():
        result.append(user_list)
    return result
print(list1["kaxi" , "ana" ,"Aleqsandre", "ia" , "Giorgi" , "Iamze" , "beqa"])




# 7)შექმენით ფუნქცია რომელსაც გადაეცემა შემდეგი სია["kaxi" , 5 ,"Aleqsandre", 10, "Giorgi" ,20 , "beqa"] თვენი დავალებაა ამ სიიდან ამოშალოთ მხოლოდ integer ები და დააბრუნოთ სია მათ გარეშე
def int_delete(user_int):
    for i in user_int:
        if type(i) == int:
            user_int.remove(i)
    return user_int
print(int_delete["kaxi" , 5 ,"Aleqsandre", 10, "Giorgi" ,20 , "beqa"])