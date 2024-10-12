class Calculator:

    calculation_type = "Arithmetic Operations"


    @staticmethod
    def add(a, b):

        return a + b 
    print(f"Calculation type: {calculation_type}")
    


    @classmethod
    def multiply(cls, a, b):

        return a * b
