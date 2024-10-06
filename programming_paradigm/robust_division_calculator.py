# Adding function for safe division 

def safe_divide(numerator, denominator):

    try :
        
       float(numerator), float(denominator)
    #    result =  numerator / denominator
               
    except ZeroDivisionError : 
        print("Error: Cannot divide by zero.")
        # result = None

    except ValueError : 
        print("Error: Please enter numeric values only.")
        # result = None

    else :
        
        print("The division is Safe")
       

    finally : 

        print("The result of the division is {:.1f}".format(numerator/denominator))
