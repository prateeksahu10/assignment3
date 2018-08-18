# q1 Create A List
l1=[]
a=int(input("enter number of variables"))
print("enter element")
for i in range (a):
    n=int(input())
    l1.append(n)
print(l1)

# q2 Concatenate lists
list=['ball','bat','baseball']
l1.extend(list)
print(l1)

# q3 count occurance in a list
list1=[1,2,3,5,1,2,3,5,2,3]
print(list1.count(2))

# q4 sort the list
list2=[5,25,6,49,66,80]
list2.sort()
print(list2)

# q5 concatenate and sort two sorted arrays
list2=[5,25,6,49,66,80]
list3=[2,23,35,68,62,50]
list2.sort()
list3.sort()
print("sorted list 1 is :",list2)
print("sorted list 2 is :",list3)
list2.extend(list3)
print("after concatenate: ",list2)
list2.sort()
print("final list is :",list2)

# q6 count even and odd number in a list
count1=0
count2=0
for i in list2:
    if(i%2==0):
        count2+=1
    else:
        count1+=1
print("odd numbers are:",count1)
print("even numbers are:",count2)

# q7 print a tuple in reverse
list4=[]
b=int(input("enter numbers ofvariables"))
print("enter elements")
for i in range(b):
    b1=int(input())
    list4.append(b1)
tup=tuple(list4)
print("tuple is :",tup)
rev=reversed(tup)
print("reversed tuple is: ",tuple(rev))

# q8 find largest and smallest elements of tuple
list5=[]
c=int(input("enter number of variables"))
print("enter elements")
for i in range(c):
    c1=int(input())
    list5.append(c1)
tupp=tuple(list5)
print(max(tupp),min(tupp))

# q9 convert a string to upper case
str=input("enter a string \n")
print(str.upper())

# q10 check if string contain all numeric characters
str1=input("enter a string\n")
c=0
for i in range(len(str1)):
    if str1.isdigit():
        c=1
    else:
        c=0
        break
if (c==1):
    print("true")
else:
    print("false")

# q11 replace givenn string with your name
str2='hello friends'
print(str2.replace("hello friends","prateek"))
