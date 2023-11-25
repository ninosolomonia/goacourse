#Complete the square sum function so that it squares 
#each number passed into it and then sums the results together.
#For example, for [1, 2, 2] it should return 9 because 
def square_sum(numbers):
    sum = 0
    square = 1
    for element in numbers:
        square = element*element
        sum += square
    return sum



#Write a function that removes the 
#spaces from the string, then return the resultant string.
def no_space(x):
    return x.replace(" ","")





#Nathan loves cycling.Because Nathan knows it is important to stay hydrated, he drinks 0.5 #litresof water per hour of cycling.
#You get given the time in hours and you need to return the number of litres Nathan will #drink,rounded to the smallest value.
def litres(time):
    return (time*0.5)//1




#Make a simple function called greet that returns the most-famous "hello world!".
def greet ():
    razmis_liderebi=4
    razmis_wevrebi=31
    nika=1
    if razmis_liderebi>razmis_wevrebi:
        return("goodbye world")
    elif nika<razmis_wevrebi:
        return("hello world!")       
    else:
        return("hello chad") 