def add(num1, num2):
    sum = num1 + num2
    return sum

def sub(num1, num2):
    diff = num1 - num2
    return diff

def multi(num1, num2):
    prod = num1 * num2
    return prod

def div(num1, num2):
    quot = num1/num2
    return quot

def mod(num1, num2):
    rem = num1 % num2
    return rem

def operator_switch(num1, num2, operator):
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return sub(num1, num2)
    elif operator == "*":
        return multi(num1, num2)
    else:
        return div(num1, num2)

