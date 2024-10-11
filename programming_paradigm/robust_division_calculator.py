# Creating function for safe division 

def safe_divide(numerator, denominator):

    try :
       result = float(numerator) / float(denominator)
       return f"The result of the division is {float(numerator)/float(denominator):.1f}"

               
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."

    except ValueError: 
<<<<<<< HEAD
        return f"Error: Please enter numeric values only."    
=======
        return f"Error: Please enter numeric values only." 
>>>>>>> 7a1f71d6784a1164c56b2d06a6c9ba0d2169dd58
