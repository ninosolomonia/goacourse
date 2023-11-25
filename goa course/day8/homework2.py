#ბილეთი ღირს 25 ლარი,
#მაგრამ ბავშვებისთვის უფასოა,
#გვყავს 13 ადამიანი, აქედან 10 დიდი და 3 ბავშვი, 
#გამოთვალეთ ჯამში რამდენი ლარი დასჭირდებათ 
ammount_of_kids = 0
ammount_of_adults = 0
total_cost = 0
for i in range(5):
    age=int(input("enter your age: "))
    if age>18:
        print("25 lari")
        ammount_of_adults+=1
        total_cost+=25
        print("jamshi gadasaxdeli iqneba am etapze"+ str(total_cost))
    elif age<=18 and age>0:
        print("0 lari")
        ammount_of_kids+=1
    else:
        print("are you a human?")        
print("sul iqneba " +str(ammount_of_kids)+" bavshvi" + "da " + str(ammount_of_adults)+ "didi")