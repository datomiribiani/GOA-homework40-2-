
// 1)შექმენი ფუნქცია greet(name), რომელიც დაბეჭდავს: Hello, name!
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით
function greet(name){
    console.log("hello" + name)
}
greet("dato")
greet("gio")
greet("luka")


// 2)შექმენი ფუნქცია showAge(age), რომელიც დაბეჭდავს: You are age years old.
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით

function showAge(age){
    console.log("you are" + age + "years old"   )
}

showAge(15)
showAgeage(32)
showage(12)
showage(67)

// 3)შექმენი ფუნქცია sum(a, b), რომელიც დაბეჭდავს ორი რიცხვის ჯამს.
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით
function sum(a, b){
    console.log(a + b)
} 
sum(12,14)
sum(12,14)
sum(12,14)
// 4)შექმენი ფუნქცია multiply(a, b), რომელიც დაბეჭდავს ორი რიცხვის ნამრავლს.
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით
function multiply(a, b){
    console.log(a * b)

}

multiply(143432,14344)
multiply(1343433,4434344)


// 5)შექმენი ფუნქცია fullName(firstName, lastName), რომელიც დაბეჭდავს სრულ სახელს ერთ სტრინგად.
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით
// # medium hard
function fullName(firstName, lastName){
    console.log(firstName + lastName)
}
fullName("dato" ,"miribiani")
firstName("rezi","maxaradze")
firstName("saba","bezuashvili")


// 6)შექმენი ფუნქცია isAdult(age).
// თუ ასაკი(პარამეტი) 18 ან მეტია, დაბეჭდოს Adult, სხვა შემთხვევაში Minor.(გამოიყენე ternary)
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით
function  isAdult(age){
    age > 18? console.log("adult"):console.log("minor")
}
isAdult(13)
isAdult(53)
isAdult(55)
isAdult(123)
// 7)შექმენი ფუნქცია checkNumber(num).
// თუ რიცხვი(პარამეტრი) დადებითია — დაბეჭდოს Positive, უარყოფითია — Negative, ხოლო 0-ზე — Zero , გამოიყენე ternary
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით

function  checkNumber(num){
    num>0?console.log("positive"): num< 0? console.log("negative"):console.log("zero")
}

checkName(12)
checkName(-12)
checkName(0)
// 8)შექმენი ფუნქცია rectangleInfo(width, height), რომელიც დაბეჭდავს მართკუთხედის ფართობს: width * height.
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით
// # harder
function rectangleInfo(width, height){
    console.log(width * height)

}

rectangleInfo(12,154)
rectangleInfo(32,44)
rectangleInfo(122,54)


// 9)შექმენი ფუნქცია greetUser(name, time).
// თუ time არის "morning", დაბეჭდოს Good morning, ${name}!
// თუ time არის "evening" — Good evening, ${name}!
// სხვა შემთხვევაში — Hello, name!
// გამოძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით
function  greetUser(name, time){
    time === "morning" ? console.log(`Good morning, ${name}`): time === "evening"?console.log(`Good evening, ${name}`):console.log("hello", name)

}

greetUser("dato","morning")
greetUser("rezi","evening")
greetUser("saba","game")


// 10)შექმენი ფუნქცია checkPassword(password).
// თუ პაროლის სიგრძე 8-ზე ნაკლებია, დაბეჭდოს Password is too short, სხვა შემთხვევაში Password accepted.(ternary)
// გამოძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

function checkPassword(password){
    password.length < 8? console.log("Password is too short"):console.log("Password accepted")

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
checkName("dato")
checkName("gio")
// 12)შექმენი ფუნქცია lower(word) რომელიც არგუმენტად გადაცემულ სიტყვას გადაიყვანს მთლიანად აფერქეისში
// გამოძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

function lower(word){
    console.log(word.toUpperCase())
}
lower("sfhfc")
lower("fygdghcc")