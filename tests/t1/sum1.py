# write a program that reads in 10 numbers, then prints the sum of those

numbers = []
x = 0
i=0
while i in range(10):
    response = input("input an integer.")
    x = x + int(response)
    i = i + 1
    numbers.append(response)
print(numbers)
print(x)