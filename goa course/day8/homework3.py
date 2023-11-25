
#მომხმარებელს შემოატანინეთ სახელი,
#და დაპრინტეთ ეს სახელი იმდენჯერ, რამდენი ასოც არის სახელში.
name=input("enter your name : ")
len_name=len(name)
for i in range(len_name):
    print(str(i)+" "+ name)