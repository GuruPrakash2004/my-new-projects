n = int (input("enter the no.of elementes in list:"))
#creating the empty list to store the values
List =[ ]
 
for i in range (0,n):
    a = int(input("enter the elements:"))
    List.append(a)
 #new list is created 
print(List)

g = [ ]
#getting the positive inputs
for j in List:

    if j > 0:
        g.append(j)
print("the list of positive elemets :",g) 

