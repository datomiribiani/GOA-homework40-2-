
// 1)შექმენი ფუნქცია greet(name), რომელიც დაბეჭდავს: Hello, name!
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით
function greet(name){
    console.log("hello" + name)
}
name("dato")

// 2)შექმენი ფუნქცია showAge(age), რომელიც დაბეჭდავს: You are age years old.
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით

function showAge(age){
    console.log("you are" + age + "years old"   )
}

age(15)
age(32)
age(12)
age(67)

// 3)შექმენი ფუნქცია sum(a, b), რომელიც დაბეჭდავს ორი რიცხვის ჯამს.
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით
function sum(a, b){
    console.log(a + b)
} 
a(12)
b(14)
a(133)
b(434)
// 4)შექმენი ფუნქცია multiply(a, b), რომელიც დაბეჭდავს ორი რიცხვის ნამრავლს.
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით
function multiply(a, b){
    console.log(a * b)

}

a(143432)
b(14344)
a(1343433)
b(4434344)

// 5)შექმენი ფუნქცია fullName(firstName, lastName), რომელიც დაბეჭდავს სრულ სახელს ერთ სტრინგად.
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით
// # medium hard
function fullName(firstName, lastName){
    console.log(firstName + lastName)
}
firstName("dato")
lastName("miribiani")
firstName("rezi")
lastName("maxaradze")
firstName("saba")
lastName("bezuashvili")

// 6)შექმენი ფუნქცია isAdult(age).
// თუ ასაკი(პარამეტი) 18 ან მეტია, დაბეჭდოს Adult, სხვა შემთხვევაში Minor.(გამოიყენე ternary)
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით
function  isAdult(age){
    age > 18? console.log("adult"):console.log("minor")
}
age(13)
age(53)
age(55)
age(123)
// 7)შექმენი ფუნქცია checkNumber(num).
// თუ რიცხვი(პარამეტრი) დადებითია — დაბეჭდოს Positive, უარყოფითია — Negative, ხოლო 0-ზე — Zero , გამოიყენე ternary
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით

function  checkNumber(num){
    num>0?console.log("positive"): num< 0? console.log("negative"):console.log("zero")
}

num(12)
num(-12)
num(0)
// 8)შექმენი ფუნქცია rectangleInfo(width, height), რომელიც დაბეჭდავს მართკუთხედის ფართობს: width * height.
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით
// # harder
function rectangleInfo(width, height){
    console.log(width * height)

}

width(12)
height(154)
width(32)
height(44)
width(122)
height(54)

// 9)შექმენი ფუნქცია greetUser(name, time).
// თუ time არის "morning", დაბეჭდოს Good morning, ${name}!
// თუ time არის "evening" — Good evening, ${name}!
// სხვა შემთხვევაში — Hello, name!
// გამოძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით
function  greetUser(name, time){
    time === "morning" ? console.log("Good morning", ${name}): time === "evening"?console.log("Good evening", ${name}):console.log("hello", name)

}

name("dato")
time("morning")
name("rezi")
time("evening")
name("saba")
time("game")

// 10)შექმენი ფუნქცია checkPassword(password).
// თუ პაროლის სიგრძე 8-ზე ნაკლებია, დაბეჭდოს Password is too short, სხვა შემთხვევაში Password accepted.(ternary)
// გამოძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

function checkPassword(password){
    password.length < 8? console.log("Password is too short"):console.log(Password accepted)

}

password("sdgd")
password("sdhdhehdjncdgd")


// 11)შექმენი ფუნქცია checkName(name).
// თუ სახელი იწყება ასო "G"-ზე, დაბეჭდოს Starts with G, სხვა შემთხვევაში Does not start with G. (გამოიყენე startsWith() და (if else)
function checkName(name){
    if(name.startsWith("g")){
        console.log("Starts with G")
    }else{
        console.log("Does not start with G.")
    }
}

// 12)შექმენი ფუნქცია lower(word) რომელიც არგუმენტად გადაცემულ სიტყვას გადაიყვანს მთლიანად აფერქეისში
// გამოძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

function lower(word){
    console.log(word.upperCase())
}
word("sfhfc")
word("fygdghcc")