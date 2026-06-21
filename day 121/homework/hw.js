// 1)შექმენი ფუნქცია analyzeTemperature(temp) რომელიც:
// თუ ტემპერატურა 30-ზე მეტია, დააბრუნებს "Hot".
// თუ 15-30 შუალედშია, დააბრუნებს "Normal".
// თუ 15-ზე ნაკლებია, დააბრუნებს "Cold".
// ternary
function analyzeTemperature(temp){
   return temp > 30? "hot": temp  > 15 && temp<30? 'normal':"cold" 
}

// 2)შექმენი ფუნქცია:

// calculateSalary(hoursWorked, hourlyRate = 20)
// რომელიც დააბრუნებს მთლიან ხელფასს.
// მაგალითად:
// calculateSalary(8) // 160
// calculateSalary(10, 30) // 300
function calculateSalary(hoursWorked, hourlyRate = 20){
    return hoursWorked * hourlyRate 
}
calculateSalary(8)
calculateSalary(10,30)
// 3)შექმენი ფუნქცია numberType(num) რომელიც დააბრუნებს:
// "Positive"
// "Negative"
// "Zero"
// .sign()
function numberType(num){
    return Math.sign(num)?"positive": Math.sign(num) ?"negative":"zero"
}

// 4)ბილეთის ფასი
// შექმენი ფუნქცია:
// ticketPrice(age, isStudent = false)
// წესები:

// 12 წლამდე → 5 ლარი.
// 12-დან 60 წლამდე → 15 ლარი.
// 60+ → 8 ლარი.
function ticketPrice(age, isStudent = false){
    switch(ticketPrice){
        case age <= 12:
            return "5L"
            break
        case age >12 && age <60: 
            return "15L"
            break
        case age > 60:
            return "8L"
            break
        default:
            return "error"
            break
        }   

}

// 5)შექმენი ფუნქცია:
// grade(score)
// რომელიც აბრუნებს:
// 90-100 → "A"
// 80-89 → "B"
// 70-79 → "C"
// 60-69 → "D"
// 0-59 → "F"
function grade(score){
    switch(grade){
        case score > 90:
            return "A"
                break
        case score  >80 && score < 89: 
            return "B"
            break
        case score > 70 && score<79:
            return "c"
                break
        case score  >60 && score < 69: 
            return "D"
            break
        case score > 0 && score <59:
            return "F"
                break
      
}
}



// switch()