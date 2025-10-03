# 6)დაწერეთ ფუნქცია multiples_of_five(lst), რომელიც აბრუნებს სიას, სადაც არის მხოლოდ ის რიცხვები, რომლებიც იყოფა 5–ზე და 3-ზ
def multiples_of_five(lst):
    addd = []

    for i in lst:
        if i % 5 ==0 and i %3 ==0:
            addd.append(i)
    return addd
print(multiples_of_five([1,2,3,4,5,6,7,8,9]))
