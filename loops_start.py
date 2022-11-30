#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0

    # TODO: define a while loop
    while(x <= 10):
        print(x)
        x += 1


    # TODO: define a for loop
    
    #for i in range(5,10):
    #    print(x)

    # TODO: use a for loop over a collection
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]


    # TODO: use the break and continue statements
    for x in range(10,30):
        if(x % 3 == 0):
            continue
        if(x == 20):
            break
        print(x)

    # TODO: using the enumerate() function to get index 
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for x, d in enumerate(days):
        print (x, d)
    
  
if __name__ == "__main__":
    main()
