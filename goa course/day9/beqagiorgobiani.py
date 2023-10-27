#გვაქვს სია list=[21,-3,11,-31,7,-34]
#ამ სიაში დაამატეთ მეხუთე ინდექსად ინფუთით რიცხვი
#და დაპრინტეთ მხოლოდ დადებითი რიცხვების ჯამი
list=[21,-3,11,-31,7,-34]
sum = 0
for num in list:
    if num >= 0:
        sum += num
print(sum)
number =int(input("enter one number: "))
list[5] = number
if number >= 0:
    total_sum = sum + number
    print("mtliani jami sheadgens : {}".format(total_sum))
else:
    print("jami aris 39")    

