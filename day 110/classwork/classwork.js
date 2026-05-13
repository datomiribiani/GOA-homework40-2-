// 1)მომხმარებელს შემოატანინე რაიმე სახელი და შეინახე ცვლადში
// შემდეგ შეამოწმე if სთეითმენთით თუ მომხმარებლის მიერ შემოყვანილი სახელი იწყება ასო "g" ით კონსოლში გამოიტანე --> "ეს სახელი იწყება გ ასოზე"
let name = prompt("enter name")
if (name.startsWith('g')){
    console.log("ეს სახელი იწყება გ ასოზე")
} 

// 2)შექმენი ცვლადი და შეინახე შიგნით true
// შემდეგ if ში ფრჩხილებში ჩასვი ცვლადის სახელი,შემდეგ დააკონსოლლოგე ---> ეს პირობა არის true
let boll = true
if (boll){
    console.log("ეს პირობა არის true")
}

// 3)მომხმარებელს შემოარანინე რაიმე სახელი

// შემდეგ შეამოწმე თუ მომხმარებლის მიერ შემოტანილის ახელი იწყება "i" ასოზე დააკონსოლლოგე --> starts with letter i
// სხვა შემთხვევაში დააკონსოლლოგე --> "this name does not start with letter i" 

let name = prompt("entername")
if(name.startsWith("i")){
    console.log("starts with letter i")
}else{
    console.log("this name does not start with letter i" )
}