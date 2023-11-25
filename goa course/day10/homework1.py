#შექმენით random password generator პროგრამა რომელშიც დაგენერირდბა პაროლი,
#8 სიმბოლოიანი, სადაც აუცილებლად 2 სიმბოლო იქნება !##%(#)^#, 
#2 სიმბოლო იქნება აბგქწეკჯასკჯქწე , 4 სიმბოლო იქნება ციფრები 215346347347
import random
symbols = ["!","§","%","&","/","#"]
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
         'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0","1","2","3","4","5","6","7","8","9"]
my_password = []
for i in range(2):
    my_password.append(random.choice(symbols))
for i in range(2):
    my_password.append(random.choice(chars))  
for i in range(4):
    my_password.append(random.choice(numbers)) 
#random.shuffle(my_password) 
#print(my_password)
final_password = ""
for i in range(len(my_password)):
    current_char = random.choice(my_password)
    final_password += current_char
    my_password.remove(current_char)
print(final_password)    
