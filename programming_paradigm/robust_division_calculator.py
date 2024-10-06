# Adding function for safe division 

def safe_divide(numerator, denominator):

    try :
        
        float(numerator) = input("Enter numerator value: ")
        float(denominator) = input("Enter denominator value: ")
       
    except ZeroDivisionError : print("Error: Cannot divide by zero.")

    except ValueError : print("Error: Please enter numeric values only.")

    else :
        result =  numerator / denominator
        print("The division is Safe")

    finally : 

        print(f"The result of the division is {result}")
