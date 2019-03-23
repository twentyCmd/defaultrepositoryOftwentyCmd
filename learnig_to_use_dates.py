import datetime
x = datetime.datetime.now()
print ("now is")
print(x)
if (x.strftime("%w"))==1:
    print ("omg i hate mondays")
elif (x.strftime("%w"))==0:
    print ("today is cool but be careful cuz you gotta be sharp for tomorrow")
elif (x.strftime("%w"))==6:
    print ("ooo yeah party day today")
