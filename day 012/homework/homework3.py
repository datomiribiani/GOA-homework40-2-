# 4) შექმენით ფუნქცია, სადაც მომხმარებლის შემოტანილ ტექსტს შეაბრუნებთ ისე რომ თითოეულ ასოს შორის - (ტირე) იყოს. (სლაისინგის გარეშე სცადეთ) 
# მაგ: თუ მომხმარებელმა შემოიტანა Goa შედეგი უნდა იყოს a-o-G


def reverse_string(user):
    result = ''
    for i in user :
        result = i + "-" + result
    return result
print(reverse_string("goal academy"))
