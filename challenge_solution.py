# Solution to programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#
""" 
def is_palindrome(teststr):
    # use the slice trick to reverse the string
    if teststr == teststr[::-1]:
        return True
    return False

run = True
while (run):
    teststr = input("Enter string to test for palindrome or 'exit':")

    # If the user types "exit" then quit the program
    if teststr == "exit":
        run = False
        break

    # convert the string to all lower case
    teststr = teststr.lower()

    # strip all the spaces and punctuation from the string
    newstr = ""
    for x in teststr:
        if x.isalnum():
            newstr += x

    print("Palindrome test:", is_palindrome(newstr))
 """



def ispalindrome(userinput):
    if userinput == userinput[::-1]:
        return True
    else:
        return False


go = True
while(go):
    userinput = input("Enter a string, to check wether it's a palindrome or not: (type exit to quit)")
    if userinput == "exit":
        go = False
        break
    userinput == userinput.lower()

    userinputChecked = ""
    for i in userinput:
        if(i.isalnum()):
            userinputChecked+=i


    print("Palindrome checking: ", ispalindrome(userinputChecked))

