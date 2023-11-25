 ####funqciistvis gvchirdbeba def funqciis saxeli ()frchxilebi da ori wertili :
#def bichebtan_misalmeba():
    #print("hello nika")
    #print("hello gio")
    #print("hello lasha")
    #print("hello luka")
#print("dila")    
#bichebtan_misalmeba()
#print("shaudge")
#bichebtan_misalmeba()
#print("sagamo")
#bichebtan_misalmeba()
#rom turtle import *
#ef draw_a_square():
    #for i in range(4):
        #forward(100)
        #left(90)
#funqciis paramateri iwereba frchilebshi da aris zogadi saxeli input that u define for the function
#def misalmeba(saxeli,age):
    #print("mogesalmebi " + saxeli)
    #print("sheni asakia", age)
#misalmeba("nika",34)    ##argumenti aris konkretuli actual value for the given parameter
#misalmeba("luka",23)
#misalmeba("gabrieli",14)
#misalmeba("sandro",34)

#paramets gadascems shemqmeli funqcias,arguments gadavcemt chven


   ####################sololearn#####################
#numbers = list(range(3,15,2))
#print(numbers[2])
#x = list(range(7, 3, -1)) ###ukugma wasvla 7,6,5,4
#print(x)

squares = [0,1,2,3,4,8,26,57,53,68]
print(squares[::2])  ###dasawyisidan bolomde 2 nabijit
print(squares[2:8:3]) ##3 nabijit
 
sqs = [0,1,2,3,4,8,26,57,53,68]
print(sqs[1::4]) ## wava bolomde 4 nabijit

sqss = [0,1,2,3,4,8,26,57,53,68]
print(sqss[1:-1]) ## tavidan bolos winas chatvlit bolo index aris -1

sqsss = [0,1,2,3,4,8,26,57,53,68]
print(sqss[7:5:-1]) ###57 da 26 meshvidedan mexutemde ukusvlit

nums = [5,42,7,1,0]
res = nums[::-1]
print(res) ####daprintavs yvelapers daiwyebs bolodan .siis shetrialeba

x = [0,1,2,3,4,8,26,57,53,68]
y = x.index(68)  ##printavs im indexs romelzec dgas chven mier mititebuli wevri
print(y) 


squares = [0,1,2,3,4,8,26,57,53,68]
print(min(squares)) # printavs minimalurs siidan
print(max(squares)) # printavs maqsimalurs siidan

z = [0,1,1,2,3,4,8,26,57,53,68]
print(z.count(1)) # daprintavs mocemuli elementi siashi ramdenjer gvxvdeba

z = [0,1,2,3,4,8,26,57,53,68]
z.remove(68)  # washlis siidan am elements
print(z)

z = [0,1,2,3,4,8,26,57,53,68]
z.reverse()  ### abrunebs sias ukugma
print(z)

numbers = [0,1,2,3,4,8,26,57,53,68]
msg = "numbers: {0} {1} {2}".format(numbers[0],numbers[1],numbers[2])
print(msg)
