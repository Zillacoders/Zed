#RISHABH GAME
import random

class DeathScene():
    def __init__(self, Eaten, Carcass, Drag):
        self.Eaten = Eaten
        self.Carcass = Carcass
        self.Drag = Drag

d1 = DeathScene("The 'Monster' pins you down and eats you up. You are now a pile of bones.",
"Wow. I don't think anyone's gonna recognize that carcass.",
"The troll drags you back to the cave for dinner.")

def ending():
    print("You got shredded to bits.That was a waste of time. I'll write to your mother to let her know you're dead.")

print("Welcome adventurer! It seems you are finally awake.\nIt looks like you had alot to drink! How are you feeling?\n\n(Good/Bad)")

Player_input = input()

if Player_input == "Good":
    print("Brilliant! let's get going then!" )
    print("\n")
elif Player_input == "Bad":
    print("Go to sleep then! I'll wake you up later.")
    exit()
else:
    while Player_input != "Good" or "Bad":
        print("Are you still drunk?")
        break
        exit()

day = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

print("Today is", end = " " )                                                            ## This is a same line code. Use it to print two sentences on the same line.
print(random.choice(list(day)), end = "")
print(", so you shouldn't have any issues along the way.")


print("\n")
print("let's get going shall we? You walk out of the tavern and are facing the road towards the adventure.\nThe village is preparing for the winter by hoarding wood and stocking up on the meals.\n\nYou keep walking.")

print("Press 'X' to keep walking.")

X_input = input()
while True:
    if X_input == "X":
        print("Keep walking")
        X_input = input()
        break
        continue
        break                                                                       # Do not change this. This repeater works on the break and continue statements.
    else:
        print("We need to get going!")
        break

print("While walking down the road, you notice a drop in the temperature. Luckily, you packed some warm clothes!\n\nYou put on your favorite jacket and notice a rustling in the bushes.")
print("A monster jumps out of the bush and leaps towards you! You spot a stick next to you. What do you do?")

decision1 = input()

while True:
    if decision1 == "Kick":
        print(d1.Carcass)
        print("Ya dead")
        exit()

    elif decision1 == "Run":
        print(d1.Eaten)
        print("I'll call the coroner.")
        exit()

    elif decision1 == "Fight with stick":
        print("You survive...for now.")
        break
    else:
        print("Now's not the time to doubt yourself!")
        decision1 = input()

print("You are now going deeper into the woods.", end = " ")

print("After a long journey, you reach a crossroad.\nYou can now choose where you'd like the road to lead.")

print("Which road do you choose? Left or Right?")

choice = input("> ")

if choice == ("Left"):

    print("You are confronted by a troll")
    print("The troll asks for your credit card.")
    print("Especially your AMEX")
    print("What do you do?")

    left_road = False

    while True:
        pick = input("> ")

        if pick == "Give AMEX":
            print("The troll steals your other cards, hits you with a hammer and leaves you for dead.")
            exit()

        elif pick == "Beat troll":
            print(d1.drag)
            exit()

        elif pick == "Walk away":
            print("You walk away and try another day.")
            exit()
        else:
            print("Try again")

elif choice == ("Right"):
    print("You enter the forest and are suddenly lost amongst the trees.\n You are chased by beasts, all the while searching for a safe refuge.")
    print("Suddenly you enter a calm and serene place.\n You come across the tree spirit.")
    print("What do you ask?")

    tree_say = ('Hmmmm that could create a whole in the universe.' , 'Maybe you should rethink your questions' ,'Enough of this mockery, you whippersnapper!' , 'I am getting too old for this s***', '*The tree looks at you with confusion*')

    right_road = False

    while True:
        question = input("> ")

        if question == ("Where is the treasure?"):
            print("Now now. Don't be hasty. The treasure was inside you all along.\n You go back home dejected.")

        elif question ==("Will I ever find a wife?"):
            print("You will! Just go home and do yo thang!")

        else:
            print(random.choice(list(tree_say)))
