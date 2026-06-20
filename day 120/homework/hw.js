
// 1)რიცხვის დამრგვალება
// შექმენი ფუნქცია, რომელიც მიიღებს ათწილად რიცხვს და დააბრუნებს:
// Math.round() შედეგს
// Math.floor() შედეგს
// Math.ceil() შედეგს
function numbers(num){
    return Math.round(num), Math.floor(num), Math.celi(num)
}
num(0.12)
num(12.12)
num(1.4)

// 2)უდიდესი და უმცირესი რიცხვის პოვნა
// ფუნქციამ უნდა მიიღოს 5 რიცხვი და დააბრუნოს:

// ყველაზე დიდი
// ყველაზე პატარა
function num (numbers){
    return Math.max(numbers) && Math.min(numbers)
}
numbers(12,212,21212,2121,1)
numbers(121212,1,12122,333,0)

// 3)ფუნქციამ უნდა მიიღოს ორი რიცხვი:
// პირველი რიცხვი
// და
// ხარისხი
// და დააბრუნოს პირველი რიცხვი მეორის ხარისხში აყვანილი.
function ricxvi(value1,value2){
    return Math.pow(value1 , value2)
}
value1(3)
value2(5)
// 4)ფუნქციამ უნდა მიიღოს რიცხვი და დააბრუნოს მისი კვადრატული ფესვი.
function scr(number){
    return Math.sqrt(number)
}
numbers(81)
// 5)დაწერე ფუნქცია, რომელიც დააბრუნებს შემთხვევით მთელ რიცხვს 0-დან 1-მდე.
function root(num){
    return Math.random()
}
num()
// 6)ფუნქციამ უნდა მიიღოს რიცხვი და დააბრუნოს მისი დადებით მნიშვნელობა 
function dadeb(ricxv){
    return Math.abs(ricxv)
}
ricxv(-1)
ricxv(-5344343)
// 7)მომხმარებლის მიერ გადმოცემული რიცხვი დაამრგვალე უახლოეს ათეულამდე.
let num = Number(prompt("enter num"))
console.log(Math.round())

// 7)შექმენი ფუნქცია ultimateMath(a, b, c)

// იპოვე:
    function ultimateMath(a, b, c){
        return Math.max(a,b,c) , Math.min(a,b,c),Math.max(a,b,c).pow(a,b,c) , Math.min(a,b,c).sqrt(a,b,c),Math.max(a,b,c) - Math.min(a,b,c)
        
    }
a(2112)
b(23523)
c(3223)


// ყველაზე დიდი რიცხვი
// ყველაზე პატარა რიცხვი
// ყველაზე დიდი რიცხვის კვადრატი
// ყველაზე პატარა რიცხვის კვადრატული ფესვი
// სხვაობა მათ შორის


// 8)შექმენი ფუნქცია checkSign(num)
// გამოიყენე Math.sign() და დაბეჭდე:
// Positive
// ან
// Negative
// ან
// Zero
function s(number){
    switch(number){
        case number >0:
            return "positive"
                break
        case number = 0:
            return "zero"
            break
        case number <0:
            return "negativve"
            }
}