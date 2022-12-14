# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

""" print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)
 """
# re-declaring a variable works
works = 3


# to access a member of a sequence type, use []
print(mylist[2])

# use slices to get parts of a sequence
print(mylist[1:6])
"""print(mylist[1:4:2])"""

# you can use slices to reverse a sequence
""" print(mylist[5:3:-1]) """
# dictionaries are accessed via keys

# ERROR: variables of different types cannot be combined
print("string and number" + str(44))

# Global vs. local variables in functions

print(myfloat)

def frankyFuntion():
    global myfloat
    myfloat = 4.5
    print(myfloat)

frankyFuntion()
print(myfloat)

del myfloat
#print(myfloat)

