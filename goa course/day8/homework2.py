#ბილეთი ღირს 25 ლარი,
#მაგრამ ბავშვებისთვის უფასოა,
#გვყავს 13 ადამიანი, აქედან 10 დიდი და 3 ბავშვი, 
#გამოთვალეთ ჯამში რამდენი ლარი დასჭირდებათ 
age=int(input("enter your age: "))
if age>18:
    print("25 lari")
elif age<=18: 
    print("0 lari")
else:
    print("are you a human?")        
print("the price of 10 tickets for adults and 3 tickets for children  is "+str(10*25)+str(3*0))