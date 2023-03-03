x = [1,2,3,4,5,6,7,8,9,10,4]
y = list(set(x))

print (x)
print (y)

if len(x) == len(y):
    print ("list is full of unique numbers")
else:
    print ("list has duplicates")
