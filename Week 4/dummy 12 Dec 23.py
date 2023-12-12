def addition(list):
    
    total = 0

    for value in list:
        total += value

    return total

def subtraction(list):
    
    total = list.pop(0) # [1,2,3]

    for value in list:
        total -= value # (1-2)-3

    return total



def division(list):
    try:
        total = list.pop(0) # Whatever the first value in my list was

        for value in list:

            total /= value

        if total == 0.00:
            return "What did you expect?"
        else:
            return total
    except ZeroDivisionError:
        print("Don't divide by zero silly.")

def multiplication(list):
    
    total = 1

    for value in list:
        total *= value

    return total


try:

    numbers = []
    amount = int(input("How many numbers in your calculation? : "))

    for num in range(1,amount+1):

        x = float(input(f"Enter value {num} : "))
        numbers.append(x)

except ValueError:
    print("Invalid Value detected!")

operation = input("Please enter the mathematical operation desired \
(+, -, /, *) : ")

if operation == '+':

    total = addition(numbers)
    print(f"The sum of {numbers} is : {total:.2f}")

elif operation == '-':

    total = subtraction(numbers)
    print(f"The difference of {numbers}: {total:.2f}")

elif operation == '*':

    total = multiplication(numbers)
    print(f"The product of {numbers} : {total:.2f}")

elif operation == '/':

    total = division(numbers)
    print(f"{total}")