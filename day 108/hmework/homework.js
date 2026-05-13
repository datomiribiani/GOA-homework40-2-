/*
1)კომენტარის სახით ახსენით თუ რა ფუნქციები ვისწავლეთ მონაცემთა ტიპის შესაცვლელად ,ჩამოწერე ყველა მათგანი
Number = gadayavs stringi ricxvad ogond saxeli ara cifri
parseInt gadayavs frchxilebshi mocemuli stingi numbershi
parseFloat = gadayavs frchxilebshi mocemuli mnishneloba numbershi
 =======
String = gadayavs monacemi stingshi
.tostring =gadayavs monacemi stingshi magram wertilis marcxena adgilas
2) 
მომხმარებელს შემოატანინე მნიშვნელობა prompt-ით.
გააკეთე:

გადააქციე Number()-ით
გადააქციე parseInt()-ით
გადააქციე String()-ით
გამოიყენე toString() (თუ შესაძლებელია)
დაბეჭდე ყველმათი ტიპები 

let name = prompt("enter number")
let name1 = prompt("enter number")
let name2 = prompt("enter str")
late name3 = prompt("enter str")
console.log(Number(name))
console.log(String(name))
console.log(parseInt(name))
meotxwe araa shesadzlebeli radgan egreve wertilis marcxena mxares idgmeva

3)მომხმარებელს შემოატანინე ორი მნიშვნელობა,შენი დავალებაა რომ იპოვო ამ რიცხვების ჯამი
let name1 = Number(prompt("enter number"))
let name2 = Number(prompt("enter number"))
console.log(name1 + name2)

4)მომხმარებელს შემოატანინე მნიშვნელობები შენს შესახებ --> სახელი გვარი ... და interpolation ით შექმენი წინადადება 
let name = prompt("enter name")
let surname = prompt("enter surname")
let age = Number(prompt("enter age"))
console.log(`my name is ${name} , my surname is ${surname} and my age is ${age})

5)მომხმარებელს შემოატანინე რაიმე რიცხვი,შემდეგ გადააქციე ეს სტრინგი რიცხვი ნამბერად შესაბამისი მეთოდით და დაბეჭდე მისი ტიპი
let num = Number(prompt("enter num"))
console.log(typeof num)

6)მომხმარებელს შემოატანინე რაიმე ნამბერ ტიპის მონაცემი,შენი დავალებაა რომ გადააქციო ეს რიცხვი სტრინგად და დაბეჭდო მისი ტიპი
let num = prompt("enter num")
console.log(typeof num)

7)მომხმარებელს შემოატანინე 4 ნამბერ ტიპის მონაცემი,შენი დავალებაა რომ მოახდინო ამ რიცხვების კონკატინაცცია,გამოიყენე შესაბამისი მეთოდები
let name1 = Number(prompt("enter num"))
let name2 = Number(prompt("enter num"))
let name3 = Number(prompt("enter num"))
let name4 = Number(prompt("enter num"))
console.log(String(name1) + String(name2)+  String(name3) + String(name4))

8)მომხმარებელს შემოატანინე ორი რიცხვი, შენი დავალებაა კონსოლში გამოიტანო რამდენია პირველი ამ ორი რიცხვის გაყოფისას მიღებული ნნაშთი(გამოიყენე შესაბამისი ფუნქცია და მათემატიკური ოპეტაროტი-->გადახედეთ გავლილს)
let num = Number(prompt("enter num"))
let num1 = Number(prompt("enter num"))
console.log(num % num1)

9)მომხმარებელს შემოატანინე ორი რიცხვი,შენი დაალებაა გაიგო ამ ორი რიცხვის ნამრავლი
let num = Number(prompt("enter num"))
let num1 = Number(prompt("enter num"))
console.log(num * num1)
10)მომხმარებელს შემოატანინე 5 რიცხვი,შენი დავალებაა გაიგო რამდენია ამ რიცხვების საშვალო არითმეტიკული(მოიძიეთ თუ არ იცით რა არის საშვალო არითმეტიკული)
let num = Number(prompt("enter num"))
let num1 = Number(prompt("enter num"))
let num2= Number(prompt("enter num"))
let num3 = Number(prompt("enter num"))
let num4 = Number(prompt("enter num"))
console.log((num + num1 + num2 + num3 + num4 ) / 5 )

11)შექმენი ცვლადი სადაც მომხმარებელი შემოტანს სტრინგს,შემდეგ დაბეჭდე მისი ტიპი
შემდეგ შენი დავალებაა ეს ცვლადი განაახლო ახალი მომხმარებლის მიერ შემოყვანილო მნიშვნელობით რომელიც იქნება უკვე რიცხვი,შემდეგ დაბეჭდე მისი ტიპიც
let str = prompt("enter str")
console.log(typeof str)
str = Numer(prompt("enter num"))
console.log(typeof str)

12)მომხმარებელს შემოატანინე რაიმე სახელი,შენი დავალებაა რომ გადაიყვანო ეს სახელი დიდ ასოებში და გამოიტანო კონსოლში
let name = prompt("enter name")
console.log(name.toUppercase())
13)მომხმარებელს შემოაყვანინე რაიმე სახელი,შემდეგ შემოატანინე რაიმე ასო
შენი დავალებაა გაიგო იწყება თუ არა მომხმარებლის მიერ შემოტანილის სახელი მის მიერ შემოყვანილ ასოზე
let name = prompt("enter name")
let name1 = prompt("enter aso")
console.log(name.StartWith(name1))

14)მომხმარებელს შემოატანინე რაიმე სახელი ოღონდ დიდი ასოებით,შენი დავალებაა გადააქციო ეს სახელი პატარა ასოებად და გამოიტანო კონსოლში
let name = prompt("enter name")
console.log(name.toLowercase())

15)მომხმარებელს შემოატანინე რაიმე სტრინგი რასაც გარშემო ექნება სფეისები,შენი დავალებაა დააკონსოლლოგო ეს სტრინგი სფეისების გარეშე
let name = prompt("       enter name        ")
console.log(name.trim())

*/
