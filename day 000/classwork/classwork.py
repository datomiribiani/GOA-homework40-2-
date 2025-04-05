# 1) განმარტეთ რა არის string, integer, float, boolean ტიპები. და მაგალითებიც მიუწერეთ
# 2) შექმენით ცვლადი სადაც თავიდან შეინახავთ სტრინგ ტიპის მონაცემს, შემდეგ ინტეჯერ ტიპის, მერე float ტიპის და ბოლოს bool ტიპის

print("str არის სტრინგი სადაც შეგვიძლია ჩავწეროთ სახელები ბრჭყალებში | int არის ინტეჯერი სადაც ვწერთ მთელ რიცხვებს ბრჭყალების გარეშე | float არის ათწილადი და ლუწი  ციფრები | boolean არის true da folse    ")
print("dat")
print(int("5"))
print(float(2.4))

# 2) შექმენით ცვლადი სადაც თავიდან შეინახავთ სტრინგ ტიპის მონაცემს, შემდეგ ინტეჯერ ტიპის, მერე float ტიპის და ბოლოს bool ტიპის

number_two = "dat"
number_two = 5
number_two = 2.4
number_two = True


# 3) ცვლადში შეინახეთ ინტეჯერ ტიპის მონაცემი, შემდეგ გადააქციეთ float ტიპად და ისე დაპრინტეთ
number_one = 5 
print(float(number_one))



# 4) მომხმარებელს შემოატანინე ასაკი, შემდეგ დაპრინტე რამდენი წელია სხვაობა თქვენ ასაკებს შორის. 

age = int(input("enter tour age: "))
my_age = 14 
print(my_age - age) 



# 5) მომხმარებელს შემოატანინე ტექსტი, შემდეგ რიცხვი. და მომხმარებელი რა რიცხვსაც აირჩევს, იმდენჯერ დაპრინტეთ შემოტანილი ტექსტი
text_text = input("enter your text: ")
num_num = int(input("enter your number: "))
print(text_text *  num_num)


# 6) მომხმარებელს შემოატანინე ორი რიცხვი. ერთი float ტიპის, მეორე int ტიპის. და დაპრინტეთ ყველა შესაძლო მათემატიკური მოქმედება მათ შორის. (+, -, *, /, //, **, %) 

number = float(input("enter your float number:"))
numer2 = int(input("enter  your numer: "))
print(number + numer2)
print(number - numer2)
print(number // numer2)
print(number * numer2)
print(number ** numer2)
print(number % numer2)