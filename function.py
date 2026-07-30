def calculator(num1, num2, operator):

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero!"

    else:
        return "Invalid Operator!"



num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

result = calculator(num1, num2, operator)

print("Result =", result)



def days_of_week(days):
    match days:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day number! Please enter a number between 1 and 7."

day_number = int(input("Enter a number (1-7) to get day of the week: "))
day_name = days_of_week(day_number)
print(day_name)