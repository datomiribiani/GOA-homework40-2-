# 1)შექმენი სია,სადაც მოათავსებთ სახელებს,თქვენი დავალებაა დაასორტიროთ ეს სია სიაში მტოფი სახელების სიგრძის მიხედვით და შემოატრიალოთ უკუღმა
list1 = ["dato" , "name", "gabana" , "kasjoho"]
x = sorted(list1 , key=len , reverse= True)
print(x)



# 2)შექმენი ფუნქცია რომელსაც გადაეცემა სია სადაც მოთავსებული იქნება სხვადასხვა მონაცემთა ტიპები,შენი დავალებაა რომ ამ სიიდან ამოიღო ინტეჯერებიდ ა მოათავსო ცალკე ახალ სიაში,ასევე უნდა მაოიღო სტრინგებიც და ცალკე სიაში,შენი დავალებააა ეს ორი სია დაასორტირო,სტრინგების სია დაასორტირე ანბანის მიხედვით და შემოატრიალე,და რიცხვების სია დაასორტირე ზრდადობის მიხედვით
# lis = ["sdgsdgd", "deshhfdbefhb" , 'afddfd' , 121, 2,32,2,5,45,45,6,56,5,6,56,6]
def sort(user_user):
    new = []
    new2 = []
    for i in user_user:
        if type(i) == str:
            new.append(i)
    for a in user_user:
        if type(a) == int:
            new2.append(a)
    z = sorted(new2)
    v = sorted(new, key=len , reverse=True)
    return z ,v
print(sort(["sdgsdgd", "deshhfdbefhb" , 'afddfd' , 121, 2,32,2,5,45,45,6,56,5,6,56,6]))
