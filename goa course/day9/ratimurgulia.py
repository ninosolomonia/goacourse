#რატი მურღულია — მომხმარებელს შემოატანინეთ ორი სახელი და გვარი
#და შეადარეთ ერთი მეორეს,დაითვალეთ a-ს რაოდენობა 
#რომელ სახელში არის მეტი,და დაპრინტეთ მიღებული შედეგი
ammount_of_a1 = 0
ammount_of_a2 = 0
name1 = input("enter your name and surname: ")
name2 = input("enter your name and surname: ")
for char in name1:
    if char in "a":
        ammount_of_a1 += 1
for char in name2:
    if char in "a":
        ammount_of_a2 += 1
if ammount_of_a1 > ammount_of_a2:
    print("pirvel saxelshi gvaqvs upro meti a da misi raodenoba sheadgens {}".format(ammount_of_a1))
else:
    print("meore saxelshi gvaqvs upro meti a da misi raodenoba sheadgens {}".format(ammount_of_a2))    
        


        
