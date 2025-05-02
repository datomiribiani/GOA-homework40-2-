# 1)შექმენით სია რომელსაც გადასცემთ სამ ხილის სახელს,შენი დავალებაა ჩაანაცვლო ეს ხილის სახელები ქვეყნის სახელებით
list = ['vashli', "atami", "firtoxali"]
list[0] = "saqartvelo"
list[1] = "saprangeti"
list[2] = "espaneti"
print(list)

#  2)შექმენით სტრინგი და სცადეთ პირველ ინდექსზე მდგომი ასო შეცვალოთ ასო ბგრეა "უ"-ით და ნახე შედეგი,ასევე კომენტარის სახით ახსენი რა მოხდა
list = "fato"
list[0] = "u"
# erori radgan am fato ar aris motavsebuli siashi



# 3)შექმენით ცვლადი სადაც შეინახავთ სიტყვა "hidroeleqtrodadguri" ,თქვენი დავალება იქნება რომ გამოიტანოთ მხოლოდ "hodroele" გამოიყენეთ სლაისინგი
hidro = "hidroeleqtrodadguri" 
print(hidro[:8])

# 4)შექმენით სია სადაც შეინახავთ 10 სახელს , თქვენი დავალებაა ამ სიაში გამოიტანოთ ელემენტები სამი step ის გამოტოვებით
name = ["dato", "dato", "dato", "dato", "dato", "dato", "dato", "dato", "dato", "dato"]
print(name[::3])