def fact(n):
    """
    Calculate the factorial of a positive integer n
    Parameter:
     - n: Positive integer 
    Return:
    - Factorial of n
    """
    if n < 0:
        raise ValueError('Factorial is not defined for negative numbers')
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)