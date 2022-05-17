print('Calculate your participation and discussion points \n -------------------------------')
user_name = input('What is your name? ')
print('Thank you ' + user_name)
print('Please answer two questions:')
unexcused_absences = int(input('How many unexcused absences do you have?: '))
tardy = int(input('How many times have you being tardy? '))
print ('----------------------------------------------')

print('The number of unexcused absences you entered:' , unexcused_absences )
print ('The number of being tardy you entered:' , tardy )
print ('----------------------------------------------')

MIX = int(format(tardy/3, ".0f"))

print ( tardy , 'times being tardy is equel to' , unexcused_absences , 'unexcused absence(s)')
print ( 'Thus, the number of total unexcused absence(s):' ,  MIX + unexcused_absences )
print ('----------------------------------------------')

X = MIX + unexcused_absences
if X==1: print('Thus, your participation and discussion point: 48/50')
if X==2: print('Thus, your participation and discussion point: 45/50')
if X==3: print('Thus, your participation and discussion point: 41/50')
if X==4: print('Thus, your participation and discussion point: 33/50')
if X==5: print('Thus, your participation and discussion point: 23/50')
if X==6: print('Thus, your participation and discussion point: 9/50')
if X==7: print('Thus, your participation and discussion point: 0/50')
elif X >7: print('Thus, your participation and discussion point: 0/50')

a = 10
b = 5
print (a%b)
print (b%a)

x = (a!=b)
print (x)