#4.Guri Jishkariani 
#შევქმნათ ორი List-ი. ერთში გოგონების სახელები ჩავწეროთ მეორეში ბიჭების.
#დავპრინტოთ დაწყვილებულად   😄
#აი დააკომენტარეთ და დაგაწყვილებთო რო იცოდნენ ფბზე ეგრე დაახლოებით  :დდ
#girls = ["nana ","nunu ","nini "]
#boys = ["gaga","zuzu","gigi"]
#res = [i + j for i, j in zip(girls, boys)]
#print ("The list after element concatenation is : " +  str(res))
#girls = ["nana ","nunu ","nini "]
#boys = ["gaga","zuzu","gigi"]
#i = 0
#for name in boys:
    #print(name + " " + girls[i])
    #i += 1
girl_list = []
boy_list = []
for i in range(4):
    girl_name = input("enter your name: ")
    boy_name = input("enter your name:")
    girl_list.append(girl_name)
    boy_list.append(boy_name)
