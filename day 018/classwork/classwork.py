# 1)შექმენი ფუნქცია რომელსაც გადაეცემა სხვადასხვა მონაცემეებით სავსე სია,თქვენი დავალებაა ახალ სიაში ჩააამატოთ მხოლოდ სტრინგ ტიპის მონაცემები
# def onl_str(user_str):
#     result = []
#     for i in user_str:
#         if type(i) == str:
#             result.append(i)
#     return result
# print(onl_str["dato" , 5 , 5.6 , True])



# 2)შექმენი ფუნქცია რომელსაც გადაეცემა რიცხვებით სავსე სია,თქვენი დავალებაა იპოვოთ მხოლოდ 50 ზე მეტი ტიცხვების საშუალო არითმეტიკული
def average(list1):
    result1  = []
    result = 0
    for i in list1:
        if i > 50:
            result1.append(i)
            result +=1
    return result // len(result1)

print(average([1,5,50,65,34,545,43356,1223,7]))
