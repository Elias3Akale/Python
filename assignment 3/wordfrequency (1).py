file = open('dream.txt' , 'r')
Counter = 0
search = input('Enter a word to see how many times it occurs in this file: ')
search = search.lower()
search = search.replace ('', '')
search = search.strip()

for line in file:
    for word in line.split():
        lookup = word
        lookup = lookup.lower()
        lookup = lookup.replace('','')
        lookup = lookup.strip()
        if lookup == search:
            Counter += 1

if Counter > 2: 
    print ('The word', str(search),  'appeared', str(Counter), 'times' )
elif Counter == 2:
    print ('The word', str(search), 'appeared twice')
elif Counter == 1:
    print ('The word', str(search), 'appeared once')
elif Counter == 0:
    print ('The word', str(search), 'dosent exist')
