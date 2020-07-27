i = 0
numbers = []

    while i > 0 :
        print(f"At the top i is {i}")
        numbers.append(i)
        break

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
