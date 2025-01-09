def perform_operation(num1, num2, operation):
    if operation=='add':
        result = num1 + num2
    elif operation=='subtract':
        result = num1 - num2
    elif operation=='multiply':
        result = num1 * num2
    elif operation=='divide':
        result = 0 if num2 == 0 else num1 / num2
    return result

perform_operation(0, 6, "divide")
    
