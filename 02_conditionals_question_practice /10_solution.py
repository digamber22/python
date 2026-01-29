age = 6
pet = 'dog'

if pet == 'dog':
    if age < 2:
        res = 'Puppy food'
    elif age > 5:
        res = 'Senior dog food'
    else:
        res = 'Adult dog food'

elif pet == 'cat':
    if age < 2:
        res = 'Kitten food'
    elif age > 5:
        res = 'Senior cat food'
    else:
        res = 'Adult cat food'

print(age, res)
