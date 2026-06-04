/*
1)მომხმარებელს შემოატანინე მნიშვნელობა prompt()-ით.
თუ მნიშვნელობა არის truthy, დაბეჭდე "მნიშვნელობა არსებობს",
ხოლო თუ falsy არის → "მნიშვნელობა ცარიელია".

let name = prompt("enter name")
if(name){
    console.log("მნიშვნელობა არსებობს")
}else{
    console.log("მნიშვნელობა ცარიელია")
    }

2)შექმენი ცვლადი nickname.
თუ მომხმარებელმა არაფერი შეიყვანა, გამოიყენე "Guest" მნიშვნელობა || ოპერატორით.
ბოლოში დაბეჭდე nickname.
let nickname = prompt("შეიყვანე nickname") || "Guest";
console.log(nickname);

3)მომხმარებელს შემოატანინე ტექსტი.
თუ ტექსტი არსებობს და .trim() შემდეგ სიგრძე 5-ზე მეტია → "გრძელი ტექსტია"
სხვა შემთხვევაში → "მოკლე ტექსტია".
let text = prompt("enter text")
if(text === true && text.trim() && text.length > 5){
    console.log("გრძელი ტექსტია")
}else{
    console.log("მოკლე ტექსტია")
    }

4)მომხმარებელს შემოატანინე ასაკი.
თუ ასაკი truthy-ა და 18-ზე მეტია → "სრულწლოვანი"
თუ ასაკი falsy-ა → "ასაკი არ არის შეყვანილი".

let age = Number(prompt("enter age"))
if(age === true && age > 18){
    console.log("სრულწლოვანი")
}else{
    console.log("ასაკი არ არის შეყვანილი")
    }

5)mომხმარებელს შემოატანინე ორი მნიშვნელობა.
თუ ორივე truthy-ა → "ორივე სწორია"
თუ ერთ-ერთი falsy-ა → "რომელიღაც ცარიელია".
let nickname = prompt("შეიყვანე nickname")
let nickname = prompt("შეიყვანე nickname")
if(nickname){
    console.log("ორივე სწორია")
}else{
    console.log("რომელიღაც ცარიელია")
    }

6)let isNum = 0;
let result = isNum || "other nym";
console.log(result)
chven rogorc vicit 0 ani aris falty da || ori xasi trues mxaresaa sul magito miviget eg mnishneloba
დაბეჭდე result და ახსენი რატომ მიიღო ეს მნიშვნელობა.



7)მომხმარებელს შემოატანინე ტექსტი.
თუ:
typeof არის "string"
და ტექსტი არ არის ცარიელი
და length 3-ის ჯერადია
დაბეჭდე "Special string"
სხვა შემთხვევაში → "Normal string"
let name = prompt("enter name")
if(name.typeof === "string" && !== "" && name.length % 3 ===0  ){
    console.log(""Special string"")
}else{
    console.log("Normal string")
    }


8)მომხმარებელს შემოატანინე ორი username.
თუ:
ორივე იწყება "go"-თი
და ერთნაირი არ არის(!==)
და ორივეს length მინიმუმ 6 აქვს

let name = prompt("enter name")
let name1 = prompt("enter name")
if(name.startsWith("go") && name1.startsWith("go") && name !== name1 && name1.length >=6 && name1.length >=6 ){
    console.log("Matching users")
}else{
    console.log("Users failed")
    }

დაბეჭდე "Matching users"
სხვა შემთხვევაში → "Users failed"

9)მომხმარებელს შემოატანინე 2 პაროლი.
თუ:
ორივე პაროლი ერთმანეთს ემთხვევა
და პირველი პაროლის length მეტია 8-ზე
და პაროლი uppercase-ში არ უდრის ორიგინალს
დაბეჭდე "Passwords match"
სხვა შემთხვევაში → "Passwords do not match"
let name = prompt("enter name")
let name1 = prompt("enter name")
if(name === name1 && name.length > 8 && name !== name1 ){
    console.log("Passwords match")
}else{
    console.log("Passwords do not match")
    }


10)მომხმარებელს შემოატანინე ტექსტი.
თუ:
ტექსტი იწყება "java"-თი 
ან length მეტია 20-ზე
დაბეჭდე "Programming text"
თუ length ნაკლებია 5-ზე → "Too short"
let name = prompt("enter name")
if(name.startsWith("java") || ame.lrngth > 20 ){
    console.log(""Programming text"")
}else if(name.length<5){
    console.log("to short")
    }else{
        console.log("Unknown text")
        }

სხვა შემთხვევაში → "Unknown text"
11)მომხმარებელს შემოატანინე username და role.
თუ:
username იწყება "user"-ით
და role lowercase-ში უდრის "admin"
let name = prompt("username")
let role = prompt("username")
if(name.startsWith("user")&& role.lowerCase === "admin" ){
    console.log("fake admin")
}else if(name.startsWith("admin")&& role.lowerCase === "admin"){
    console.log("Real admin")
    }else{
        console.log("normal user")
        }

დაბეჭდე "Fake admin"

თუ:

username იწყება "admin"-ით
და role lowercase-ში უდრის "admin"

დაბეჭდე "Real admin"

სხვა შემთხვევაში → "Normal user"
*/