#1 შექმენით ფუნქცია რომელიც შეამოწმებს არგუმენტად გადაცემულ სტრინგში თუ არის რიცხვი.
def str1(user_int):
    numbers = "0123456789"
    for i in user_int:
        if i in numbers:
            return i
print(str1("goabest1"))

#2 შექმენით ფუნქცია რომელიც შეაბრუნებს სიის ელემენტებს, (for loop-ით)
def list1(user_list):
    result = []
    for i in range( len(user_list),0 , -1 ):
        result.append(i)
    return result
print(list1([1,2,3,4,5,6,7,8]))
#3 შექმენით ფუნქცია რომელიც შეამოწმებს არის თუ არა არგუმენტად გადაცემულ სტრინგში ერთი დიდი ასო მაინც
def big(user_list):
    result = []
    for i in user_list:
        if i == i.upper():
            result.append(i)
    return result
print(big("DoaIsbest"))

#4 შექმენით ფუნქცია რომელიც შეამბრუნებს მომხმარებლის შემოტანილ სიტყვას
def word(user_word):
    return user_word[::-1]
print(word("goabest"))

#5 შექმენით სია, სადაც გამოიტანთ ელემენტებს მეორე ინდექსიდან ბოლომდე 3-ის გამოტოვებით
list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
print(list1[2::3])