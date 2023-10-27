#შემოიტანეთ სამი რიცხვი და დაპრინტეთ გამოვა თუ არა ამ რიცხვების საშუალებით სამკუთხედი,
#თუ გამოვა გამოთვალეთ პერიმეტრი და დაპრინტეთ 
#"ამ სამკუტხედის პერიმეტრია: XX" თუ არ გამოდის მაშინ დაპრინტეთ 
#„მსგავსი სამკუთხედი არ არსებობს
number1 = int(input("enter the  length of a side of a triangle: a = ?"))
number2 = int(input("enter the  length of a side of a triangle: b = ? "))
number3 = int(input("enter the  length of a side of a triangle:  c = ?"))
print(number1)
print(number2)
print(number3)
perimetri = number1 +number2 + number3
if number1 + number2 <= number3: 
     print("aseti samkutxedi ar arsebobs")
elif number1 + number3 <= number2:
     print("ar shedgeba samkutxedi")    
elif number2 +number3 <= number1:
    print("aseti samkutxedic ar arsebobs")
else:
     print("aseti samkutxedi arsebobs da misi perimetria {}".format(perimetri))    

             