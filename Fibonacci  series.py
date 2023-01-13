#required no.of series 
n = int(input ("enter the value:"))
#starting value
a = 0
#the second value
b = 1
count = 0
#loop to excute it
print("the fibonical sries is :")
while count < n:
    print( a)
    c = a+b
    a=b
    b=c
    count+=1
