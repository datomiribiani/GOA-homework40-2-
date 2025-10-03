# 3)დაწერეთ ფუნქცია double_numbers(lst), რომელიც აბრუნებს ახალ სიას, სადაც თითოეული ელემენტი ორმაგია.
def double_numbers(lst):
    duble =[]
    for i in lst:
        if i > 0:
            duble.append(i*i)
        if i == 0:
            duble.append(i)
        if i < 0:
            duble.append(i*i)
    return duble
print(double_numbers([1,2,3,4,5,6,7,9,0,11,2,3,5]))
