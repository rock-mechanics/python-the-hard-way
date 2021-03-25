from sys import argv

#unpack argv
script, input_file = argv

def print_all(f):
    print( f.read() )

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print("{} : {}".format(line_count, f.readline()))

current_file = open(input_file)

print("Let's print the whole file : \n" )
print_all(current_file)

print("Let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines")
current_line = 1
print_a_line(current_line, current_file)

current_line = 2
print_a_line(current_line, current_file)

current_line = 3
print_a_line(current_line, current_file)

# try some seek methods to see what is happening
# move the pointer to the second character index 1
# from the beginning of the file 0
current_file.seek(1,0)

# when you readline, it reads all the way to the end of \n character
# at the same time, it also moves the seek pointer after the \n character
print(current_file.readline())

current_file.close()
