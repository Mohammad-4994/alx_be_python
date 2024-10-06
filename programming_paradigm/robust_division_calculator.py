# Adding function for safe division 

def safe_divide(numerator, denominator):

    try :
        result = numerator / denominator
        numerator = float(input("Enter numerator value: "))
        denominator = float(input("Enter denominator value: "))

    except ZeroDivisionError : print("Invalid for Zero Division")

    except ValueError : print("Please enter numeric values")

    else : print("The division is Safe")

    finally : 

        print(result)
