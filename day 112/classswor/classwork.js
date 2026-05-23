function thermometer(checkThermostat,temperature ) {
    if(checkThermostat === "winter" &&  temperature < 18 ){
        return "Turn on heating"
    }else { 
        return "Heating off"    
    }
    if (checkThermostat === "summer" && temperature >25){
        return "Turn on cooling"
    }else
        return "Cooling off"
        else{
            return "Invalid season"
        }
    }



//     თუ ქულა 90 ან მეტია, დააბრუნე: "A"

// თუ ქულა 80-დან 89-მდეა, დააბრუნე: "B"

// თუ ქულა 70-დან 79-მდეა, დააბრუნე: "C"

// თუ ქულა 51-დან 69-მდეა, დააბრუნე: "D"

// თუ ქულა 51-ზე ნაკლებია, დააბრუნე: "F"
if(gradeCalculator > 90){
    return 'A'
}
else if(gradeCalculator >= 80 && gradeCalculator <= 89  ){
    return "B"
}

else if(gradeCalculator >= 70 && gradeCalculator <= 79 ){
    return 'c'
}
else if(gradeCalculator >= 60 && gradeCalculator <= 69 ){
    return "d"
}
else{
    return "f"
}

// პაროლის ვალიდატორი (validatePassword)
// აღწერა: ფუნქციამ უნდა შეამოწმოს პაროლის უსაფრთხოება მისი სიგრძის (length) და შეიცავს თუ არა სპეც-სიმბოლოს (hasSpecialChar - true ან false) მიხედვით.

// თუ სიგრძე 8 სიმბოლოზე ნაკლებია, დააბრუნე: "Too short"

// თუ სიგრძე 8 ან მეტია:

// თუ აქვს სპეც-სიმბოლო (true), დააბრუნე: "Strong password"

// თუ არ აქვს სპეც-სიმბოლო (false), დააბრუნე: "Medium password"


a = true
if(validatePassword.length <8 ){
    return "Too short"
}
else if(a.length  >8) {
    return "Strong password"
}
else{
    return  "Medium password"
}
