first_name = raw_input("Please Enter Your First Name: ")
last_name=raw_input ("Please Enter your Last Name:" )

print ("These are the months of the year \n March=1\n April=2\n May=3\n June=4\n July=5 \n August=6\n September=7\n October=8 \n November=9\n december=10 \n January=11\n February=12")
day= raw_input ("Please Enter Your Day of birth as a number between 1-31:" )
month= raw_input ("Please Enter Your birth Month as a number between 1-21:" )
year=raw_input ("Please Enter Year:")
century = raw_input("Please Enter Century:")
B=int(day)
A=int(month)
if A>12:
    print "You are out of range!"
C=int(year)
D=int(century)
if A==11:
    C=C-1
elif A==12:
    C=C-1


sunday=0
monday=1
tuesday=2
wednessday=3
thursday=4
friday=5
saterday=6
W = (13*A - 1) / 5
X=C/4
Y=D/4
Z = W + X + Y + B + C - 2*D
R = Z%7


    
print first_name+' '+last_name+ " was born on",
print B,
print "/",
print A,
print "/",
print C,
print "In the ", D, "Century"

if R==0:
    print "Day is Sunday"
elif R==1:
    print "Day is Monday"
elif R==2:
    print "Day is Tuesday"
elif R==3:
    print "Day is Wednesday"
elif R==4:
    print "Day is Thursday"
elif R==5:
    print "Day is Friday"
elif R==6:
    print "Day is Saterday"
