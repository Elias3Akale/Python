print('Converting Fahrenheit to Celsius')
user_name = input('Please enter your first name: ')

print('thank you ' + user_name )
F = float(input('Please enter temperature in Fahrenheit: '))
C = format((F-32)*5/9, ".2f")

print( F , "in Fahrenheit is" , C , 'degrees in Celsius')

print('Converting Celsius to Fahrenheit')

C2 = float(input('Please enter temperature in Celsius: '))
F2 = format((C2*9)/5+32, ".2f")

print( C2 , "in Celsius is" , F2 , 'degrees in Fahrenheit')
