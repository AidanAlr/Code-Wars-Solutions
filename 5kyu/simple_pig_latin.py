# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.
#
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    nl = []
    for word in text.split(' '):
        if word.isalpha():
            nl.append(word.replace(word[0], '', 1) + word[0] + 'ay')
        else:
            nl.append(word)

    result = ' '.join(nl)

    return result


print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))