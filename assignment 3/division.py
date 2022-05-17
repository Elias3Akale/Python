while True:
    try:
        x = float(input('Enter the first number:'))
        y = float(input('Enter the second numner:'))
    except ValueError:
        print('Entered value is not a number')
    else:
        try:
            result = x / y
        except ZeroDivisionError:
            print('Can’t divide by zero')
        else:
            print("The division: ", result)
            break