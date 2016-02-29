# copy the code from sum1.py into this file, THEN:
# change your program so it keeps reading numbers until it gets a -1, then prints the sum of all numbers read
numbers = []
x = 0
i=0
notNeg = True
while notNeg:
    response = input("input an integer.")
    if int(response) < 0:
        notNeg = False
    else:
        x = x + int(response)
        i = i + 1
        numbers.append(response)
print(numbers)
print(x)