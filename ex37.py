# del delete an object in python
# in python everything is an object

x = "Hello"
del x

try : 
    print(x)
except NameError as err: 
    print("Error : {}".format(err))

# if variable not defined in function
# python source it from outside
x = "Hello World"
def printx():
    try : 
        print(x)
    except NameError as err: 
        print("Error : {}".format(err))

printx()

# if a variable defined locally. python source it locally
# no matter where it is defined. python stops sourcing from outside.
def printx_again():
    x = "I am not listening to you"
    try : 
        print(x)
    except NameError as err: 
        print("Error : {}".format(err))

printx_again()

def printx_again_again():
    try : 
        print(x)
    except NameError as err: 
        print("Error : {}".format(err))
    x = "I am not listening to you"
printx_again_again()

def printx_again_again():
    global x
    try : 
        print(x)
    except NameError as err: 
        print("Error : {}".format(err))
    x = "I am not listening to you"
printx_again_again()
print(x)

def printx_again_again_again():
    global x
    try : 
        print(x)
    except NameError as err: 
        print("Error : {}".format(err))
    
    y = "I am not listening to you"
printx_again_again_again()

# keep an object within this blocks, disposal it once done.
with open('file_path.txt', 'w') as f : 
    f.write("hello")

x = "low"
# assert x == "hi", "x is not hi"

try:
    jack = rose
except NameError : 
    pass

for i in range(1, 10):
    # not implemented
    pass

print("Hello world")

# iterables are lists like structures you can loop over
# generators are literable that generate the value on the fly
# generators use ( ) 
mylist = ( x*x for x in range(3))
print (mylist)

for i in mylist : 
    print(i)

# yield is like return, but it returns a generator
def create_gen():
    mylist = range(3)
    for i in mylist : 
        yield i*i
# the first time the code encouter yield, it return a block of code
# that is a generator object
ls = create_gen()

# when a generator object runs, it runs the code in the object until hitting yield
# next time it continue to run the code until hitting yield
# the code terminate when loop finish without hitting yield
for i in ls : 
    print(i)

# exec execute a block of code, but it does not return anything
code = "print('Hello, James.')"
exec(code)

# lambda defines a function with a single line

plus1 = lambda num : num + 1

print(plus1(10))
