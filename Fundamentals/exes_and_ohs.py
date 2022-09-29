# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean
# and be case insensitive. The string can contain any char.
#
# Examples input/output:
#
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    s = s.upper()
    xc = s.count('X')
    oc = s.count('O')
    if oc == xc:
        return True
    return False

print(xo("xooxx"))