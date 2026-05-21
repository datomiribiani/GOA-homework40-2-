/*1)შექმენი ორი ცვლადი a და b.
გამოიტანე:
let a = 14
let b = 9
console.log(a > b)
console.log(a < b)
console.log(a >= b)
console.log(a <= b)
a > b
a < b
a >= b
a <= b

2)შექმენი ორი რიცხვი და შეამოწმე ტოლი არიან თუ არა == ოპერატორით.
let nm = 15
let nn = 16
console.log(nm == nn)

3)ექმენი ორი განსხვავებული რიცხვი და შეამოწმე !== ოპერატორით განსხვავდებიან თუ არა.
let nn = 343
let ww = 374
console.log(nn !== ww)

4)მომხმარებელს შემოატანინე ასაკი prompt-ით.
შეამოწმე:
let name = Number(prompt("enter num"))
if(name >= 18){
    console.lg(name)
}
არის თუ არა 18-ზე მეტი
არის თუ არა 18-ის ტოლი

5)მომხმარებელს შემოატანინე პაროლი.
შეამოწმე ტოლია თუ არა "admin123"-ის.
let pw = prompt("enter password")
if(pw === "admin123" ){
    console.log(pw)
}


6)შექმენი ცვლადი temperature.
შეამოწმე:
let temperature = 0
console.log(temperature >30 || temperature <0)
მეტია თუ არა 30-ზე
ნაკლებია თუ არა 0-ზე

7)მომხმარებელს შემოატანინე რიცხვი.
შეამოწმე:
let name = Number(prompt("entr num"))
console.log(name  > 100 || 50)
არის თუ არა 100-ზე დიდი
არის თუ არა 50-ზე ნაკლები

8)შექმენი ორი სტრინგი:

let name1 = "Goga"
let name2 = "goga"
console.log(name1 === name2)
შეამოწმე ტოლი არიან თუ არა.

9)შექმენი ორი რიცხვი და გამოიტანე რომელია უფრო დიდი მხოლოდ შედარების ოპერატორებით.
let n = 10
let b = 11
console.log(n <= b)

10)შექმენი ცვლადი:

let x = "5"
let y = 5

console.log(x == y)
console.log(X === Y)
შეამოწმე:

x == y
x === y

11)მომხმარებელს შემოატანინე სახელი.
თუ სახელის სიგრძე (length) მეტია 5-ზე:
let name = prompt("enter name")
if (name.length > 5){
    console.log("გრძელი სახელია")
}else{
    console.log("მოკლე სახელია ")
    }
გამოიტანე "გრძელი სახელია"

სხვა შემთხვევაში:

"მოკლე სახელია"

12)მომხმარებელს შემოატანინე ტექსტი.
თუ ტექსტი მთლიანად პატარა ასოებითაა:
let name =prompt("enter name")
if (name == name.tolowercase()){
    console.log("patara asoebi")
}console.log("didi asoebi")

გამოიტანე "პატარა ასოებია"

სხვა შემთხვევაში:

"არის დიდი ასოებიც"

13)მომხმარებელს შემოატანინე პაროლი.
თუ პაროლის სიგრძე მინიმუმ 8-ია:
let password = prompt("enter passord")
if(password.length >= 8){
    console.log("dzlieri passwordi")
}else{
    console.log("sustii")
    }

"ძლიერი პაროლი"

სხვა შემთხვევაში:

"სუსტი პაროლი"

14)მომხმარებელს შემოატანინე username.
თუ username-ის სიგრძე 4-ზე ნაკლებია:
let name = prompt("enter username")
if(name.length < 4){
    console.log("moklea")
}else{
    console.log("username sworia")
    }
"ძალიან მოკლე username"

სხვა შემთხვევაში:

"username სწორია"

15)მომხმარებელს შემოატანინე ტექსტი.
თუ ტექსტი ტოლია თავის toUpperCase() ვერსიის:
let name = prompy("enter text")
if(name === name.touppercase()){
    console.log("yvela assso didida")
}else{
    console.log("yvela aaso didi araa")
    }

"ყველა ასო დიდია"

სხვა შემთხვევაში:

"ყველა ასო დიდი არაა"
*/