# Python Program to find Largest and Smallest Number in a List 
 
List = []
Number = int(input("Please enter element length in list "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    List.append(value)
 
print("The Smallest Element in this List is : ", min(List))
print("The Largest Element in this List is : ", max(List))
