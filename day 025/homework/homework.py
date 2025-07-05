#1 შექმენით სია რომელიც სავსე იქნება სტრინგებით და დაასორტირეთ ეს სია ანბანის მიხედვით.
list1 = ['dgusgdygfdsw' , "fgsdwljdiyrfn" , "abdgfefsgvfrgre" , "bfdfgfs"]
print(sorted(list1 , reverse=False))
#2 შექმენით სია რომელიც სავსე იქნება რიცხვებით და დაასორტირეთ ეს სია ნიშნების რაოდენობის მიხედვით. (ჯერ ორნიშნა, მერე ერთნიშნა კლებადობით)
list2 = [1,2,3,45,65,6,4,43,56,76,5,3,4,5,76,6,5,5,43,45,76,6,4,14]
print(sorted(list2, reverse=True ))

#3 შექმენით სია რომელიც სავსე იქნება სტრინგებით და დაასორტირეთ ეს სია ასო კ-ს რაოდენობის მიხედვით
list3 = ["datokabuniabelikekkkkkkkkkk"]
def cont(user_word):
    return user_word.count('k')
print(sorted(cont, reverse=True , key=list3))
#4 შექმენით სია რომელიც სტრინგებით იქნება სავსე. გადაუარეთ ამ სიას და თითოეული ელემენტის კენტ ინდექსზე მყოფი სიმბოლოები გაერთიანეთ და ისე ჩაამატეთ ახალ სიაში.
list4 = ["dato" , "zviangi", "zviadi"]
list0= []
for i in list4:
    if i.index(3):
        list0.append(i)
print(list0)

#5 შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ წინადადებაში ხმოვან ასოებს გაფილტრავს.
def filt(user_str):
    le1 = []
    for i in user_str:
        if i not in "aeiou":
            le1.append(i)      
    return le1
print(filt(input("enter str:")))