from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from {} to {}".format(from_file, to_file))

in_file=open(from_file)
indata = in_file.read()
# indata = open(from_file).read()
# file object without will be automatically closed by the os

in_file.close()

print("The input file is {} bytes long".format(len(indata)))
print("Does the output file exists? {}".format(exists(to_file)))

print("Ready, hit Enter to continue, Ctrl-C to abort")
input("?")

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")
out_file.close()

