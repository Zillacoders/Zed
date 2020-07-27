people = 30                 #Variable1
cars = 40                   #variable2
trucks = 15                 #variable3


if cars > people:                                       #boolean expression 'if' establishing a basic choice
    print("We should take the cars.")                   #print statement.
elif cars < people:                                     #elif states the alternative to the question statement
    print("We should not take the cars.")               #print statement
else:                                                   #Unlike elif, only one else is applicable.
    print("We can't decide.")                           #print statement

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we can take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
