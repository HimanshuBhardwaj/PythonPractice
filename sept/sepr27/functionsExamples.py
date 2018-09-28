def changer(x, y):
    x = 2  # changes local value of x only
    y[0] = 'hi'  # changes shared object


x = 3
y = [2, 3, 4]
changer(x, y)

print x
print y


# default arguments

def func(a, b, c=10, d=100):
    print a, b, c, d


func(2, 3)


#while loop
x = 1
while x < 10:
    print x
    x = x + 1

print x



#forloop; 0--9
for x in range(10):
    print x


