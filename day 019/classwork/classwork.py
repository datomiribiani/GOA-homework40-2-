# 1) შექმენით ფუნქცია რომელსაც გადაეცემა მომხმარებლის შემოტანილი რიცხვი. დააბრუნეთ ამ რიცხვის ჩათვლით ყველა ლუწი რიცხვის საშუალო არითმეტიკული
def lut_rcevebis_sashualo(n):
    jami = 0             
    raodenoba = 0        
    i = 0
    while i <= n:
        if i % 2 == 0:   
            jami = jami + i
            raodenoba = raodenoba + 1
        i = i + 1    
    sashualo = jami / raodenoba
    return sashualo
print(lut_rcevebis_sashualo(1,2,3,4,5,6,7,8,9,10))