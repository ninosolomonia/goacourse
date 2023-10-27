#შექმენით ლისტი სადაც სტრინგის სახით ჩაწერთ სამ ელემენტს 
#(სამივე განსხვავებული ზომის ), გამოთვალეთ ელემენტების სიმბოლოების რაოდენობა და
#რომელიც საშუალო იქნება ის დაპრინტეთ 
#my_list = ["matarebeli","tvitmprinavi","dedamiwa"]
#print(len(my_list[0]))
#print(len(my_list[1]))
#print(len(my_list[2]))
#print("am siashi sashualo simboloebis raodenoba aqvs sityvas "+ my_list[0] +
      #" da simobloebis raodenoba sheadgens: {}".format(len(my_list[0])))


sport = ["rugby" , "football" , "basketball"]

rugby = len(sport[0])
football = len(sport[1])
basketball = len(sport[2])

if rugby > football and rugby <basketball : 
    print(sport[0])

elif football > rugby and  football < basketball : 
    print(sport[1])

else : 
    print(sport[2])