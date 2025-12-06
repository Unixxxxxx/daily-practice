#false
x = False
print(x)

#non
x = None
print(x)

#True
flag = True
print(flag)


#and 
print(4>3 and 3<10)

#as
import math as m 
print(m.sqrt(16))


#assert 
x = 10
assert x > 5 


#async 

async def hello():
    return "Hii"

#brack 
for i in range(5):
    if i == 3:
        break 
    print(i)

#class 
class new:
    pass

# continue
for i in range(5):
    if i == 2:
        continue 
    print(i)

#def 
def greet():
    print('Hello')

#del
xp =50 
del xp

#elif
p = 10
if p == 5:
    print('Five')
elif x ==   10:
    print("Ten")

#else
x = 3 
if x > 5:
    print("Big")
else:
    print("small ")

#except
try : 
    print(10/0)
except:
    print("Error!")

#finally
try :
    x = 10/0
except:
    print("Caughr error")
finally:
    print("Always runs")


#for 
for i in range(3):
    print(i)


#from 
from math import sqrt 
print(sqrt(16))

#global
x = 10
def change():
    global x
    x = 20
change()
print(x)


#if 
if 5 >2:
    print("yes")


# import 
import math 
print(math.pi)

#in
print("a" in "apple")

#is 
y = None 
print(y is None)


#lambda 
square = lambda x: x*x
print(square(4))

# nonlocal 
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner"
    inner ()
    print()
outer()

#not 
print(not True )


#or
print(5<3 or 10>8)

#PASS
def fun():
    pass
#raise 
try:
    raise ValueError("Custom Error")
except ValueError as e:
    print("Handled error:", e)

#return 
def add():
    return 5+5
print(add())

#try 
try:
    print(10/2)
except:
    print("Error")

#while 
i = 1
while i <= 3:
    print(i)
    i += 1

#with 
with open("test.txt", "w") as f:
    f.write("Hello")


#yield
def gen():
    yield 1
    yield 2

for i in gen():
    print(i)

