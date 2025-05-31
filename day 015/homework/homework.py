# 1)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი,შენი დავალებაა ამ სტრინგიდან ამოშალო კენტ იდექსზე მდგომი ასოები და დააბრუნო სტრინგი მათ გარეშე
# def str1(user_str):
#     for i in user_str:
#         i.remove
#     return i
# print(str1("dato", "gio" , "tengo"))



# 2)შექმენი ფუნქცია რომელსაც დაგაეცემა სია,შენი დავალებაა ამ სიიდან ამოშალო კენტ ინდექსზე მდგომი მხოლოდ კენტი რიცხვები და დაამატო ეს რიცხვები ახალ სიაში
# def num(listt):
#     result = []
#     for i in range(len(listt)) :
#         if i %2 == 0:
#             result.remove(listt[i])
#     return result
# print(num[1,2,3,4,5,6,7,8,9,10])

# 3)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი --> "hidroeleqtrosadguri" ,თქვენი დავალებაა ამოშალოთ ამ სტრინგიდან მხოლოდ ხმოვნები და დააბრუნოთ ეს სტრინგი ხმოვნების გარეშე
# def xmovani(user_xm):
#     result = ""
#     for i in user_xm:
#         if i not  in "aeiou":
#             result += i
#     return result
# print(xmovani("hidroeleqtrosadguri"))

# 4)შექმენი ფუნქცია რომელიც მომხმარებელს შემოატანინებს რიცხვს და სტრინგს,თქვენი დავლაებაა გამოიტანოთ მომხმარებლის შემოტანილი სტრინგიდან მომხმარებლის შემოტალინ რიცხვზე(ინდექსზე )მდგომი ასო



# 5)შექმენი ფუნქცია რომელსაც გადაეცემა სია,თქვენი დავალებაა სიიდან ამოშალოთ მხოლოდ ის სიტყვები რომლის სიგრძეც ნაკლებია 5 ზე
def list2(user_list):
    result = []
    for i in user_list:
        if len(i)  >= 5 :
            result.append(i) 
    return result
print(list2(["datomagari", "kacia" ,"dad", "sbf"]))