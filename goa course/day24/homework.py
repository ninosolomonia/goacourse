""" string cleaning
Your boss decided to save money by purchasing some cut-rate optical character
recognition software for scanning in the text of old novels to your database.
At first it seems to capture words okay, but you quickly notice that it throws
in a lot of numbers at random places in the text."""
def string_clean(s):
    for element in s:
        if element in "0123456789":
            s = s.replace(element,"")
    return s        
   
"""
Write a function that returns the total surface area and volume of a box as 
an array: [area, volume]"""   
def get_size(w,h,d):
    a = 2*(w*h + h*d + w*d)
    b = w * h * d
    my_arr = [a,b]
    return my_arr
"""Find Mean
Find the mean (average) of a list of numbers in an array."""
def find_average(nums):
    return sum(nums)/ len(nums)
"""You need to write a function that reverses the words in a given string. 
A word can also fit an empty string. If this is not clear enough, 
here are some examples:
As the input may have trailing spaces, you will also need to ignore 
unneccesary whitespace."""
def reverse(st):
    s=st.split()
    return " ".join(s[::-1])
"""Implement a function named generateRange(min, max, step), which takes three arguments
 and generates a range of integers from min to max, with the step. The first integer is 
the minimum value, the second is the maximum of the range and 
the third is the step. (min < max)"""
def generate_range(min, max, step):
    my_arr = []
    for i in range(min,max+1,step):
        my_arr.append(i)
    return my_arr
"""This function takes two numbers as parameters, the first number being the 
coefficient, and the second number being the exponent.

Your function should multiply the two numbers, and then subtract 1 from the exponent. 
Then, it has to return an expression (like 28x^7). "^1" should not
 be truncated when exponent = 2."""
def derive(coefficient, exponent): 
    return str(coefficient *exponent) +"x^"+ str(exponent-1)
"""multiple index
Return a new array consisting of elements which are multiple of their own index
 in input array (length > 1)."""
def multiple_of_index(arr):
    new_arr  = []
    for i in range(1,len(arr)):
        if arr[i] % i == 0:
            new_arr.append(arr[i])
    if arr[0] == 0:
            new_arr.insert(arr.index(0),0)
    return new_arr
            