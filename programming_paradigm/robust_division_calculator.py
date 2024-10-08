# Adding function for safe division 

def safe_divide(numerator, denominator):

        
    float(numerator), float(denominator)

    if denominator == 0 :
   
        print("Error: Cannot divide by zero.")

    elif type(numerator) or type(denominator) == str : 
        print("Error: Please enter numeric values only.")    

    else : 

        print(f"The result of the division is {float(numerator)/float(denominator): .1f}")
