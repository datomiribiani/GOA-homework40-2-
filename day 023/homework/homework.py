# 1)კომენტარის სახით ჩამოწერეთ ყველა LIST FUNCTION თან ახსენით რას აკეთებს და თითეულის ქვეშ მოიყვანეთ სათითაო მაგალითები

# append - ამატებს  სიის ბოლოში რაიმე მონაცემს 
list1 = [1,12,1212,12]
list1.append(15)
print(list1)
# remove - შლის სიიდან მონაცემს =
list1 = [1,12,1212,12]
list1.remove(12)
print(list1)
# pop - რომელ ინდექსზე გვინდა ამოვშალოთ სიიდან რაიმე მონაცემი =
list1 = [1,12,1212,12]
list1.pop(3)
print(list1)
# insert - ამატებს მონაცემს ნებისმიერ ადგილას =
list1 = [1,12,1212,12]
list1.insert(4,"mze")
print(list1)
# find - პოულობს რომელ ადგილზეა ინდექსი = 
list1 = [1,12,1212,12]
list1.find(12)
print(list1)
# index - პოულობს ინდექს =
list1 = [1,12,1212,12]
list1.index(1)
print(list1)

# 2)გაიხსენეთ for while / loop პრინციპი,ახსენით კომენტარის სახით ორივეს დანიშნულება,მოიყვანე სათითაო მაგალითი(ორივეთი დაითვალე 50 დან 100 მდე 5 ის გამოტოვებით)
# for loop სათითაოდ გამოაქვს და აბრუნებს რამდენჯერაც გვინდა
# while loop კი სანამ მოქმედება არ შესრულდება მანამდე გამოიტანოს
for  i in range(50,100,5):
    print(i)
# 3)შექმენი ცვლადი და შეინახე რაიმე სტრინგი,შენი დავალებაა WHILE FOR/LOOP გამოყენებით გამოიტანო თითეული ასო ამ სტრინგიდან

def datvla(user_int):
    for i in len(user_int):
        return user_int
print(datvla("gioo"))


def datvla(user_int):
    while user_int == user_int:
        input("try again")
    return user_int
print(datvla("dato"))


# 4)while/for loop გამოყენებით დაითვალე 20,დან 100მდე  // 50 დან 80 მდე 3 ის გამოტოვებით // 
for i in range(20,100):
    print(i)
for i in range(50,80,3):
    print(i)
# 5)მომხმარებელს 10 ჯერ შემოაყვანინე რიცხვი for loop/while loop გამოყენებით  
num = int(input("enter num:"))
for i in range(10):
    print(i,num)

num1= int(input("enter num:"))
while num <10:
    input("try again:")
print("enter num:")