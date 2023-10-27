#შემოიტანეთ აპლიკანტის: სიმაღლე (>= 1,6 და <=2,3) წონა (>=55 და <= 130) 
#ასაკი (>=18 და <=27), თუ აპლიკანტის მონაცემები აკმაყოფილებს შესაბამის მთხოვნებს,
#მაშინ დაობეჭდოს " გილოცავთ!, თქვენ ჩაირიცხეთ სავალდებულო სამხედრო სამსახურში"
#და თუ არ აკმაყოფილებს მაიშინ დაობეჭდოს "სამწუხაროდ თქვენი მონაცემები არ შესაბამება 
#ჩვენს მოთხოვნებს
height = float(input("enter your height: "))
weight = float(input("enter your weight: "))
age =int(input("enter your age: "))
if height >= 1.6 and height <= 2.3:
    if weight >=55 and weight <=130:
        if age >=18 and age <=27:
            print("gilocavt!,tqven chairicxet savaldebulo samxedro samsaxurshi")
else:
            print("samwuxarod tqveni monacemebi ar sheesabameba chvens motxovnebs")    
