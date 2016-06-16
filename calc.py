
def plus (x,y):
    return x + y
def minus (x,y):
    return x - y
def multiply (x,y):
    return x * y
def divide (x,y):
    return x / y

x = int(input ('Type first number:\n'))
y = int(input ('Type second number:\n'))
destiny = int(input('Choose your destiny: 1)add numbers; 2)subtract numers; 3)multiply numbers; 4)divide numbers:\n'))

if destiny == 1:
           print (plus(x,y))
elif destiny == 2:
           print (minus(x,y))
elif destiny == 3:
           print (multiply(x,y))
elif destiny == 4 and y == 0:
           print ('no way')
elif destiny == 4:
           print (divide(x,y))
else:
           print ('1,2,3 or 4, dude') #one time shit, all apologies
       
