from sys import argv            #from system import argv( value unpacker)

script, filename = argv         #introduce a script and filename

print(f"We're going to erase {filename}.")     #command prompt1
print("If you don't want that, hit Ctrl-C (^C).") #command prompt2
print("If you do want that, hit RETURN.") #command prompt3

input("?")    #User types in the control that they want. Ctrl C exits python. Enter proceeds with the program.

print("Opening the file...")  #file is opened
target = open(filename,'w')   #variable is named target. target opens the filename specified in the argument. Write function is enabled.

print("Truncating the file. Goodbye!") #prompt to erase file
target.truncate()   #truncate wipes out the file

print("Now I'm going to ask you for three lines.") #the program asks for the replacement text

line1 = input("line 1: ")   # 1
line2 = input("line 2: ")   # 2
line3 = input("line 3: ")   # 3

print("I'm going to write these to the file. ") # implementation warning

target.write(line1) #implementation
target.write("\n")  #implementation
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()  #python closes
