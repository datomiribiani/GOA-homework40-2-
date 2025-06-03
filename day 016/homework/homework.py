# 1) კაჰუტზე რა საკითხებიც შეგხვდათ გადაიმეორეთ კარგად.
print("kahutis sakitxebi gadavimeore")

# 2) კომენტარის სახით ახსენით რას ნიშნავს ქეის სენსიტიური, string, float, boolean, integer, list. 
print("qeisensitiuri aris rodesac vwert magalitad cvlads did da patara asoebs didi mnishneloa aq")
print("str aris prwyalebshi mocemuli raime mnishneloba ")
print("float aris atwiladi")
print("bool aris true and false")
print("int aris mteli ricxvebi")
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
   return user_word.split("a")
print(word1(word))
# 5) შექმენით ფუნქცია, რომელიც მომხმარებელს შემოატანინებს სახელს სანამ არ შემოიტანს თქვენს სახელს. თან ჩაამატეთ ახალ სიაში. და დააბრუნეთ ეს სია და რამდენი ელემენტისგან შედგება.
name = input("enter your name")
def name2(user_name):
    my_name1 = "dato" 
    list3 = [] 
    while user_name != my_name1:
        input("try again")
        list3.append(user_name)
    return list3 , len(list3) 
print(name2(name))
# 6) მომხმარებელს შემოატანინეთ რიცხვი. შემდეგ სიტყვა სანამ არ შემოიტანს 'გაჩერდი!', ეგ ყველაფერი დაამატეთ ახალ სიაში და ამ სიიდან მომხმარებლის შემოტანილი რიცხვი რაც არის, იმაზე მდგომი სიტყვის ჩათვლით გამოიტანეთ ამ სიიდან სიტყვები.
number = int(input("enter your num"))
str1 = input("enter your str")
def wor_num(user_word , number1):
    result = []
    while user_word != "stop":
        input("try again:")
        result.append(user_word)
    return result[0:number1]
print(wor_num(str1,number))
