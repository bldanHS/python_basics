#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def function1():
    print("I am a function")


# TODO: function that takes arguments

def function2(arg1, arg2):
    print("the arguments passed were: "+ arg1 + " " + arg2)



# TODO: function that returns a value
def stringConcat():
    word1 = input("Type in the first word: ")
    word2 = input("Type in the second word: ")
    return word1+word2



# TODO: function with default value for an argument

def doubleUp(x=1):
    return 2*x


# TODO: function with variable number of arguments

def multi_add(*args):
    result = 0
    for i in args:
        result += i
    return result

""" print(function1)
print(function1())

print(function2(2,4))
print(stringConcat())
 """

print(multi_add(2,55,6,7,10))
print(doubleUp(3))