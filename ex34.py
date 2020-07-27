print('Enter a number: ')

i = 0
numbers = []
x = int(input())

while i < x :
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

# Halle fuckin lujah
