# vypis hlasku pomocou fstringu
from os.path import split

name = 'John Doe'
age = 34
occupation = 'gardener'

msg =f'{name} is a {occupation} and he is {age} years old.'
print (msg)


# vypis sumu
# vypis prvy, posledny prvok
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(vals[1])
print (vals[-1])
print(sum(vals))

mysum = 0
for val in vals:
    mysum += val
print (mysum)


# vypocitaj sumu
data = "1,2,3,4,5,6,7,8,9,10"
fields = data.split(',')
mysum2 = 0

for field in fields:
    mysum2 += int(field)
print (mysum2)
