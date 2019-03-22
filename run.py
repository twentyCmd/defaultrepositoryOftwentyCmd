nums = eval(input())
x=0
y=1
z=1
i=0
print ("the fibbonnaci series goes like:")
while i<nums:
    i += 1
    z=x+y
    print (z)
    x=y
    y=z
print ("end of the line dude")