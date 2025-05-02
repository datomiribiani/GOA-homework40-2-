# 2) მომხმარებელს შემოატანინე პაროლი მანამ სანამ ამ პაროლის მნიშვნელობა არ იქნება 'GOA BEST' და თუ შემოიტანა პაროლი სწორად, დაპრინტე 'ყოჩაღ, პაროლი სწორია'.
password= input("enter your password:")
while password != "goabest" : 
    input("try again")
if password == "goabest":
    print(True)