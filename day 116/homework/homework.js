/*
TERNARY

1)prompt()-ით მიიღე ასაკი.
თუ 18 ან მეტია, დაბეჭდე "შეგიძლია ხმის მიცემა", წინააღმდეგ შემთხვევაში "ჯერ ვერა".

2)მომხმარებელს შეაყვანინე რიცხვი.
Ternary-ით განსაზღვრე ლუწია თუ კენტი.

3)მომხმარებელს შეაყვანინე პაროლი.
თუ მისი .length არის 8 ან მეტი, გამოიტანე "ძლიერი პაროლი", სხვა შემთხვევაში "სუსტი პაროლი".

4)მომხმარებელმა შეიძლება შეიყვანოს:

"    admin    "

trim() გამოიყენე და ternary-ით შეამოწმე, არის თუ არა "admin".

5)რიცხვის მიხედვით გამოიტანე:

"დადებითი"
"უარყოფითი"
"ნულია"

გამოიყენე მხოლოდ ternary.

6)ორი სახელი შეაყვანინე.
თუ პირველის .length მეტია, გამოიტანე პირველი, წინააღმდეგ შემთხვევაში მეორე.

7)შეიყვანე ორი რიცხვი prompt()-ით.
თუ პირველი მეტია მეორეზე, დაბეჭდე "პირველი დიდია", სხვა შემთხვევაში "მეორე ტოლია ან დიდია".

8)შექმენი ცვლადი:

let data = "25";

Ternary-ით შეამოწმე:
თუ typeof data === "string" გამოიტანე "სტრინგია", სხვა შემთხვევაში "სტრინგი არაა".

9)მომხმარებლის როლი
let role = prompt("შეიყვანე როლი").trim().toLowerCase();

თუ role არის "admin" → "სრული წვდომა"

თუ "moderator" → "შეზღუდული წვდომა"

დანარჩენ შემთხვევაში → "მომხმარებელი"

(გამოიყენე nested ternary.)

10)მომხმარებელი წერს ქულას (0-100).

გამოიტანე:

90+ → "A"
80+ → "B"
70+ → "C"
60+ → "D"
დანარჩენი → "F"

მხოლოდ ternary-ებით.



SWITCH

10)მომხმარებელი წერს თვის ნომერს (1-12).

switch-ით განსაზღვრე სეზონი:

12, 1, 2 → ზამთარი
3, 4, 5 → გაზაფხული
6, 7, 8 → ზაფხული
9, 10, 11 → შემოდგომა

11)მომხმარებელი წერს ფერს:

"red"
"yellow"
"green"

switch-ით გამოიტანე:

red → "გაჩერდი"
yellow → "მოემზადე"
green → "იარე"

12)შეიყვანე ცხოველის სახელი:

dog
cat
cow
sheep

switch-ით გამოიტანე შესაბამისი ხმა.

13)მომხმარებელი წერს სიმბოლოს:

A
B
C
D
F

switch-ით გამოიტანე შესაბამისი ტექსტი:

A → შესანიშნავი
B → ძალიან კარგი
C → კარგი
D → დამაკმაყოფილებელი
F → ჩაჭრილი

14)შეიყვანე ბრაუზერის სახელი:

chrome
firefox
edge
safari

გამოიტანე მცირე აღწერა თითოეულზე.

15)შეიყვანე:

admin
moderator
user
guest

გამოიტანე მათი უფლებები.
*/


// 1
let age = Number(prompt("etnter age:"))
age >=18 ? console.log("shegilia xma misce") : console.log("jer ver miscem xmas")

// 2 
let num = Number(prompt("enter nmum:"))
num % 2 === 0 ? console.log("luwia") : console.log("kenti")

// 3
let pass = prompt("enter password")
pass.length > 8 ? console.log("dzlieri paroli"):console.log("susti paroli")

// 4
let name = "    admin    "
name.trim() === name ? console.log("real admin"): console.log("error")

// 5 
let num = Number(prompt("enter num"))
num > 0 ? console.log("dadebiti"): num = 0 ?  console.log("nuli"): console.log("uaryofiti")

// 6
let name = "dato"
let name1 = "gio"
name.length > name1.length ? console.log(name):console.log(name1)

// 7
let num = 43
let num1 = 23
num > num1 ? console.log(num):console.log(num1)

// 8
let data = "25"
typeof data === "string"? console.log("stringia"): console.log("araa stringi")

// 9
let role = prompt("შეიყვანე როლი").trim().toLowerCase()
role === "admin"? console.log("sruli wvdoma"): role === "moderato"? console.log("shesguduli wvdoma"): console.log("მომხმარებელი")

// 10
let qula = Number(prompt("enter qula:"))
qula >= 90 ? console.log("A"): qula >=80 ? console.log("B"): qula >= 70? console.log("C"): qula >=60 ? console.log("D"): console.log("F")

// 11 
let num = Number("prompt 1-12 mde")
switch(num){
    case 12,1,2:
        console.log("zamtari")
        break
    case 3,4,5:
        console.log("gazafxuli")
        break
    case 6,7,8:
        console.log("zafxuli")
        break
    case 9,10,11:
        console.log("shemodgoma")
        break
    default :
        console.log("ararsebobs")
        break
    }

// 12
let rgy = prompt("enter color red or green or yellow")
switch (rgy){
    case "red":
        console.log("gacherdi")
        break
    case "yellow":
        console.log("moemzade")
        break
    case "green":
        console.log("dagazee")
        break
    default :
        console.log("ararsebobs")
        break    
    }

// 13
let animal = prompt("dog or cow or cat or sheep")
switch (animal){
    case "dog":
        console.log("vaf")
        break
    case "cow":
        console.log("muuu")
        break    
    case "cat":
        console.log("miauu")
        break
    case "sheep":
        console.log("beee")
        break
    default :
        console.log("ararsebobs")
        break
}

// 14
let aso = prompt("A,B,C,D,F")
switch (aso){
    case "A":
        console.log("dzalian kargi")
        break
    case "B":
        console.log("kargia")
        break
    case "C":
        console.log("sashvualo")
        break
    case 'D':
        console.log("normaluria")
        break
    case "F":
        console.log("cudia")
    }   

// 15
// firefox
// edge
// safari

let brouserr = prompt("enter brousers")
switch (brouserr){
    case "chrome":
        console.log("igeb informacia")
        break
    case "firefox":
        console.log("free open-source webbrowes")
        break
    case "edge":
        console.log("the outside limit or furthest point")
        break
    case "safari":
        console.log("apple websait")
    }

// 16
let role = prompt("enter admin or moderator or user or guest")
switch (role){
    case "admin":
        console.log("yvelafristvis xelmisawvdomi")
        break
    case "moderator":
        console.log("naxevrad xelmisawvdomi")
        break
    case "guest":
        console.log("loginis gareshe shemosuli")
        break
    default:
        console.log("error")
    }