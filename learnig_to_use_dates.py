import datetime
x = datetime.datetime.now()

print ("now is year {} {} of {}".format((x.strftime("%Y")),(x.strftime("%d")),(x.strftime("%B"))))

y = x.strftime("%w") # y is a string because (x.strftime("%w")) returns a string

if y == "1" : # thats why i used  "" in the "if" constructions
    print ("Current day: Monday")
    print ("omg i hate mondays")
elif y == "0" :
    print("Current day: Sunday")
    print ("today is cool but be careful cuz you gotta stay sharp for tomorrow")
elif y == "2":
    print("Current day: Tuesday")
    print ("alright time to put myself together")
elif y == "3":
    print("Current day: Wednesday")
    print("halfway now, keep it goin'")
elif y == "6":
    print("Current day: Saturday")
    print("ooo yeah party day today")