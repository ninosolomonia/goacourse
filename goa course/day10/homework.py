#დაწერეთ პროგრამა, რომელშიც შექმნით ჩვენი ჯგუფელებისგან სიას.
#რენდომად გამოიძახებთ ერთ ჯგუფელს, თუ კითხვაზე უპასუხებს მოემატება 
#10 ქულა  tu arasworad-daakldes 5 qulaდა გადავალთ შემდეგზე(ოღონდ ეს ვეღარ 
#უპასუხებს იმ დღეს ნუ remove დაგჭირდებათ
import random
arr_of_students = ["giorgi","rati","salome","anri","demetre"]
arr_of_grades = [0,0,0,0]
for i in range(5):
    random_student= random.choice(arr_of_students)
    print(random_student)
    answer = input("did the student answer correctly?: ")
    index_of_random_student = arr_of_students.index(random_student) 
    if answer == "yes":
        random_student_grade =arr_of_grades[index_of_random_student]
        random_student_grade += 10
        print(random_student ," has plus 10 points and the next student is: ")
        arr_of_students.remove(random_student)
    elif answer == "no":
        random_student_grade = arr_of_grades[index_of_random_student]
        random_student_grade -= 5
        print("the student has minus 5 points and the next student is: ")
        arr_of_students.remove(random_student)
    else:
        print("yes or no")
print("quiz is over and the students have overall points",arr_of_grades) 
####ar gamodis im codnit rac vicit 


