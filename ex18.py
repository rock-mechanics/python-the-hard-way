# this one is your script with argv
# we need to do an unpack for the arguments
def print_two(*args):
    arg1, arg2 = args
    print("arg1 : {}, arg2 : {}".format(arg1, arg2))

# okay, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1 : {}, arg2 : {}".format(arg1, arg2))

# this just takes one argument
def print_one(arg1):
    print("arg1 : {}".format(arg1))

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two('Zed', "Shaw")
print_two_again('Zed', 'Shaw')
print_one("First!")
print_none()

