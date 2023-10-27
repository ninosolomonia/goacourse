#User-ს შემოატანინეთ თავისი სიმაღლე. მიეცით საშუალება მომხმარებელს აირჩიოს ის, 
#თუ რომელ სიდიდეში სურს გაიგოს თავისი სიმაღლე, სანტიმეტრებში თუ ფუტებში...
#(თუ შემოიტანს 180-ს და აირჩევს ფუტებში გადაყვანას თავისი წონის, 
#დაუპრინტეთ რამდენი ფუტია ის
height = float(input("enter your height: "))
measure_in = input("airchie romel erteulshi ginda gachvenos:santimetri tu puti -")
measure_in_feet = height/30.48

if measure_in == "santimetri":
    print("shen xar " + str(height) +" " +str(measure_in))
else:
    print("shen xar " + str(measure_in_feet) +" " +str(measure_in))  


