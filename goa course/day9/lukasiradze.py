#input ფუნქციით შემოატანინეთ წინადადება და შმოტანილ წინადედებაში პროგრამას 
#დაათვლევინეთ თანხმოვნები
my_sentence = input("write your sentence: ")
vowels = "aeiouAEIOU"
ammount_of_consonants = 0
for char in my_sentence:
        if char  not in vowels:
            ammount_of_consonants += 1   
print("we have  {} consonants".format(ammount_of_consonants))
