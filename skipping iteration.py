list = [2,6,3,7,9,3,1,4,6,8,4,2,1,2,5,7,3,2,5,4,7,4,8,6]

print("printing only numbers dividable by 2")

for x in list:
    if (x%2)==1:
        continue
    print (x)
print ("finished")