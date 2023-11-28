"""1))))))))))))))century from year
Introduction
The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

Task
Given a year, return the century it is in."""
def century(year):
    if year %100 == 0:
        return year // 100 
    return year //100 +1


"""2)))))beginner series #2 clock
Clock shows h hours, m minutes and s seconds after midnight.
Your task is to write a function which returns the time since midnight in milliseconds.
Example:
h = 0
m = 1
s = 1
result = 61000"""
def past(h, m, s):
    return (h*3600 +m*60+s)*1000

"""3))))beginner-lost without a map 
Given an array of integers, return a new array with each value doubled.
For example:
[1, 2, 3] --> [2, 4, 6]"""
def maps(a):
    my_arr = []
    for i in a:
        i = 2 * i
        my_arr.append(i)
    return my_arr

"""4 abbreviate a two word name))))Write a function to convert a name into initials. 
This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
It should look like this:
Sam Harris => S.H
patrick feeney => P.F"""
def abbrev_name(name):
    my_list = name.split()
    list_name = my_list[0]
    list_surname = my_list[1]
    
    return (list_name[0] +"." + list_surname[0]).upper()

"""5))))opposites attract
Timmy & Sarah think they are in love, but around where they live, 
they will only know once they pick a flower each.
If one of the flowers has an even number of petals and the other has an odd number
of petals it means they are in love.
Write a function that will take the number of petals of each flower 
and return true if they are in love and false if they aren't."""
def lovefunc( flower1, flower2 ):
    if (flower1+flower2) % 2 ==0:
        return False
    return True

"""6))))))))beginner-lost without a map
Given an array of integers, return a new array with each value doubled.
For example:
[1, 2, 3] --> [2, 4, 6]"""
def maps(a):
    my_arr = []
    for element in a:
        element = 2 * element
        my_arr.append(element)
    return my_arr    



"""7))convert number to reversed array of digits
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of 
this number within an array in reverse order.
Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0]"""
def digitize(n):
    my_arr = []
    for element in str(n):
        my_arr.append(int(element))  #my_arr.insert(0,int(element))
    return my_arr[::-1]


"""8)))) beginner series schoool paperwork
Your classmates asked you to copy some paperwork for them.
 You know that there are 'n' classmates and the paperwork has 'm' pages.
Your task is to calculate how many blank pages do you need.
 If n < 0 or m < 0 return 0.
Example:
n= 5, m=5: 25
n=-5, m=5:  0"""
def paperwork(n, m):
    if n > 0 and m > 0:
        return m * n
    return 0


"""9)))) simple multiplication This kata is about multiplying a given number by eight
 if it is an even number and by nine otherwise."""
def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    return number * 9


"""10)))) a needle in the haystack
Can you find the needle in the haystack?
Write a function findNeedle() that takes an array full of junk
but containing one "needle"
After your function finds the needle it should return a message (as a string) 
that says:"found the needle at position " plus the index it found the needle, so:"""
def find_needle(haystack):
    index_needle = haystack.index("needle")
    for element in haystack:
        if element == "needle":
            return "found the needle at position" + str(index_needle)
        

"""11))))))))makeuppercase
 Write a function which converts the input string to uppercase."""  
def make_upper_case(s):
    return s.upper()


"""12)) are you playing banjo?
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!
The function takes a name as its only argument, and returns one of the following strings:
name + " plays banjo" 
name + " does not play banjo"""
def are_you_playing_banjo(name):
    if name[0] =="R" or name[0] == "r":
        return name +  " plays banjo"
    return name + " does not play banjo"


"""13)))) invert values
Given a set of numbers, return the additive inverse of each. 
Each positive becomes negatives, and the negatives become positives.
invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
You can assume that all values are integers. Do not mutate the input array/list."""
def invert(lst):
    new_arr=[]
    for element in lst:
        element = element * -1
        new_arr.append(element)
        
    return new_arr


"""14)))))) calculate average 
Write a function which calculates the average of the numbers in a given list.
Note: Empty arrays should return 0."""
def find_average(numbers):
    if len(numbers) == 0:
        return 0
    my_sum = 0
    for element in numbers:
        my_sum += element 
    return my_sum/len(numbers)

