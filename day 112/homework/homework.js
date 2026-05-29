/*1)მომხმარებელს prompt()-ით შემოატანინე სახელი.
თუ შეყვანილი ტექსტი ცარიელია trim()-ის შემდეგ → გამოიტანე "შეიყვანე სახელი"
სხვა შემთხვევაში:
თუ სახელი იწყება "A" ასოზე (startsWith()) → "შენი სახელი A-ზე იწყება"
სხვა შემთხვევაში → "სხვა ასოზე იწყება"

let name = prompt("enter name")
if(name === name.trim()){
    console.log("შეიყვანე სახელი")
}else if(name.StartsWith("A")){
    console.log("შენი სახელი A-ზე იწყება")
}esle{
    console.log("სხვა ასოზე იწყება")
}

2)მომხმარებელს შემოატანინე ასაკი prompt()-ით.(რიცხვი)
ასაკი მეტია 18-ზე → "სრულწლოვანი ხარ"
წინააღმდეგ შემთხვევაში → "არ ხარ სრულწლოვანი"
let age = Number(prompt("enter age:"))
if(age > 18){
    console.log("სრულწლოვანი ხარ")
}else{
    console.log("არ ხარ სრულწლოვანი")
    }

3)მომხმარებელს შემოატანინე სიტყვა.
გამოიყენე შემოტანილ მნშვენლობნაზე:
trim()
toUpperCase() 
თუ მიღებული ტექსტი უდრის "ADMIN" → "ადმინის რეჟიმი"
სხვა შემთხვევაში → "ჩვეულებრივი მომხმარებელი"
let word = prompt("enter word:")
if(word.trim().toUpperCase() === "ADMIN" ){
    console.log("ადმინის რეჟიმი")
}esle{
    console.log("ჩვეულებრივი მომხმარებელი")
}

4)მომხმარებელს შემოატანინე ასაკი.
Number()-ით გადააქციე რიცხვად.
let age = Number(prompt("enter age:"))
if(age > 18){
    console.log("სრულწლოვანი")
}else if(age < 18){
    console.log("არასრულწლოვანი")
}else if(age == 18){
    console.log("ზუსტად 18 წლის ხარ")
    }
თუ:

ასაკი > 18 → "სრულწლოვანი"
ასაკი < 18 → "არასრულწლოვანი"
ასაკი == 18 → "ზუსტად 18 წლის ხარ"

5)მომხმარებელს შემოატანინე ტექსტი.
let text= prompt("enter text")
if(text.length > 10){
    console.log("გრძელი ტექსტი")
}else if(text.length < 5){
    console.log("მოკლე ტექსტი")
}esle{
    console.log("საშუალო ტექსტი")
}

თუ:
ტექსტის სიგრძე > 10 → "გრძელი ტექსტი"
ტექსტის სიგრძე < 5 → "მოკლე ტექსტი"
სხვა შემთხვევაში → "საშუალო ტექსტი"

6)მომხმარებელს შემოატანინე ქვეყანა.
გამოიყენე toLowerCase().
let countr = prompt("enter qbeyana:")
if(countr.toLowerCase() === "georgia"){
    console.log("saqartvelo")
}else if(countr.toLowerCase() ===  "france"){
    console.log("safrangeti")
}else{
    console.log("sxva qveyana")
    }
თუ ქვეყანა არის:

"georgia" → "საქართველო"
"france" → "საფრანგეთი"
სხვა შემთხვევაში → "სხვა ქვეყანა"

7)მომხმარებელს შემოატანინე სიტყვა.
let name = prompt("enter name")
if(name === "hello" ){
    console.log("misalmeba")
}else{
    console.log("sxva texti")
    }
თუ ტექსტი იწყება "hello"-ზე → "მისალმება"
სხვა შემთხვევაში → "სხვა ტექსტი"

8)მომხმარებელს შემოატანინე ორი რიცხვი.
ორივე გადააქციე Number()-ით.
let age1 = Number(prompt("entr age"))
let age2 = Number(prompt("entr age"))
if(age1 > age2){
    console.log("პირველი მეტია")
}esle if(age2 > age1){
    console.log(მეორე მეტია")
}else{
    console.log("ტოლია")
    }
თუ:

პირველი > მეორე → "პირველი მეტია"
მეორე > პირველი → "მეორე მეტია"
ტოლია → "ტოლია"

9)მომხმარებელს შემოატანინე ტექსტი.
გამოიყენე typeof.
let name = prompt("text:")
if(name.typeof === "string"){
    console.log("string")
}else{
    console.log("not str")
    }
თუ ტიპი არის "string" → "ეს სტრინგია"
სხვა შემთხვევაში → "ეს სტრინგი არ არის"

10)მომხმარებელს შემოატანინე რიცხვი.
let nm = Number(prompt("num:"))
if(nm > 0){
    console.log("dadebiti")
}els if(nm <0){
    console.log(uaryofiti)
}else{
    console.log("nli")
    }
თუ:

რიცხვი > 0 → "დადებითი"
რიცხვი < 0 → "უარყოფითი"
რიცხვი == 0 → "ნულია"

11)მომხმარებელს შემოატანინე ტექსტი.
let txt = prompt("entett txt:")
if(txt === txt.tolowercase()){
    console.log("pataraa")
}else if(txt.touppercase()){
    console.log(didi asoebi)
}else{
    console.log("shereuli")
    }
თუ ტექსტი მთლიანად პატარა ასოებითაა → "lowercase ტექსტი"
თუ მთლიანად დიდი ასოებითაა → "uppercase ტექსტი"
სხვა შემთხვევაში → "შერეული ტექსტი"

12)მომხმარებელს შემოატანინე სიტყვა.
გამოიყენე String().
let name = prompt("enter nae")
if(name.length  ==0){
    console.log("carieli txt")
}else{
    console.log("TEXTI SHEYVANILIA")
    }
თუ სიტყვის სიგრძე == 0 → "ცარიელი ტექსტი"
სხვა შემთხვევაში → "ტექსტი შეყვანილია"
*/
