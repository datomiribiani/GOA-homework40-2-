# 1) შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა მომხმარებლის შემოტანილი სიტყვა. ხმოვნები სადაც იქნება ! ნიშნით ჩაინაცვლოს და თანხმოვნები *-ით სხვა დანარჩენი სიმბოლო იყოს ისე როგორ იქნება. 
txmn = input("enter your sityva:")
def string1(user_string):
    result = ''
    for string in user_string:
        if txmn ==   "a" + "e" + "i " + "o" + "u":
            return result == "!" 
        else:
            result == "*"
print(string1("dato aeridfkevfkE"))
# 2) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა მომხმარებლის სახელი და ასაკი. შეამოწმეთ თუ ასაკი მეტი არის 18-ზე და მისი სახელი არის თქვენი სახელის ტოლი მაშინ დააბრუნოს თქვენ წარმატებით აიღეთ მართვის მოწმობა. სხვა დანარჩენ შემთხვევაში რომ ჩაიჭრნენ
age_name = int(input("enter your name , age:"))
def age_name(user_string):
    if age_name == 18 or age_name == "dato" :
        return "shen aige martvis mowmoba"
    else:
        "chaiweri"
print(age_name("dato" , 18))

# 3) შექმენით ფუნქცია, რომელიც მომხმარებლის შემოტანილ float ტიპის მოცანემს გახლიჩავს. შედეგი ასე რომ იყოს :  19.27 => 19 + 0.27 
flout = float(input("enter your float :"))
def floute(user_float):
    if flout == 19.27>= 19 + 27:
        return 19.27 >= 19 + 27
print(floute(19.27>= 19 + 27))

# 4) შექმენით ფუნქცია რომელიც მომხმარებელს შემოატანინებს სიტყვას მანამ სანამ არ შემოიტანს 'საკმარისია'ს. ეს შემოტანილი სიტყვები დაამატეთ სიაში და გაფილტრეთ. სიაში უნდა იყოს ისეთი სიტყვები რომლის სიგრძეც არ აღემატება 5-ს და ურევია რიცხვები.
sakmarisia = input("enter tour sakmarisia :" )
def sakm(user_sakmarisi):
    result = []
    while user_sakmarisi == "sakmarisia":
        result += 1
    return result
print(sakm[sakmarisia])
# 5) დაამთავრეთ საკლასოები

# BONUS: შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ რიცხვის ჩათვლით გამოგვიტანს ყველა მარტივი რიცხვის ნამრავლს
martivi = int(input("enter your martivi :"))
def mart(user_martivi):
    result = 0
    for i in user_martivi: 
        result += 1
    return result
print(mart(12345678912))

