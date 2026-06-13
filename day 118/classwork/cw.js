/*
შექმენით ფუნქცია სადაც შეინახავთ ორ პარამეტრს --> sityva , sityvisDasawyisi , მიანიჭე ამ ორივე პარამეტრს default მნიშნველობები მაგ: avtosadguri  და avt 

შემდეგ შეამოწმე ფუნქციაში , თუ sityva ისყება sityvisDasawyisi ზე მაშინ დააბრუნოს ფუნქციამ --> "iwyeba" სხვა შემთხვევაში დააბრუნე "ar iwyeba" 

გამოიძახე ფუნქცია ორჯერ,ერთხელ არგუმენტებით მეორედ არგუმენტების გარეშე(თან დააკონსოლლოგე გამოძახხებული ფუნქციები რომ ნახოთ შედეგი)და ნახეთ შედეგი

ქვემოთ კომენტარის სახით ახსენით თუ რატომ დაბეჭდა პირველმაფუნქციამ ეს შედეგი და რატომ დაბეჭდა მეორე ფუნქციამ ეს შედეგი
*/

function name(sityva = 'avtosadgomi',sityvisDasawyisi = 'avt'){
    if(sityva.startsWith(sityvisDasawyisi)){
        return "iwyeba"
    }else{
        return "ar iwyeba"
    }
}
console.log(name("avtosadguri","avt")) 
console.log(name())

// imitom radgan weshmaritia da meores imitom ar dabechdavs rom arari false si