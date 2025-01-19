def safe_divide(numerator, denominator):
    try:
        num1 = float(numerator)
        num2 = float(denominator)
        if num2 != 0:
            result = num1 / num2
            return f"The result of the division is {result}"
        else:
            raise ZeroDivisionError
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
