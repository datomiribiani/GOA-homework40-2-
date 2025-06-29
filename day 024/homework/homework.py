#  1)შექმენით ფუნქცია რომელიც გადააიყვანს მომხმარებლის შემოყვანილ სტრინგს lower case იდან upper case ში
# name = input("enter str:")
# print(name.upper())
# 2)შექმენი ფუნქცია რომელსაც გადაეცემა სია,ამ სიაში უნდა იყოს მოთავსებული სახელები,თქვენი დავალებაა მიწვდეთ ამ სახელებს და შემდეგ ამ სახელებში მყოფ ასოებს,თქვენი დავალებაა ახალ სიაში ჩაამატოთ მხოლოდ თანხმოვანია ასოები,შემდეგ ამ სიაში მყოფი ასოები დაალაგეთ ანბანის მიხედვით(დაასორტირეთ)მოიძეთ ინფორმაცია თუ როგორ ხდება სორტირება და რომელი ფუნქცია გამოიყენება ამისათვის

def tx(user_str):
    new = []
    for a in user_str:
        for i in a:
            if i in "qwrtypsdfghjklzxcvbnm":
                new.append(i)
    return sorted(new)
print(tx(["datoq" , "luska", "salba" , "gion" , "zmviadi"]))
# 3)შექმენი ფუნქცია რომელსაც გადაეცემა სია,ამ სიაში უნდა გქონდეთ კიდევ სამი სია,და ამ სამ სიაში უნდა გქონდეთ სამ სამი ელემენტი,თქვენი დავალებაა მიწვდეთ ამ სიაში მყოფ სიას,შემდეგ ამ სიებში მყოფ ელმენტებს და შემდეგ ამ ელემენტებშ მყოფ ასოებს,შემდეგ ახალ სიაში დაამატე მხოლოდ ხმოვანი ასოები და დაასორტირე,დაალაგე ანბანის მიხედვით(არ არის სავალდებულო,შემდეგზე აგიხსნით მაგრამ ეცადეთ მოიძოთ,სორტირება)
def sorted_pl(user_list):
    new = []
    for i in user_list:
        for word in i:
            for alpa in word:
                if alpa in "aeiou":
                    new.append(alpa)
    return sorted(new)
print(sorted_pl([["dato"],["gio"],["tengo"]]))



# 4)შექმენი ფუნქცია რომელსაც გადაეცემა რაიმე რიცხვი,შენი დავალებაა 0 დან ამ რიცხვამდე დაითვალო 3 ის გამოტოვებით FOR LOOP/WHILE LOOP
def num(user_int):
    for i in range(0,user_int , 3):
        print(i)
print(num(int(input("enter num:"))))

nin = 0
def nun(user_int):
    while nun != user_int:
        nin +=3
    return nin
print(nun(int(input("enter num:"))))    
# 5)შექმენი ფუნქცია რომელსაც გადაეცემა ერთი მთლიანი დიდის ტრინგი,ამ სტრინგშ სიტყვები დააშორე % ამ ნიშნით,შენი დავლებაა ეს სტრინგი აქციო სიად,შემდეგ შეამოწმო თუ ამ სიაში მყოფი ელემენტი დგას ლუწ ინდექსზე ჩაამატე ახალ სიაში,შემდეგ თქვენი დავალება იქნება რომ ეს სია გადაიყვანოთ ისევ სტრინგში და ეს სიტყვები გამოყო ერთმანეთსგან სფეისებით
def splited_str(user_str):
    new_user = user_str.split()
    new =  '%'.join(new_user)
    new_list = []
    for i in range(0,len(new),2):
        new_list.append(new_user[i])
    return ' '.join(new_list)
print(splited_str("goal oriented academy"))