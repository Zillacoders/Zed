from sys import exit

def left_path():
    print("You are now on the path to freedom.")
    print("You meet a lady.")
    print("What do you do?")
    left_path = False

    while True:
        choice = input("> ")

        if choice == "say hello":
            print("She friendzones you immediately. You get rejected. You are all alone.")
            print("Go home. Bye!")
            exit()

        elif choice == "catcall her":
            print("You shameless cow! You kiss your mother with that mouth? ")
            exit()

        elif choice == "ask her where to go next" and not left_path:
            print("She points you to a tavern.")
            print(" You ask for the treasure.")
            print("They laugh and tell you the treasure is a myth.")
            exit()
        else:
            print("She looks at you weirdly.")


def left_road():
    print("You are confronted by a troll")
    print("The troll asks for your credit card.")
    print("Especially your AMEX")
    print("What do you do?")
    left_road = False

    while True:                                      #an infinite loop has been created so as to circle back to the same decision without the apporpriate answer
        choice = input("> ")

        if choice == "give AMEX":
            dead("The troll steals your other cards, hits you with a hammer and leaves you for dead.")
            exit()

        elif choice == "hit troll" and not left_road:
                print("You fight a bloody battle with the troll. You still die")
                print("bitch.")
                left_road = True
                exit()

        elif choice == "walk around" and not left_road:
            left_path()
        else:
            print("Don't be a chicken, ya lil shit.")


def right_road():
    print("You keep walking")
    print("You come across the tree spirit.")
    print("What do you ask?")
    right_road = False

    while True:
        choice = input("> ")

        if "where's the treasure?" in choice:
            print("You're immediately knocked back in time. You are now back to square one")
            exit()
        elif choice == "will I ever get married?":
            print('The tree says "Well!\n I do know a fair maiden who wants to get married." ')
            print("You meet the girl of your dreams and realise that she was the treasure all along.")
            exit()
        elif "what's going on here?" in choice:
            dead("The tree tells you his life story and puts you to sleep.")
        else:
            print("The tree looks at you in bewilderment!")


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("Hello there! Hope yer ready for an adventure!")
    print("You are a traveller on a journey.")
    print("You come across two roads. Which one do you traverse?")

    choice = input("> ")

    if choice == "left":
        left_road()
    elif choice == "right":
        right_road()
    else:
        dead("You stumble around the room until you starve.")


start()
