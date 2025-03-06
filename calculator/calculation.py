class Calculation:
    """
    A class to represent a calculation operation.

    This class stores two numbers (a and b) and an operation function,
    then performs the operation on the two numbers and returns the result.

    Attributes:
    -----------
    a : float
        The first number for the operation.
    b : float
        The second number for the operation.
    operation : function
        The function that performs the arithmetic operation (e.g., add, subtract, multiply, divide).
    """

    def __init__(self, a, b, operation):
        """
        Initialize the Calculation object with two numbers and an operation function.

        Parameters:
        -----------
        a (float): The first number for the operation.
        b (float): The second number for the operation.
        operation (function): The function to perform the arithmetic operation.
        """
        self.a = a
        self.b = b
        self.operation = operation  # Store the operation function

    def get_result(self):
        """
        Perform the stored operation on the two numbers.

        Calls the operation function (e.g., add, subtract, multiply, divide) 
        with the two numbers (a and b) and returns the result.

        Returns:
        --------
        float: The result of applying the operation on a and b.
        """
        # Call the stored operation with a and b
        return self.operation(self.a, self.b)