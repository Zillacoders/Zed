from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
in_file = open(from_file, 'r')

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CRTL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(from_file)

out_file.close()
in_file.close()
