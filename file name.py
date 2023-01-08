#creating the code to find its  python 
fname = input("enter the file name:")
x = fname.split(".")
y = x[-1]
if y=="py":
    print ("the extention is"+"python")
else:
    print("it is not a python code")
