def perform_operation(num1, num2, operation):
    if operation=='add':
        result = num1 + num2
    elif operation=='subtract':
        result = num1 - num2
    elif operation=='multiply':
        result = num1 * num2
    elif operation=='divide':
        result = num1 / num2 if num2 != 0 else 0
    return result

perform_operation(40, 0, "divide")
    
