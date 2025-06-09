#1 შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგად დიდი წინადადება. თქვენი მიზანია ეს წინადადება გახლიჩოთ და შეაერთოთ ისევ, ოღონდ ისე რომ თითოეული სიტყვის პირველი ასო იყოს დიდად
def jon(user):
    new_user = user.split()
    New = []
    for i in new_user:
        New.append(i.capitalize())
        return New
print(jon("hellouserdato1"))

#2 შექმენით ფუნქცია რომელსაც გადაეცემა სხვადასხვა მონაცემთა ტიპით სავსე სია, თქვენი მიზანია ამ სიიდან მარტო სტრინგ ტიპის მონაცემები დააბრუნოთ ახალ სიაში
def str1(user_str):
    str2 = []
    for i in user_str:
        if user_str == str:
            str2.append(i)
    return str2
print(str1([1,"dato","gio" , True,5.6]))
#3 მომხმარებელს შემოატანინეთ სიტყვა და for / while loop-ების საშუალებით გამოიტანეთ თითოეული ასო



#4 შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილი რიცხვის ჩათვლით გამოგვიტანს ყველა კენტი რიცხვის კვადრატის ჯამს
def num(user_int):
    for i in user_int:
        if i % 3 == 0:
            i ** user_int
    return user_int
print(num(1,2,3,4,5,6,7,8,9))
#5 შექმენით ფუნქცია რომელიც მომხმარებელის შემოტანილ სიტყვიდან ლუწ ინდექსზე მდგომ სიმბოლოების გაერთიანებას დაგვიბრუნებს~
def luw(user_luwi):
    new =""
    for i in user_luwi:
        if i.index % 3 == 0:
            new +=1
    return new
print(luw("goa is the best"))

