# 3)შექმენი ორი ცვლადი ერთში შეინახე შენი სახელი მეორეში შენი ასაკი,შენი დავალებაა შეამოწმო,თუ ასაკი მეტია 18ზე ამ შემთხვევის შიგნით უნდა შეამოწმო შემდეგი პირობა,თუ სახელი ემთხვევა შენს სახელს დაუპრინტე we have same names and we are adults,სხვა შემთხვევაში კი დაუპრინტე we dot have same names but we are adults,ბოლოს დავუბრუნდეთ ასაკს და შევამოწმოთ თუ ასაკი ნაკლებია 18ზე დაპრინტეთ we dont have same names and we are not adults
name = input("enter your num")
age = int(input("enter your num"))
my_name = "dato" 
my_age = 15
if my_age > 18 and my_name == name and age > 18 : 
    print("we have same names and we are adults")
else :
    print("we dont have same names and we are not adults")