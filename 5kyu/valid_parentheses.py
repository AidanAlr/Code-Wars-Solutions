# Write a function that takes a string of parentheses, and determines if the order of the
# parentheses is valid. The function should return true if the string is valid, and false if it's
# invalid.
#
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= input.length <= 100
#
# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters.
# Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat
# other forms of brackets as parentheses (e.g. [], {}, <>).
#

def valid_parentheses(string):
    stack = []
    for b in string:
        if b not in '()':
            string = string.replace(b,'')

    for b in string:
        if b == '(':
            stack.append(b)
        else:
            # If b is not opening parentheses check top of stack and pop it
            # If pop matches closing parentheses continue to next b: else return False
            if not stack:
                return False
            current = stack.pop()
            if current == '(' and b != ')':
                return False
    # If stack not empty too many opening brackets
    if stack:
        return False
    return True

print(valid_parentheses("hi(hi)()"))