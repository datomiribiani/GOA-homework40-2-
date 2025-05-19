# 1) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა მომხმარებლის შემოტანილი სიტყვა და დაითვლის სიგრძეს  len() ფუნქციის გარეშე.
def length(user_string):
    count = 0
    for i in user_string:
        count +=1
    return count
print(length("academy"))
# 2) შექმენით ფუნქცია რომელაც არგუმენტად გადაეცემა მომხმარებლის შემოტანილი სიტყვა და ამ სიტყვაში დაითვლის ასო "k'ს რაოდენობას. დააიგნოროს ქეის სენსიტიურობა.
# def count_k(user_string):
#     count =0
#     for i in user_string:
#         if i == "k" or i == "K":
#             count +=1
# user = input("enter your str")
# print(count_k(user))


# შექმენით ფუნქცია რომელსაც არგუმენტად სია, ამ სიაში უნდა იყოს სხვადასხვა ტიპის მონაცემები და დაითვალოს რამდენი სტრინგ ტიპის მონაცემი არის
# def str1(user_string):
#     count = 0
#     for i in  user_string:
#         if  type(i) == str:
#             return count 
# print(str1[1212,"dada ", 'dadadadad'])

# 4) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა სია სადაც იქნება სხვადასხვა ტიპის მონაცემი. გაიგეთ ამ სიაში რიცხვების ჯამი
def date(data_type):
    sum =0
    for i in data_type:
        if type(i) == int  or type(i) == float:
            sum += i
    return sum
print(date[1,2,3,323,323.43,54545.54]) 
        

