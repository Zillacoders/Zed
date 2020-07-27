def cheese_and_crackers(cheese_count, boxes_of_crackers):           #using def to allot a name to the variables
    print(f"You have {cheese_count} cheeses!")                      #print statement one
    print(f"You have {boxes_of_crackers} boxes of crackers!")       #print statement two
    print("Man that's enough for a party!")                         #print statement three
    print("Get a blanket!")                                         #print statement four


print("We can just give the function numbers directly:")            #print statement five
cheese_and_crackers(20, 30)                                         #assign ints to variable, quantifying the "Cheese and Cracker"

print("OR, we can use variables from our script:")                  #print statement six
amount_of_cheese  = 10                                              #adding int to the variable
amount_of_crackers = 50                                             #adding int to the variable

cheese_and_crackers(amount_of_cheese, amount_of_crackers)           #calculate the amount of "Cheese and crackers" stated above



print("We can even do the math inside too:")                        #print statement seven
cheese_and_crackers(10 + 20, 5 + 6)                                 #add the stated figures


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers)
