
#GOA ში ყოველ შემოყვანილ ადამიანზე გეძლევა 100ლ.
#მომხმარებელს შემოატანინეთ თუ რამდენი ადამიანი შემოიყვანა 
#ხოლო თითო შემოყვანილ ადამიანზე დაერიცხოს 100ლ

#1) რამდენი დაგერიცხება თუ შემოიყვან 10 ბავშვს?  15 ბავშცს?

#2) რამდენი დაგერიცხება თუ შემოიყვან 100 ბავშვს გამოკლებული 37 დამატებული 13 გაყოფილი 10 და გამრავებული 264 ზე


bonus=100
new_goamember=int(input("ramdeni axali matriceli shemoiyvane? :"))
total_bonus=new_goamember*100
print(total_bonus)
if new_goamember==10:
    print("tqven dagericxebat :"+ str(bonus*new_goamember)+"lari")
elif new_goamember==15:
    print("tqven dagericxebat :"+ str(bonus*new_goamember)+"lari")
else:
    print("ar shecherdet!")    
total_bonus100=100*(100-37+13)/10*264 
print(total_bonus100)