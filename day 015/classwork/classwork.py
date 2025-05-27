# 1)შექმენი ფუნქცია,რომელსაც გადაეცემა სტრინგი --> aleqsandre , თქვენი დავალებაა დააბრუნოთ კენტ ინდექსზე მდგომი ასოები

def nue(sringing):
    result = ""
    for i in range(len(sringing)):
        if i % 2 == 1:
            result += sringing[i]
    return result
print(nue("aleqsandre"))

# 2)შექმენი ფუნქცია რომელსაც გადაეცემა რიცხვებით სავსე სია,თქვენი დავალებაა დააბრუნოთ ახალი სია სადაც გექნებათ მხოლოდ ლუწი რიცხვები

def num(user_num):
    list1 = []
    for i in user_num:
        if i %2 == 0:
             list1.append(i)
    return list1
print(num[1,2,3,4,5,6,7,8,9,10])

# 3)შექმენი ფუნქცია როომელსაც გადაეცემა სტრინგი --> fortoxali,თქვენი დავალებაა დააბრუნოთ თითოეული ასოს ინდექსი სიის სახით (არ გამოიყენოთ len ფუნქცია)

def orange1(orange):
    rest = []
    for i in orange:
        rest.append(orange.find(i))
    return rest
print(orange1("fortoxali"))




# 3)შექმენი ფუნქცია როომელსაც გადაეცემა სახელებით სავსე სია,თქვენი დავალებაა დააბრუნოთ თითოეული ელემენტის ინდექსი(არ გამოიყენოთ len ფუნქცია)

def saxelebi(names):
    rest = []
    for i in names:
        rest.append(names.index(i))
    return rest
print(saxelebi["dato" , "gio" , "luka"])


# 4)შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვებით სავსე სია,თქვენი დავალებაა ამ სიიდან ამოშალოთ კენტი რიცხვები და დააბრუნოთ სია კენტი რიცხვების გარეშე
def sia(user_sia):
    rest = []
    for i in user_sia:
        if i % 2 == 1:
            user_sia.remove(i)
    return rest
print(sia(1,2,3,4,5,6,7,8,9))



