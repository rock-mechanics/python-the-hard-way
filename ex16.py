from sys import argv

script, filename = argv

print("We are going to erase {}".format(filename))
print("If you don't want that, hit Ctrl-C")
print("If you do want that, hit Return")

input("?")

print("Opening the file ...")
target = open(filename, 'w')

print("truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("Line 1 : ")
line2 = input("Line 2 : ")
line3 = input("Line 3 : ")

print("I am going to write these to the file.")
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print("And finallt, we close it")
target.close()


