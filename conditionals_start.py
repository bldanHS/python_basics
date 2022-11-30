#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 1000, 100

    # conditional flow uses if, elif, else
    if x < y:
        result = "x is less than y"
    elif x == y:
        result = "x and y is the same"
    else:
        result = "y is less than x"
    print(result)


    # conditional statements let you use "a if C else b"

    result2 = "x is less than y" if x < y else "x is greater or equal to y" 
    print(result2)

    # match-case makes it easy to compare multiple values
    value = "45"

    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three":
            result = 3
        case "four" | "five":
            result = (4,5)
        case _:
            result = -1

    print(result)

if __name__ == "__main__":
    main()
