# შექმენით 10 მათემატიკური შეკითხვა მომხმარებლისთვის
#შემდეგ გააკეთეთ ისე რომ ყოველი მცდარი ან  სწორი პასუხის შემდეგ პასუხის ქვემოთ ეწერებოდეს
#სწორია ან არასწორია ხოლო ტესტის დასრულების შემდეგ თუ 10 ივე  კითხვის პასუხი 
#იქნება ჭეშმარიტი დაიპრინტოს: "შენ აშკარად GOA ში სწავლობდი ჩემო ძმაო".  
#ხოლო თუ ამ 10 პასუხიდან 1 მაინც იქნება მცდარი დაიპრინტოს ...
#"კიდევს სცადეთ ან შემოგვიერთდი GOA ში, GOA ელს ეს არეკადრება" 
correct_answers = 0 
question1 = 20 + 5
answer1 = int(input("enter your answer: "))
if answer1 == 25:
    print("sworia")
    correct_answers += 1
else:
    print("arasworia ")    
question2 = 18 + 6
answer2 = int(input("enter your answer: "))
if answer2 == 24:
    print("sworia")
    correct_answers += 1
else:
    print("arasworia ")    
question3 = 25*12
answer3 = int(input("enter your answer: "))
if answer3 == 300:
    print("sworia")
    correct_answers += 1
else:
    print("arasworia ")
question4 = 12/2
answer4 = int(input("enter your answer: "))
if answer4 == 6:
    print("sworia")
    correct_answers += 1
else:
    print("arasworia ")    
question5 = 100*100
answer5 = int(input("enter your answer: "))
if answer5 == 10000:
    print("sworia")
    correct_answers += 1
else:
    print("arasworia ")
print("number of your correct answers is: "+ str(correct_answers)) 
if correct_answers == 5:
    print("shen ashkarad goashi swavlobdi ")
else:
    print("კიდევს სცადეთ ან შემოგვიერთდი GOA ში, GOA ელს ეს არეკადრება") 
#answer = input("enter your answer: ")
#for num in range(5):
    #if answer == 25:
        #print("sworia")
      


