# 3) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა მომხმარებელის შემოტანილი რიცხვი მნიშნველობად და გაარკვიეთ ამოდის თუ არა ფესვი არ მირცხვიდან.
no_num = int(input("enter your number:"))
def num(pesvi):
    if no_num < 0 :
        return "ar amodis"
    elif no_num == 0:
        return "0 udris"
    else:
        return "amodis"
print(num(no_num))
        