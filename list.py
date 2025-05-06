myList = [ 'sdk', 'tfk', 'jkl', 'abc', 'xyz' ]

myList.append('123')
myList.append('456')

if 'abcc' in myList:
    myList.remove('abc')
else:
    myList.append('abc')

print(myList)

for i in myList:
    print(i)