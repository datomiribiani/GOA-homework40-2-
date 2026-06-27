// 1)შექმენი Function Expression --> square, რომელიც მიიღებს რიცხვს და დააბრუნებს მის კვადრატს.გამოიყენე Math
// გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით და ნახე შედეგი

const gam = function(square){
    return Math.pow(square,square)
}
gam(12)
gam(12)
gam(14)
// 2)შექმენი Function Expression --> maxNumber, რომელიც მიიღებს ოთხ რიცხვს და დააბრუნებს მათგან დიდს.
// გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით და ნახე შედეგი

const greet = function(maxnumber) {
    return Math.max(maxnumber)
}

greet(12,12,212,1)
greet(1,12,121212,121)
greet(2231212,33,323,3)
greet(1,33,22,2)

// 3)პაროლის შემოწმება
// შექმენი Function Expression --> checkPassword, რომელიც დააბრუნებს true თუ პაროლი:
// მინიმუმ 8 სიმბოლოა და მთავრდება ასო "a" ზე
// სხვა შემთხვევაში დააბრუნოს false.

const pas = function(pssword){
    password.length > 8 && password.endsWith(a)?"ture":"fasle"
}
pas("dudhdda")
pas("egdfgddd")

// 4)შექმენი Function Expression --> isLuckyNumber, რომელიც დააბრუნებს true თუ რიცხვი:
// იყოფა 3-ზე
// და იყოფა 5-ზე
// სხვა შემთხვევაში დააბრუნოს false.(use ternary)
// გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით და ნახე შედეგი

const ps = function(isLuckyNumber){
    isLuckyNumber %3===0 && isLuckyNumber %5===0?"true":"false" 
}

// 5)შექმენი Function Expression--> checkWord, რომელიც მიიღებს სიტყვას.
// თუ სიტყვა არის "javascript" დააბრუნოს:
// "Access Granted"
// სხვა შემთხვევაში:
// "Access Denied"

const pass = function(chekword){
    chekword === "javascript"?"access granted":"acces denied"
}


// # arrow=======================================


// 6)შექმენი Arrow Function --> isAdult, რომელიც მიიღებს ასაკს და დააბრუნებს:
// "Adult" თუ ასაკი 18 ან მეტია
// "Minor" სხვა შემთხვევაში
// ternary
// გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით და ნახე შედეგი

const arro = isadult =>isadult > 18 ? "adult":"minor"{
   
}

arro(12)
arro(222)
arro(18)
arro(3)

// 7)შექმენი Arrow Function --> rectangleArea, რომელიც მიიღებს სიგრძეს და სიგანეს და დააბრუნებს ფართობს.
// გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით და ნახე შედეგი
const rectangleArea = (wih,heit) => wih * heit{
   
}
rectangleArea(12,12)
rectangleArea(1232,5232)
 

// 8)შექმენი Arrow Function -->  passwordStrength, რომელიც მიიღებს პაროლს:
// თუ პაროლის სიგრძე 8-ზე ნაკლებია და პაროლი მთავრდება ასო "ი" თი→ "Weak"
// თუ 8 ან მეტია და იწყება ასო "გ" თი → "Strong"

const pass = passwordStrength => passwordStrength.length < 8 && passwordStrength.endsWith("i")?"weak" :passwordStrength.length>8 && passwordStrength.startsWith("g") ?"stong":"error" {
 
}

pass('dgfshfhsfdgdgdgd')
pass("gefeudhcfvcf")

// 9)შექმენი Arrow Function -->  startsWith რომელიც მიიღებს რაიმე სტრინგს
// თუ სტრინგი იწყება "გ" თი და მთავრდება "ო" თი და სიგრძე trim() ით მეტია 8 ზე დააბრუნე --> რთული სახელი , სხვა შემთხვევაში მარტივი სახელი
const startss = starts => starts.startsWith("g") && starts.endsWith("o") &&  starts.length.trim() > 8 ?"rtuli saxeli":'martivisaxeli'{

}


// single line arrow =======================================


// 10)შექმენი formatUsername, რომელიც ერთ ხაზში დააბრუნებს username-ს პატარა ასოებით.

const formatUsername = user => ServiceWorker.lowerCase(){
}

formatUsername("DSDFDFDF")

// 11)შექმენი checkCode, რომელიც ერთ ხაზში დააბრუნებს:
// "AccessGranted" თუ კოდი არის "1234"
// "Access Denied" სხვა შემთხვევაში
// ternary

const chekcode = uiser => uiser === "1234"? "Access Granted":"access Denied"{
    
}

// 12)შექმენი isLongText, რომელიც ერთ ხაზში დააბრუნებს true, თუ ტექსტის სიგრძე 10-ზე მეტია. 
const islongtext = yse => yse.length  > 10?"true":"fasle"{
    
}

// 13)შექმენი passedExam, რომელიც ერთ ხაზში დააბრუნებს:
// "Passed" თუ ქულა 51 ან მეტია
// "Failed" სხვა შემთხვევაში

let passexam = exm => exm > 51 ?"passed":"failed"{
    
}

// ternary

// 14)შექმენი freeDelivery, რომელიც ერთ ხაზში დააბრუნებს true, თუ შეკვეთის ფასი 100₾-ზე მეტია. სხვა შემთხვევაში false
// ternary

const freedelivery = yys => yys > 100 ?"true":"false"{
    
}