"""15))))is he gonna survive?
A hero is on his way to the castle to complete his mission.
 However, he's been told that the castle is surrounded with a couple of powerful 
 dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how 
 many bullets he should carry.. Assuming he's gonna grab a specific given number 
 of bullets and move forward to fight another specific given number of dragons, 
 will he survive?
Return true if yes, false otherwise :)"""
def hero(bullets, dragons):
    if bullets/2 >= dragons:
        return True
    return False

"""16)))) count of positives /sum of negatives
Given an array of integers.
Return an array, where the first element is the 
count of positives numbers and the second element is sum of negative numbers. 
0 is neither positive nor negative.
If the input is an empty array or is null, return an empty array.
Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15],
you should return [10, -65]."""
def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return arr
    positive_numbers = 0
    sum_of_negative = 0
    for element in arr:
        if element > 0:
            positive_numbers += 1
        elif element <= 0:
            sum_of_negative += element
        else:
            return [0,0]
    my_arr = [positive_numbers,sum_of_negative]    
    return my_arr


"""17))))) beginner-reduce but grow
Given a non-empty array of integers, return the result of multiplying 
the values together in order. Example:
[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24"""
def grow(arr):
    result = 1
    i = 0
    for element in arr:
        result *= element
        i += 1
    return result



"""18))))))how good are you really?
There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average
 student in your class.
You receive an array with your peers' test scores. Now calculate the average and 
compare your score!
Return True if you're better, else False!
Note:
Your points are not included in the array of your class's points. 
For calculating the average point you may add your point to the given array!"""
def better_than_average(class_points, your_points):
    total_points = 0
    for element in class_points:
        total_points += element
        average_points = (total_points + your_points)/(len(class_points) + 1)
    if your_points > average_points:
        return True
    return False



""""19)))))))) calculate bmi
Write function bmi that calculates body mass index (bmi = weight / height2).
if bmi <= 18.5 return "Underweight"
if bmi <= 25.0 return "Normal"
if bmi <= 30.0 return "Overweight"
if bmi > 30 return "Obese"""
def bmi(weight, height):
    bmi = weight/height**2
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"



"""20)))))))))find maximum or minimum values in the list
Your task is to make two functions ( max and min, or maximum and minimum, 
etc., depending on the language ) that receive a list of integers as input, 
and return the largest and lowest number in that list,
 respectively."""
def minimum(arr):
    min_number = arr[0]
    for element in arr:
        if element < min_number:
            min_number = element
    return min_number
def maximum(arr):
    max_number = arr[0]
    for element in arr:
        if element > max_number:
            max_number = element
    return max_number


"""21)))))))))sentence smash
Write a function that takes an array of words and smashes them together
into a sentence and returns the sentence. You can ignore any need to sanitize
words or add punctuation, but you should add spaces between each word. 
Be careful, there shouldn't be a space at the beginning
or the end of the sentence!
['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'"""
def smash(words):
    new_str = ""
    for element in words:
        new_str += element + " "
    return new_str.strip()


"""22)))))you only need one-beginner
You will be given an array a and a value x. All you need to do is check 
whether the provided array contains the value.
Array can contain numbers or strings. X can be either.
Return true if the array contains the value, false if not."""
def check(seq, elem):
    for element in seq:
        if element == elem:
            return True
    return False   


"""23))))will you make it
You were camping with your friends far away from home, but when it's time to go back,
 you realize that your fuel is running out and the nearest pump is 50 miles away! 
 You know that on average, your car runs on about 25 miles per gallon.
 There are 2 gallons left.Considering these factors, write a function that tells
 you if it is possible to get to the pump or not.
Function should return true if it is possible and false if not. """
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left


"""24)))dna to rna conversion
Deoxyribonucleic acid, DNA is the primary information storage molecule in biological 
systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), 
Adenine ('A'), and Thymine ('T').Ribonucleic acid, RNA, is the primary messenger
 molecule in cells. RNA differs slightly from DNA its chemical structure and contains
no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

Create a function which translates a given DNA string into RNA."""
def dna_to_rna(dna):
    return dna.replace("T","U")

"""25))))))convert a string to an array
Write a function to split a string and convert it into an array of words.
Examples (Input ==> Output):
"Robin Singh" ==> ["Robin", "Singh"]"""
def string_to_array(s):
    if len(s) == 0:
        return [""]
    return s.split()

















