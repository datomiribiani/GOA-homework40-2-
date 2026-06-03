/*1)მომხმარებელს შემოატანინე პაროლი prompt()-ით.
თუ:
პაროლი trim() შემდეგ იწყება "GOA"-თი
და მისი სიგრძე (length) მეტია 10-ზე
და მთლიანად uppercase არ არის

let pasww = prompt("enter password")
if(pasww.trim().startWith("GOA") && pasww.length > 10 && pasww != pasww.touppercase()){
    console.log("Strong password")
}else{
    console.log("Weak password")
    }
დაბეჭდე: "Strong password"
სხვა შემთხვევაში: "Weak password"

2)მომხმარებელს შემოატანინე ასაკი და სახელი.
თუ:
ასაკი მეტია 18-ზე
და სახელი იწყება "g"-ზე
let age = Number(prompty("enter age:")
let name = prompty("enter age:"))
if(age > 18 && name.startsWith("g")){
    console.log("axalgazrda")
}else{
    console.log("Wrong username")
    }
თუ ასაკი 18-ზე ნაკლებია → "Too young"
სხვა შემთხვევაში → "Wrong username"

3)მომხმარებელს შემოატანინე ტექსტი.
შეამოწმე:
არის თუ არა ტიპი (typeof) string და
აქვს თუ არა მინიმუმ 5 სიმბოლო
და იწყება თუ არა "hello"-თი 

let txt = prompt("ent")
if(txt.typeof === "string" && txt.length > 5 && txt.startWith("hello")){
    console.log("Valid text")
}else{
    console.log("Invalid text")
    }
თუ ყველა პირობა შესრულდა → "Valid text"

სხვა შემთხვევაში → "Invalid text"


4)მომხმარებელს შემოატანინე ორი სიტყვა.
თუ:
ორივე სიტყვის სიგრძეების ჯამი მეტია 12-ზე
და პირველი სიტყვა uppercase-ში არ უდრის მეორეს uppercase-ში
დაბეჭდე "Different long words"
სხვა შემთხვევაში → "Failed"

let name1 = prompt("name1")
let name2 = prompt("name2")
if(name1.length + name2.length > 12 &&  name1.touppercase() != name2.touppercase()){
    console.log("Different long words")
}else{
    console.log("Failed")
    }

5)მომხმარებელს შემოატანინე ქვეყანა.
თუ:
ტექსტი uppercase-ში უდრის "GEORGIA"
ან lowercase-ში უდრის "sakartvelo"
დაბეჭდე "Correct country"
სხვა შემთხვევაში → "Unknown country"

let cnt = prompt("qveyaba:")
if(cnt.touppercase() ===  "GEORGIA"  || cnt.tolowercase() === "sakartvelo"){
    console.log("Correct country")
}else{
    console.log("Unknown country")
    }


6)
მომხმარებელს შემოატანინე password.
თუ:
length არის 8-დან 15-მდე
და იწყება uppercase ასოთი
let pas = prompt("pass:")
if(pas.length >= 8 && =<15){
    console.log("good password")
}else{
    console.log("Bad password")
    }
დაბეჭდე "Good password"
სხვა შემთხვევაში → "Bad password"

7)მომხმარებელს შემოატანინე ტექსტი.
თუ:
ტექსტის length ლუწია
და lowercase ტექსტი არ იწყება "x"-ზე
და uppercase ტექსტი არ უდრის ორიგინალს

let text = prompt("enter txt")
if(text.length % 2 === 0 && text.tolowercase() && text != text.startWith("x") && text.touppercase() != text){
    console.log("Accepted")
}else{
    console.log("Rejected")
    }
დაბეჭდე "Accepted"
სხვა შემთხვევაში → "Rejected"

8)მომხმარებელს შემოატანინე ორი username.
თუ:
ორივე იწყება "go"-თი
და ერთნაირი არ არის(!==)
და ორივეს length მინიმუმ 6 აქვს
დაბეჭდე "Matching users"
სხვა შემთხვევაში → "Users failed"

let name1 = prompt("user1") 
let name2 = prompt("user2")
if(name1.startWith("go") && name2.startWith("go") && name1 !== name2  && name1.length  <=6  && name2.length  <=6){
    console.log("Matching users")
}else{
    console.log("Users failed")
    }
9)მომხმარებელს შემოატანინე 2 პაროლი.
თუ:
ორივე პაროლი ერთმანეთს ემთხვევა
და პირველი პაროლის length მეტია 8-ზე
და პაროლი uppercase-ში არ უდრის ორიგინალს
let name1 = prompt("user1") 
let name2 = prompt("user2")
if(name1 === name2 && name1.length > 8 && name1 !== name1.touppercase()){
    console.log("Passwords match")
}else{
    console.log("Passwords do not match")
    }
დაბეჭდე "Passwords match"
სხვა შემთხვევაში → "Passwords do not match"

10)მომხმარებელს შემოატანინე ტექსტი.
თუ:
ტექსტი იწყება "java"-თი 
ან length მეტია 20-ზე
დაბეჭდე "Programming text"
თუ length ნაკლებია 5-ზე → "Too short"
სხვა შემთხვევაში → "Unknown text"

let name1 = prompt("user1") 
if(name1.startWith("java") || name1.length > 20){
    console.log("Programming text")
}else if(name1.length< 5){
    console.log("Too short)
}else{
    console.log("Unknown text")
    }


11)მომხმარებელს შემოატანინე username და role.
თუ:
username იწყება "user"-ით
და role lowercase-ში უდრის "admin"
let name  = prompt("user")
let name1  = prompt("role")
if(name.startWith(user) && name1.lowerCase() === "admin"){
    console.log("Fake admin")
}else if(name.startWith("admin") && name1.lowercase() === "admin"){
    console.log("Real admin")
}else{
    console.log("Normal user")
    }

დაბეჭდე "Fake admin"

თუ:

username იწყება "admin"-ით
და role lowercase-ში უდრის "admin"

დაბეჭდე "Real admin"

სხვა შემთხვევაში → "Normal user"

*/