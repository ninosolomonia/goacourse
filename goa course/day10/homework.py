#დაწერეთ პროგრამა, რომელშიც შექმნით ჩვენი ჯგუფელებისგან სიას.
#რენდომად გამოიძახებთ ერთ ჯგუფელს, თუ კითხვაზე უპასუხებს მოემატება 
#10 ქულა  tu arasworad-daakldes 5 qulaდა გადავალთ შემდეგზე(ოღონდ ეს ვეღარ 
#უპასუხებს იმ დღეს ნუ remove დაგჭირდებათ
import random
students = ["giorgi","rati","salome","anri","demetre"]
point = [5,10]
points = 0
for i in range(5):
    student = random.choice(students)
    print(student)
    answer = input("did the student answer correctly?: ")
    if answer == "yes":
        points += 10
        print(student ," has plus 10 points and the next student is: ")
        students.remove (student)
    elif answer == "no":
        points = points - 5
        print("the student has minus 5 points and the next student is: ")
    else:
        print("yes or no")
print("quiz is over and the students have overall points",points)    


