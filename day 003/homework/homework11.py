# BONUS:
# 12) მომხმარებელს შემოატანინეთ სტრინგი და for loop-ის საშუალებით შეაბრუნეთ ეს სტრინგი. შემდეგ გაარკვიეთ არის თუ არა პალინდრომე. (for loop-ით შემოატრიალეთ  და პალინდრომე არის ისეთი სიტყვა რომლის საწყისი ვერსიაც ემთვევა შებრუნებულს ) 
costumer = input("enter your str:")
res = ""
for i in costumer :
    res  += i
if res == res[: : -1] :
    print(True)
else :
    print(False)