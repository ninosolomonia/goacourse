"""Your task is to sum the differences between consecutive pairs in the array 
in descending order.
Example
[2, 1, 10]  -->  9
In descending order: [10, 2, 1]
Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9
If the array is empty or the array has only one element the result should be 0"""
numbers = ("1 2 -3 4 5 -4 -9")
nums = numbers.split(" ")
print(nums)


"""Combine strings function
Create a function named (combine_names) that accepts two parameters (first and last name).
 The function should return the full name."""
def combine_names(first,last):
    return first + " " + last

"""
Find the Difference in Age between Oldest and Youngest Family Members"""
def difference_in_ages(ages):
    list=[min(ages),max(ages),(max(ages)- min(ages))]
    return tuple(list)

"""the falling speed of petals
Write a function that receives the speed (in cm/s) of a petal as input, and 
returns the time it takes for that petal to reach the 
ground from the same branch."""
def sakura_fall(v):
    if v > 0 :
        return 400 / v
    return 0

"""How many stairs will Suzuki climb in 20 years?
"""
def stairs_in_20(stairs):

    return (sum(stairs[0]) + sum(stairs[1]) + sum(stairs[2]) + sum(stairs[3]) + sum(stairs[4])+
            sum(stairs[5])+sum(stairs[6])) * 20

"""remove the time
Write a function that takes the website date/time in its original string format and 
returns the shortened format"""
def shorten_to_date(long_date):
    result = long_date.split(",")
    return result[0]