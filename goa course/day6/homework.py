#მომხმარებლის ნიშნებისგან გამოანგარიშება საშუალო არითმეტიკული და თუ ცხრაზე მეტი იქნება:
#დაუპრინტეთ გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები
#თუ ეს იქნება 5ზე ნაკლები: დაუპრინტე გილოცავ გაექეცი მატრიცას
#თუ იქნება 5 იდან 9 მდე: დაუპრინტე YOU ARE MID
#თუ იქნება 10ზე მეტი ან 0ზე ნაკლები: დაუპრინტე there is something wrong with you

mark1=int(input("enter your mark in mathematics: "))
mark2=int(input("enter your mark in biology: "))
mark3=int(input("enter your mark in physics: "))
mark4=int(input("enter your mark in chemistry: "))
mark5=int(input("enter your mark in english: "))
mark6=int(input("enter your mark in history: "))
mark7=int(input("enter your mark in geography: "))
average_mark= (mark1+mark2+mark3+mark4+mark5+mark6+mark7)/7
print(average_mark)
if 9<average_mark<10:
    print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები")
elif average_mark <5:
    print(" გილოცავ გაექეცი მატრიცას")    
elif  5<average_mark<9:
    print("you are mid") 
elif average_mark>10 or average_mark<0 :
    print("there is something wrong with you")     
