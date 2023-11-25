#https://www.codewars.com/#kata/search/python?q=&r%5B%5D=-8&xids=completed&beta=false&order_by=total_completed%20desc
def solution(string):
    str = ""
    for i in range(len(string)):
        str += string[-i -1]
        i -= 1 
    return str    
print(solution("hello"))        