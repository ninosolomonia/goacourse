"""
Find the first non-consecutive numbe"""
def first_non_consecutive(arr):
    for i in range(0,(len(arr)-1)):
        if arr[i+1] - arr[i] != 1:
            return arr[i+1]
    return  None
def first_non_consecutive(arr):
    for i in range(0,len(arr) - 1):
        if arr[i] == arr[i + 1] - 1:
            continue
        return arr[i + 1]
    return None


"""Complete the solution so that it reverses all of the words within the string passed in.

Words are separated by exactly one space and there are no leading or trailing spaces."""   
def reverse_words(s):
    split_arr = s.split(" ")
    split_arr.reverse()
    new_str = ""
    for element in split_arr:
        new_str += element + " "
        
        
    return new_str[:-1]


"""
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation."""  
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)  

"""Our football team has finished the championship.

Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]

Points are awarded for each match as follows:

if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)"""

def points(games):
    score = 0


    for element in games:
        split_arr = element.split(":")

        if split_arr[0] > split_arr[1]:
            score += 3
        elif split_arr[0] == split_arr[1]:
            score += 1

    return score



"""Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array or list ( depending on language ).
"""
def count_by(x, n):
    my_arr = []
    for i in range(1,n+1):
        my_arr.append(i*x)
    return my_arr