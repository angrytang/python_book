from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s"%(from_file, to_file))

a = open(from_file)
indata = a.read()

print("The input file is %d bytes long"%len(indata))

print("Does the output file exist? %r"%exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

b = open(to_file, 'w')
b.write(indata)
print("Alright, all done.")

b.close()
a.close()
