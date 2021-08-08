def translate(str):
    translate=''
    for letters in str:
        if letters.lower()in 'aioue':
            if letters.isupper():
                translate=translate +'Z'
            else:
                translate=translate +'z'
        else:
            translate=translate+letters

    return translate                
print(translate(input('write something :')))


