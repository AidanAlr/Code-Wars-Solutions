# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
#
# Notes:
#
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

# Time Complexity too slow
#
# def scramble(s1, s2):
#     for letter in s2:
#         if s1.count(letter) < s2.count(letter):
#             return False
#     return True
#

# Sets implement hashmaps so are much faster than searching through the string
def scramble(s1, s2):
    for l in set(s2):
        if s1.count(l) < s2.count(l):
            return False
    return True




print(scramble('katas', 'steak'))
print(scramble('cedewaraaossoqqyt', 'codewars'))

