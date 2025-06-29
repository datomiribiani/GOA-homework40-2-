#1 შექმენით სია რომელიც იქნება რიცხვებით სავსე და არეული თანმიმდევრობით. დალაგეთ რიცხვები კლებადობით.
list1 = [6,2,3,7,4,7,3,5,31,4,6,8,3,56]
print(sorted(list1, reverse=True))

#2 შექმენით სია რომელიც იქნება სტრინგებით სავსე და დაალაგეთ სიგრძის მიხედვით შებრუნებულად.
list2 = [ "gio" , "luka" , "hidroelelqtrosadguri" , "kvaxi" , "nigzari" , "zviangi"]
print(list2 )

#3 შექმენით სია, ამ სიაში უნდა იყოს სტრინგები და ეს სია დაასორტირეთ ასო ა-ს რაოდენობის მიხედვით.

def nm(user_nm):
    return user_nm.count("a")
list3 = ["dato" , "hidroni","azoti",'jangbadi']
print(sorted(nm , reverse=True, key=list3 ))


#4 შექმენით სია, ამ სიაში უნდა იყოს სტრინგები და ეს სია დაასორტირეთ ასო G-ს რაოდენობის მიხედვით კლებადობით. 
list4 = ["datogabuniabelikeggg"]
def cont(user_word):
    return user_word.count('g')
print(sorted(cont, reverse=True , key=list4))