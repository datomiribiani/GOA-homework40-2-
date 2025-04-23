# 4)მომხმარებელს შემოატანინე მისი საყვარელი ფერი,თუ საყვარელი ფერი ემთხვევა წითელს ტერმინალში გამოუტანე red is favorite color,თუ შემოტანილი ფერი ემთხვევა ყვითელს დაუპტინტე favorite color is yellow,თუ შემოტანილი ფერი ემთხვევა ლურჯს დაუპრინტე favorite color is blue,ყველა სხვა დანარჩენ შემთხვევაში დაუპტინტე other color
color = input("enter your color")
if color == "red":
    print("red")
if color == "yellow":   
    print("yellow")
if color == "blue" :
    print("blue")
else:
    print("other color")