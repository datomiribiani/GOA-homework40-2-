# 1)შექმენით სია,სადაც მოთავსებული გექნებათ სახელები,თქვენი დავალებაა გამოიტანოთ მხოლოდ მენულე და ბოლო ინდექსზე მდგომი ელემენტები
list_name = ["dato" , "gio", "lekso" , "tengo"]
print(list_name[0])
print(list_name[3])
# 2)შექმენი სია სადაც შეინახავ სახელებს,კომენტარის სახით დაწერე ამ ელემენტების ინდექსები ოღონდ უარყოფით რიცხვებში
# list = [dato0 gio-1 lekso-2 tengo-3]

# 3)შექმენი სია სადაც შეინახავთ სახელებს,შენი დავალებაა გამოიტანო სიაში მყოფი თითოეული ელემენტი ცალ ცალკე,გამოიყენე for loop
list_name = ["dato" , "gio", "lekso" , "tengo"]
go = 0   
for i in list_name:
    go += 1
print(go , list_name)

# 4)შექმენი ცვლადი სადაც შეინახავ სტრინგს,შენი დავალებაა გამოიტანო ამ სტრინგიდან თითოეული ასო ცალ ცალკე,გამოიყენე for loop
list_name = ["dato" , "gio", "lekso" , "tengo"]
print(list_name[0])
print(list_name[1])
print(list_name[2])
print(list_name[3])
# 5)შექმენი სია სადაც მოათავსებ 10 სახელს,შენი დავალებაა გამოიტანო ამ სიაში 2 ინდექსიდან 7 ინდექსამდე ელემენტები გამოიყენე slicing
list_name = ["dato" , "gio", "lekso" , "tengo" ,"dato" , "gio", "lekso" , "tengo" ,"dato" , "gio"]
list_name =[2 : 8]
print(list_name)
# 6)შექმენით ცვლადი სადაც შეინახავთ სტრინგს "konstantinopoli",შენი დავალებააა გამოიტანო ამ სტრინგიდან ბოლო 8 ასო,გამოიყენეთ slicing
list_name2 = ["konstantinopoli"]
list_name2[8 : 14]
print(list_name2)

# 7)შექმენით სია სადაც მოათავსებთ ხილის სახელებს,თქვენი დავალებაა ყველა ხილის სახელი ჩააანაცვლოთ ქვეყნის სახელებით
list_country = ["fortoxali" ,"valshi" , "atami"]
list_country[0] = "saqartvelo"
list_country[1] = "saqartvelo"
list_country[2] = "saqartvelo"
# 8)მე-7 ე დავალების მსგავსად,ოღონდ შექმენით სტრინგი და სცადე სტრინგში მყოფი ბოლო ინდექსის შეცვლა ასო ბგერა "k" -ით,კომენტარის სახით დაწერეთ რატომ ვერ 
# ვცვლით სტრინგებს იმის შემდეგ რაც მას ვქმნით
list_name = ["dato"]
list_name[-3] = "k"
print(list_name)

# 9)შექმენით ცვლადი სადაც შეინახავთ სტრინგს "kurdgelia"-თქვენი დავალებაა ამ სტრინგიდან გამოიტანოთ შემდეგი სტრინგი --> "gela"
list_ragaca = ["kurdgela"]
list_ragaca[list_ragaca] = "gela" 
print(list_ragaca)
# 10)შექმენით სია სადაც შეინახავთ რიცხვებს [10,5,20,40] თქვენი დავალებაა იპოვოთ ამ სიაში მყოფი რიცხვების ჯამი
list_num = [10,5,20,40]
sum = 0
for i in range(list_num):
    sum += i
print(sum)