num = int(input('How many integers you want to calculate: '))
numbers = []
for n in range(1, num+1):
    numbers.append(int(input('Enter an integer:')))

print('Here is a list of the numbers you created:', numbers)
max = max(numbers)
min = min(numbers)
sum = sum(numbers)
len = len(numbers)
avg = sum/len
print ('Based on these numbers, you get the following results:')
print('The maximum number:', max)
print('The minimum number:', min)
print('Total of these numbers:', sum)
print('The average of these numbers:', avg)
