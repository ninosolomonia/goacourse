#ნივთმა დაიკლო ფასში 10% ით,საიდანაც გამყიდველმა აიღო 8% მოგება
#რამდენ % იან მოგებას აიღებდა ის ფასის დაკლებამდე? 
#ჩაწერეთ ეს ყველა მონაცემი პითონში და დაათვლევინეთ მას.
first_price = float(input("enter the price: "))
second_price = first_price -(first_price*10/100)
print("pasdaklebis shemdeg nivti girs: "+ str(second_price) + " lari")
benefit = second_price*8/100
print("mogeba aris: "+ str(benefit)+ " lari")


 
