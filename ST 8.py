list_1=[]
list_2=[]
list_3=[]
def list_1_odd(list_1):
    list_1=[n for n in list_1 if n%2!=0]
    return list_1

def list_2_even(list_2):
    list_2=[n for n in list_2 if n%2==0]
    return list_2

num_1=int(input("Enter the number of values in list 1: "))
num_2=int(input("Enter the number of values in list 2: "))

print("Enter the values of list 1: ")
for i in range(num_1):
    list_1.append(int(input()))
odd_1=list_1_odd(list_1)

print("Enter the values of list 2: ")
for i in range(num_2):
    list_2.append(int(input()))
even_2=list_2_even(list_2)

list_3=odd_1+even_2
print(list_3)


