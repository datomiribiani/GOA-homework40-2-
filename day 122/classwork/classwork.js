// შექმენით ფუნქცია function expression ით რომელსაც გადაეცემა პარამეტრად num რიცხვი

// შენი დავალებაა რომ გაიგო ეს რიცხვი ლუწია თუ კენტია და დააბრუნო შესაბამისი სტრინგი --> "even" თუ ლუწია "odd" თუ კენტია

// გააკეთე ternary ოპერატორით

// გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტით

// const greet = function(num){
//     num %2=== 0? "even":"odd"
// }

// greet(12)
// greet(13222)
// greet(12121212)




// შექმენით ARROW FUNCTION რომელსაც არგუმენტად გადაეცემა 4 რიცხვი

// შენი დავალებაა დააბრუნო ამ 4 რიცხვიდან მაქსიმალური რიცხვი

// გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

// const greet = (num,num1,num2,num3) =>{
//     return Math.max(num,num1,num2,num3)
// }

// greet(12,12,212,1)
// greet(1,12,121212,121)
// greet(2231212,33,323,3)
// greet(1,33,22,2)



function greet(name , age , sunrame){
  return  `Hello my name is ${name} , my surname is ${surname} and age is ${age}`
}

console.log(greet("giorgi" , 20 , "miribiani"))


// გადააკეთეთ ზემოთ მოცემული ფუნქცია ჯერ function expression შემდეგ arrow ფუნქციად

const greet =  function(name , age , sunrame){
  return  `Hello my name is ${name} , my surname is ${surname} and age is ${age}`
}

console.log(greet("giorgi" , 20 , "miribiani"))



const  greet =(name , age , sunrame) =>{
  return  `Hello my name is ${name} , my surname is ${surname} and age is ${age}`
}

console.log(greet("giorgi" , 20 , "miribiani"))