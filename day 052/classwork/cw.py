# 1)ფუნქციამ მიიღოს სტრინგი და შეამოწმოს არის თუ არა ის პალინდრომი (წინიდან და უკნიდან ერთნაირად იკითხება).
# 👉 მაგალითი: "level" → True, "hello" → False
def palin(user):
    for i in user:
        if i[0] == i[0]:
            return True
        else:
            return False
print(palin('level'))
# 2)ფუნქციამ მიიღოს წინადადება (სტრინგი) და დააბრუნოს რამდენი სიტყვაა მასში.
# 👉 "I love Python programming" → 4

# 3)ფუნქციამ მიიღოს სტრინგი და სია აკონტროლოს: დაუბრუნოს მხოლოდ ის სიტყვები, რომლებიც მეტია 3 სიმბოლოზე.
# 👉 "I love Python and AI" → ["love", "Python"]
def sia(user):
    for i in user:
        if len(i) > 3:
            return True
        else:
            return False
print(sia(['i love programing']))





# 7)ფუნქციამ მიიღოს მთელი რიცხვების სია და დააბრუნოს მხოლოდ დადებით რიცხვთა ჯამი, რომლებიც 5-ზე დიდია.
# 👉 [2, 5, 7, 10] → 17
def num(user_num):
    cont=0
    for i in user_num:
        if i > 5:
            cont +=i
    return cont    
print(num([1,2,3,4,5,6,7,8,9]))
# 8)ფუნქციამ მიიღოს მთელი რიცხვების სია და დააბრუნოს სია, სადაც ყველა დადებითი რიცხვი გაზრდილია 1–ით, ხოლო ყველა უარყოფითი შემცირებული 1–ით.
def sh(user):
    rs=[]
    for i in user:
        if i > 0:
            rs.append(i +1)
        elif i < 0:
            rs.append(i -1)
        else:
            rs.append[0]
    return rs
# 9)ფუნქციამ მიიღოს სიტყვების სია და დააბრუნოს სია დაქანცული სიგრძის ზრდის მიხედვით.
# 👉 ["apple", "hi", "banana"] → ["hi", "apple", "banana"]
def sorted1(wrd):
    return sorted(wrd,key=len)