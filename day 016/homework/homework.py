# 1) კაჰუტზე რა საკითხებიც შეგხვდათ გადაიმეორეთ კარგად.
print("kahutis sakitxebi gadavimeore")

# 2) კომენტარის სახით ახსენით რას ნიშნავს ქეის სენსიტიური, string, float, boolean, integer, list. 
print("qeisensitiuri aris rodesac vwert magalitad cvlads did da patara asoebs didi mnishneloa aq")
print("str aris ricxvebi")
print("float aris atwiladi")
print("bool aris true and false")
print("int aris prwyalebshi mocemuli raime mnishneloba")
print("list aris sia ")

# 3) შექმენით ფუნქცია რომელსაც გადაეცემა მომხმარებლის შემოტანილი სახელი. იმ შემთხვევაში თუ თქვენი სახელები ემთხვევა ქეის სენსიტიურობის დაიგნორების შემთხვევაშიც, მაშინ დააბრუნოს: გამარჯობა {სახელი}!, სასიამოვნოა თქვენი გაცნობა. სხვა შემთხვევაში გამარჯობა {სახელი}! 
name = input("enter your name:")
my_name = "dato"
def name1(user_name):
    if my_name == user_name :
        return "hello " + user_name + "sasiamovnoa sheni gacnoba"
    else:
        return "hello" + user_name
print(name1(name))


# 4) შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ სიტყვას ასო a-ზე გახლიჩავს და დააბრუნეთ სიის სახით.
word = input("enter word:")
def word1(user_word):
    list1 = []
    for i in user_word:
        if i == user_word in "a":
            user_word.remove("a")
            list1.append(i)
    return list1
print(word1(word))
# 5) შექმენით ფუნქცია, რომელიც მომხმარებელს შემოატანინებს სახელს სანამ არ შემოიტანს თქვენს სახელს. თან ჩაამატეთ ახალ სიაში. და დააბრუნეთ ეს სია და რამდენი ელემენტისგან შედგება.
name = input("enter your name")
def name2(user_name):
    my_name1 = "dato" 
    list3 = [] 
    while user_name == my_name1:
        list3.append(user_name)
    return list3
print(name2(name))

# 6) მომხმარებელს შემოატანინეთ რიცხვი. შემდეგ სიტყვა სანამ არ შემოიტანს 'გაჩერდი!', ეგ ყველაფერი დაამატეთ ახალ სიაში და ამ სიიდან მომხმარებლის შემოტანილი რიცხვი რაც არის, იმაზე მდგომი სიტყვის ჩათვლით გამოიტანეთ ამ სიიდან სიტყვები.



