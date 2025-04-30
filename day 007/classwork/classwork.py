# 1) შექმენი სია სადაც მოთავსებული გექნება მხოლოდ string ტიპის მონაცემები
# list = ["dato" , "zviadi" , 'nugzara"]

# 2) შექმენი სია სადაც მოთავსებული გექნება მხოლოდ integer ტიპის მონაცემები
# list = [12 ,121, 212313, 2312,1]

# 3) შექმენი სია სადაც მოთავსებული გექნება მხოლოდ float ტიპის მონაცემები
# list = [32.3,323.3,3232.4]

# 4)  შექმენი სია სადაც მოთავსებული ყველა მონაცემთა ტიპის ელემენტები
# list1 = [3232,12,"dato", True]

# 5)მოცემული გაქვთ სია ["cat","purple",21,150.6,True] კომენტარის სახით დაწერეთ რომელ ინდექსზე დგას თითოეული ელემენტი
# cat = 0    "purple" = 1  21 = 2   150.6 = 3  True = 4

# 1)მოცემული გაქვთ სია ["fortoxali","gvanca",150.6,True,"fortoxali"] ,თქვენი დავალებაა ამ სიიდან გამოიტანოთ თითოეული ელემენტი ცალ ცალკე,გამოიყენეთ indexing
names =  ["fortoxali","gvanca",150.6,True,"fortoxali"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 2)მოცემული გაქვთ სია ["fortoxali","gvanca",150.6,True,"fortoxali"],შენი დავალებაა "fortoxali" შეანაცვლო "apple" ით და გამოიტანო განახლებული სია ტერმინალში სადაც ფორთოხლის მაგივრად იქნება ვაშლი ანუ "apple"
numers = ["fortoxali","gvanca",150.6,True,"fortoxali"]
numers[0] = "appel"
print(numers)

# 3)მოცემული გაქვთ სია ["fortoxali","gvanca",150.6,"tkbili",True] თქვენი დავალებაა ტერმინალში გამოიტანოთ tkbilifortoxali
nemmers = ["fortoxali","gvanca",150.6,"tkbili",True]
print(nemmers[0] +nemmers[3] )
