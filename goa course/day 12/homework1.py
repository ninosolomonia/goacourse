#It's pretty straightforward. 
#Your goal is to create a function that removes the first and 
#last characters of a string. You're given one parameter, the original string.
#You don't have to worry with strings with less than two characters


def remove_char(s):
    new_str = ""
    for char in s:
        if char == s[0] or char == s[-1]:
            new_str = s[1:-1]
    return new_str  