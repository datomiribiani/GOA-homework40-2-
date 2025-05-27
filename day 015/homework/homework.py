# 1)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი,შენი დავალებაა ამ სტრინგიდან ამოშალო კენტ იდექსზე მდგომი ასოები და დააბრუნო სტრინგი მათ გარეშე
def str1(user_str):
    for i in user_str:
        i.remove[3]
    return i
print(str1("dato", "gio" , "tengo"))



# 2)შექმენი ფუნქცია რომელსაც დაგაეცემა სია,შენი დავალებაა ამ სიიდან ამოშალო კენტ ინდექსზე მდგომი მხოლოდ კენტი რიცხვები და დაამატო ეს რიცხვები ახალ სიაში
def num(listt):
    result = []
    for i in range(len(listt)) :
        if i %2 == 0:
            result += listt[i]
    return result
print(num[1,2,3,4,5,6,7,8,9,10])

# 3)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი --> "hidroeleqtrosadguri" ,თქვენი დავალებაა ამოშალოთ ამ სტრინგიდან მხოლოდ ხმოვნები და დააბრუნოთ ეს სტრინგი ხმოვნების გარეშე
def xmovani(user_xm):
    result = ""
    for i in user_xm:
        if i in "aeiou":
            result += i
    return result
print(xmovani("hidroeleqtrosadguri"))

# 4)შექმენი ფუნქცია რომელიც მომხმარებელს შემოატანინებს რიცხვს და სტრინგს,თქვენი დავლაებაა გამოიტანოთ მომხმარებლის შემოტანილი სტრინგიდან მომხმარებლის შემოტალინ რიცხვზე(ინდექსზე )მდგომი ასო
# aso = int(input("enter your num:"))
# sityva = input("enter your num:")
# def aso_sityva(aso_sityv):
#     result = ""
#     for i in aso_sityv:
#         if aso == sityva:



# 5)შექმენი ფუნქცია რომელსაც გადაეცემა სია,თქვენი დავალებაა სიიდან ამოშალოთ მხოლოდ ის სიტყვები რომლის სიგრძეც ნაკლებია 5 ზე
def list2(user_list):
    for i in user_list:
        result = ""
        if i < 5 in "agsdsdsdw":
            i.remove(result) 
    return result
print(list2("datomagari" "kacia" "dad" "sbf"))