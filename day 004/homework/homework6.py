# 7) მომხმარებელს შემოატანინე პაროლი. და ჰქონდეს სამი ცდა.
password = input("enter your password")
my_password = "paroli"
try_nm = 3
while password != my_password:
    while try_nm >0 :
        try_nm -= 1
        input("try again")
