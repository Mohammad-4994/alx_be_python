# Adding function for safe division 

def safe_divide(numerator, denominator):

    try :
        
       float(numerator), float(denominator)
       result =  float(numerator) / float(denominator)
               
    except ZeroDivisionError : 
        print("Error: Cannot divide by zero.")

    except ValueError : 
        print("Error: Please enter numeric values only.")    

    finally : 

        print(f"The result of the division is {float(numerator)/float(denominator):.1f}")
