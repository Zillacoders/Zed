from sys import exit

print(" Hello there, stranger! How do you fare?")

greeting = input("> ")

if greeting == ("I'm good!"):
    print("Alright! Let's get going!")

else:
    print(" Come on now! Let's work on that happy smile.")

print("What's your name, stranger?")

name = input("> ")

print("What's your ancient profession?")

profesh = input("> ")

print( f"Alright then {name}! Let's get started!")

print(f"You are {name}, the greatest {profesh} in the land!")
print("You seek the Altaris treasure, which can make you quite rich.\n You embark on the journey of a lifetime!")

print("A road diverges ahead of you...\n Which road do you choose? Left or Right?")

choice = input("> ")

if choice == ("left"):

    print("You are confronted by a troll")
    print("The troll asks for your credit card.")
    print("Especially your AMEX")
    print("What do you do?")

    left_road = False

    while True:
        pick = input("> ")

        if pick == "give AMEX":
            print("The troll steals your other cards, hits you with a hammer and leaves you for dead.")
            exit()

        elif pick == "beat troll":
            print("The troll attacks you with its club. You fight a mighty fight before you lose.\n You died an honorable death.")
            exit()

        elif pick == "walk away":
            print("you walk away and try another day.")
            exit()
        else:
            print("Try again")

elif choice == ("right"):

    print("You enter the forest and are suddenly lost amongst the trees.\n You are chased by beasts, all the while searching for a safe refuge.")
    print("Suddenly you enter a calm and serene place.\n You come across the tree spirit.")
    print("What do you ask?")



    right_road = False

    while True:
        question = input("> ")

        if question == ("where is the treasure?"):
            print("Now now. Don't be hasty. The treasure was inside you all along.\n You go back home dejected.")

        elif question == ("will I ever find a wife?"):
            print("You will! Just go home and do yo thang!")

        else:
            print("Try again")

