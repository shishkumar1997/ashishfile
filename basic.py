# d={'name':'ajay','age':24}
# for key in d:
#     value = d[key]
#     print('1',key, value)


# for key in d.keys():
#     value = d[key]
#     print('2',key, value)

# for key, value in d.items():
#     print('3',key, value)

# for value in d.values():
#     print('4',value)

# for key in d:
#     value = d[key]
#     print('5',key, value)


# for key in d.keys():
#     value = d[key]
#     print('6',key, value)


# for key in d.iterkeys():
#     value = d[key]
#     print('7',key, value)


# for key, value in d.items():
#     print('8',key, value)


# for key, value in d.iteritems():
#     print('9',key, value)


# for value in d.values():
#     print('10',value)

# for value in d.itervalues():
#     print('11',value)





# dict1={"a":"c","d":"k"}

# # print(dict.get["l"])
# print(dict1.get('c'))
# print(dict1.get('k'))
# print(dict1.get('z'))
# print(dict1.get("d"))


# a=10
# b=10
# c=10
# d=10
# print(a)
# print(b)
# print(c)
# print(d)

# a=b=c=d=10
# print(a)
# print(b)
# print(c)
# print(d)

# a='ram'
# b=18
# c="ajay"
# print(a)
# print(b)
# print(c)
# d={'a':'ram','b':18,'c':'ajay'}
# print(d['a'])
# # print(d.get['a'])
# print(d.get('z'))

# a=2         
# b=10             #bitwise operator
# print(a & b)
# print(a | b)
# print(a ^ b)
# print(~a)

# a=99          #identity operator is,is not
# b=99
# print(a is b)
# print(a is not b)

# r="my name is ashish"       #Membership operator
# print("n" in r)
# print(" " in r)
# print("ashish" in r)
# print('rando' in r)
# print("n" not in r)
# print(" " not in r)

# a=4             #implicits
# b='ram'
# c=3.5
# print(a+c)
# d=int(c)
# w=complex(c)
# # print(a/b)
# print(a+d)
# print(c)
# print(w)
# B=bin(a)
# print(B)
# h=hex(a)
# print(h)
# p=oct(h)
# # print(p)
# m='ajay'
# n='ashish'
# t=10
# s=str(10)
# # k=m+n        #can catination
# # print(k)
# print(m+s)

# l=['ram',3,5,'ajay']
# t=tuple(l)
# print(t)
# # d=dict(l)
# # print(d)

# n={3:'ram','name':34}
# l=list(n)
# t=tuple(n)
# print(n)
# print(l)
# print(t)

# print('#')			# Draw pattern

# n=int(input('enter the no:'))
# for i in range(n):
# 	# print('#',end=',')
# 	# print('#',end=' ')
# 	print('#',sep=':')
# n=int(input('enter the no:'))
# for i in range(n):
# 	for k in range(i):
# 	# for k in range(i+1):
# 	# for k in range(i+3):
# 		print('#',end=' ')
# 	print()

# n=int(input('enter the no:'))
# for i in range(n):
# 	# for k in range(i+4):
# 	for k in range(n-i):
# 		print("@",end=":")
# 	print()

# n=int(input('enter the no:'))
# for i in range(n):
# 	for j in range(i):
# 		print(" ",end=":")
# 	print()
# for m in range(n):
# 	for n in range(n-m):
# 		print("#",end=" ")
# 	print()

# s='ram and shyam'
# l=list(s)
# print(l)
# d=tuple(l)
# print(d)
# t=dict(l)
# print(t) #create error
# # print(t.get(l))

# a=10
# print('given value in a:',a)             #output statements in print() fuction
# b="durga classess"
# sohan='best city'
# print('values:',a,'string_value==>',b,'how is your cit:',sohan,sep=' ')
# print('values:',a,'string_value==>',b,'how is your cit:',sohan,end='\t')

# mb=input()                #input statements input() function

# mb=input()
# print(mb)

# mb=input('your mobile number:')
# print('my mobile no:',mb)
# print(type(mb))

# mb=int(input('your mobile number:'))
# print('my mobile no:',mb)
# print(type(mb))

# print('''bed person'ram is "very" good person'and you''') #Escape sequence in python
# print('sanjay\n' "ram")

#                             #if statements
# if 4>2:
# 	print('ajay')
# print('rest of the code')


# 							 #if else statements
# n=int(input("enter the numbers:"))							 
# if n>2:
# 	print('ajay')
# 	# if 10>20:
# 	if 10<n:
# 		print('you access')
# 	else:
# 		print('not access')
# print('rest of the code')


#tarnary operation
# print('access value') if 5>2 else print('not access')
# print('access value') if 5<2 else print('not access')

# n=int(input("enter the number:"))
# r=range(n)
# for i in r:			#for loop
# 	print('#')
# 	for j in range(n-i):
# 		print('#',end=' ')
# 	print()
# print('ram')


# a=int(input("enter the number:"))	#while loop
# # a=2										
# while a<22:							
# 	print(a)
# 	a+=2
# print('rest of code')

# while 5>2:
# 	print('outer loop')
# 	while 10<3:
# 		print('inner loop')
# 	else:
# 		print('else part')
# print('rest of code')

# n=int(input("enter the number:")) #range & for loop
# t=range(n)
# print(n)
# print(t)
# for i in t:
# 	print(i)

# s='ashish sir'
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])

# s='ashish sir'
# n=len(s)
# for aj in range(n):
# 	print(aj,"=",s[aj])
# print('rest of the code')


# s='ashish sir'
# n=len(s)
# print(n)


# for aj in range(2):
# 	# print('outer loop')
# 	for i in range(3):
# 		print('inner loop')
# 	print('outer loop')
# print('rest of code')

# for u in range(10):	#break statements
# 	print(u)
# print('rest of the code')

# for u in range(10):
# 	# print(u)	
# 	if u==4:
# 		break
# 	print(u)	
# print('rest of the code')


# for u in range(10):	#continue
# 	# print(u)	#in this case working continue statements
# 	if u==4:
# 		continue
# 	print(u)	
# print('rest of the code')

# if 5<7:		#pass statements
# # if 5<2:
# 	pass
# else:
# 	print('else part')
# print('rest of the code')

# for i in range(20):
# 	# print(i)
# 	pass
# 	if i==10:
# 		# pass
# 		print(i)
# print('rest of the code')

# 101,102,103,104,105
# Stu_rollno1=101	#array
# Stu_rollno2=102
# Stu_rollno3=103
# Stu_rollno4=104
# Stu_rollno5=105
# Stu_rollno6=106

# print(Stu_rollno1)
# print(Stu_rollno2)
# print(Stu_rollno3)
# print(Stu_rollno4)
# print(Stu_rollno5)
# print(Stu_rollno6)

# 101,102,103,104,105
# Stu_rollno=('j',[101,102,103,104,105])
# for element in Stu_rollno:
# 	print(element)


# import array		#1st methon initialized one_D arry
# stu_roll=array.array('i',[101,102,103,104,105])
# print(stu_roll[0])
# print(stu_roll[1])
# print(stu_roll[2])
# print(stu_roll[3])
# print(stu_roll[4])


# from array import*		#2nd methon initialized one_D arry
# stu_roll=array('i',[101,102,103,104,105])
# print(stu_roll[0])
# print(stu_roll[1])
# print(stu_roll[2])
# print(stu_roll[3])
# print(stu_roll[4])

# from array import*		#empity methon initialized one_D arry
# stu_roll=array('i',[])

# from array import*		#using for loop without index methon initialized one_D arry
# stu_roll=array('i',[101,102,103,104,105])  # pk=element use optional
# for pk in stu_roll:
# 	print(pk)

# from array import*		#using for loop with index methon initialized one_D arry
# stu_roll=array('i',[101,102,103,104,105])
# p=len(stu_roll)
# for i in range(p):
# 	print(stu_roll[i])
# print('rest of code')

# print('dubalikes values')  #find  dubalicate values
# stu=array('i',[2,3,4,6,7,43,2])
# p=len(stu)
# for r in range(p):
# 	for t in range(r+1,p):
# 		if stu[r]==stu[t] :
# 			print(stu[t])


# a = [1, 2, 3, 4, 2, 7, 8, 8, 3]  #find dubalicates values in list  
# for i in range(len(a)):    
#     for j in range(i+1, len(a)):    
#         if a[i] == a[j]:    
#             print(a[j]) 
# print("Duplicate elements")   

# 	# print("try agin")
# # if count>2:
# 	# print(stu[t])
# print('rest of the code')




# from array import*		
# stu_roll=array('i',[101,102,103,104,105])
# p=len(stu_roll)
# for i in range(p):
# 	# print('index no:',i,"and",'students roll no:',stu_roll[i])
# 	print('index no:',i,"=",'students roll no:',stu_roll[i])
# print('rest of code')

# from array import*	#using for loop with index methon initialized one_D arry	
# stu_roll=array('i',[101,102,103,104,105])
# p=len(stu_roll)
# print(p)
# i=0
# # while 0<p:
# while i<p:
# 	print('index no:',i,"and",'students roll no:',stu_roll[i])
# 	i=i+1
# print('rest of the code')

# from array import*		#using append() method
# stu_roll=array('i',[101,102,103,104,105])
# # p=len(stu_roll)
# stu_roll.append(100)
# print(stu_roll)

# from array import*	#using for loop with index and append() method methon initialized one_D arry	
# stu_roll=array('i',[101,102,103,104,105])
# p=len(stu_roll)
# print(p)
# i=0
# # while 0<p:
# while i<p:
# 	print('index no:',i,"and",'students roll no:',stu_roll[i])
# 	i=i+1
# print(stu_roll)
# print('append after than array')
# stu_roll.append(201)
# stu_roll.append(202)
# stu_roll.append(104)
# # i=0
# # while i<p:
# # 	print(i,"=",stu_roll[i])
# # 	i+=1
# print(stu_roll)

# from array import*
# coll_roll=array('i',[])
# n=int(input("how many enter numbers:"))
# for el  in range(n):
# 	print(coll_roll.append(int(input("enter elements:"))))
# print(coll_roll,'$$$$$$$$$$$$$$$')
# # for i in range(len(coll_roll)):  #show elements in array  
# # 	print(coll_roll[i])
# # print('rest of the code')
# # print(coll_roll)
# # print(len(coll_roll))

# # import math                  #mathematicall use tool before import 
# from math import pi,sqrt 
# print(pi)
# print(sqrt(81))

# from array import*
# a=array('i',[111,112,113,114])
# # for elements in a:
# # 	print(elements)
# p=len(a)
# # for c in range(p):
# # 	print(a[c])
# c=0
# for c in range(p):
# 	print(a[c])
# print(a)
# print(len(a))
# a.append(222)
# a.append(333)
# a.append(444)
# print('append use afer than array')
# print(a)
# print(len(a))
# from array import*
# stu_marks=array('f',[])
# p=int(input(" how many enter element:"))
# for f in range(p):
# 	print(stu_marks.append(int(input('enter elements:'))))
# print(stu_marks)
# for c in range(len(stu_marks)):
# 	print(stu_marks[c])

# from array import*		#using insert() method in array
# a=array('i',[111,112,113,114])
# print(a)
# print('insert after than')
# a.insert(4,2222)
# print(a)

# from array import*		#using pop() method in array
# a=array('i',[111,112,113,114])
# print(a)
# print('insert after than')
# # a.pop()
# a.pop(2)
# print(a)

# from array import*		#using remove() method in array
# a=array('i',[111,112,113,114])
# print(a)
# print('insert after than')
# a.remove(113)
# print(a)

# 						#using remove() and pop() method in list
# a=[111,112,113,114]
# print(a)
# print('insert after than')
# a.remove(113)
# a.pop()
# a.pop(1)
# print(a)


# from array import*		#using index() method in array
# a=array('i',[111,112,113,114])
# print(a)
# print('insert after than')
# print(a.index(113))

# from array import*		#using reverse() method in array
# a=array('i',[111,112,113,114])
# print(a)
# print('insert after than')
# a.reverse()
# print(a)

# from array import*		#using reverse() method in array
# a=array('i',[111,112,113,114])
# print(a)
# print('insert after than')
# a.reverse()
# print(a)


# from array import*		#using extend() method in array
# a=array('i',[111,112,113,114])
# arr=array('i',[1,2,3,4,5])
# print(a)
# print(arr)
# print('extend  after than array')
# a.extend(arr)
# print(a)


# from array import*		#using slicing in array
# a=array('i',[111,112,113,114,1,3,4,5,67,5])
# print(a)
# print('slicing  after than array')
# new_array=a[1:8]
# print(new_array)



# from array import*		#using slicing,for loop in array
# a=array('i',[111,112,113,114,1,3,4,5,67,5])
# for c in range(len(a)):
# 	print(a[c])
# 	c+=1
# print('slicing  after than array')
# new_array=a[1:8]
# for d in range(len(new_array)):
# 	print(new_array[d])

# import numpy					#using numpy
# stu_roll=numpy.array([1,2,3,4,5])
# print(stu_roll)
# print(stu_roll.dtype)


# import numpy					#using numpy array display in for loop
# stu_roll=numpy.array([1,2,3,4,5])
# p=len(stu_roll)
# for c in range(p):
# 	print(stu_roll[c])
# print(stu_roll)
# print(stu_roll.dtype)


# import numpy					#using numpy array display in while loop
# stu_roll=numpy.array([1,2,3,4,5])
# p=len(stu_roll)
# c=0
# while c<p:
# 	print(stu_roll[c])
# 	c=c+1
# print(stu_roll)
# print(stu_roll.dtype)


# import numpy					#using numpy array display in while loop change value
# # stu_roll=numpy.array(['ram','sohan','raja','neha','rupa'])
# stu_roll=numpy.array([1.1,1.2])
# p=len(stu_roll)
# c=0
# while c<p:
# 	print(stu_roll[c])
# 	c=c+1
# print(stu_roll)
# print(stu_roll.dtype)
# print('change the elements in array')
# print(stu_roll[0])
# stu_roll[0]=2.99
# print(stu_roll)

# from numpy import*	#linspace() function using one_D array
# # a=linspace(1,10)
# a=linspace(1,10,4)
# print(a)
# a=linspace(1,10,4,endpoint=False)
# print(a)
# a=linspace(1,10,4,endpoint=True)
# print(a)

# from numpy import*	#linspace() function using one_D array with for loop
# a=linspace(1,10,2)
# c=0
# while c<len(a):
# 	print(a[c])
# 	c+=1
# # for c in range(len(a)):
# # 	print(a[c])
# print(a)

# from numpy import*
# s=array([2,3,4],[1,4,3,2],[1,2,3,4])
# for i in range(len(s)):
# 	for j in range(len(s)):
# 		print(s[i][j])
# 	print()

# print(s)

# import numpy as nmp
# from numpy import array	#multiple array
# X = array( [ [ 1, 6, 7], [ 5, 9, 2] ,[4,3,2,1]] )
# print(X)
# print(X.dtype)
# print(type(X))

# from numpy import*   		#compare operator
# a=array([1,4,2,5,5,6])
# b=array([2,4,5,5,6,1])
# result=a==b
# result= a>b
# result= a<b
# print(result)

# import sys 
# from sys import argv
# for i in argv:
# 	print(i)
# print(len(argv))

# for i in range(10):
# 	# print(i)
# 	if i==5:
# 		# break
# 		continue
# 	print(i)
# print('rest of the code')

# s=[12,34,45,65,324,45]
# for item in s:
# 	# print('enter item',item)
# 	if 100<item:
# 		# break
# 		continue
# 	print('enter item',item)
# print('rest of the code')

# s=[12,34,45,65,324,45]
# for item in s:
# 	# print('enter item',item)
# 	if 100<item:
# 		pass
# 	# print('enter item',item)
# print('rest of the code')


# if 4>2:
# 	print('outer loop')
# 	if 20>6:
# 		pass
# 		print('inner loop')
# 		# pass	
# 	print('else part')
# print('rest of the code')

# for i in range(100):
# 	if i%2==0:
# 		print(i)
# 	else:
# 		pass
# print('rest of the code')


# for i in range(100):
# 	if i%2==0:
# 		pass
# 	else:
# 		print(i)
# print('rest of the code')

# x=10
# print(x)
# del x
# print(x)

#STRING DATA TYPE IN SEQUENCE 

# from typing import Type


# S="I AM A TEACHER"
# print(S)
# print(Type(S))
# a="ram"
# print(type(a))
# for c in range(len(S)):
# 	print(c)
# 	print(S[c])
# 	print('index number:',c,"and",'string of values:',S[c])
# print('rest of the code')
# t='AM'
# print(t in S)
# print(t not in S)
# p=S.replace()
# print(p)

# s='aaaaabbbbb'
# print(s)
# print(s.replace('a','b'))


# f = open("students.txt","w")
# print(f.write())


# import os
# f_name, f_ext = os.path.splitext('doc.txt')
# print(f_name)
# print(file_object.name)



# f = open("students.txt","w")      # file handling
# f.write('hello how are you\n')
# f.write('I am very happy to be here to meet all of  you')


# f=open("students.txt",mode='r')
# data=f.read()
# print(data)
# # f.close()
# # print(f)
# # f.write('suman')

# f=open('school.txt',mode='x',encoding='utf-8')
# print(f.name)


# f=open("students.txt",mode='br')
# data=f.read()
# print(data)
# f.close()

# f=open('students.txt',mode='r',encoding='utf-8')
# print(f.name)
# print(f.mode)
# print(f.close())
# print(f.closed)
# # print(f.readable)
# # print(f.writable)
# print(f.readable())
# print(f.writable())
# print(f.encoding)

# f=open('students.txt',mode='r',encoding='utf-8')
# print('file name',f.name)
# print('file mode',f.mode)
# print('file close',f.closed)
# # print('file close',f.close())
# print('file close',f.closed)
# # print('file redable',f.readable)
# # print('file writable',f.writable)
# print('file readable',f.readable())
# print('file writable',f.writable())
# print('file encoding',f.encoding)

# f=open('students.txt',mode='w',encoding='utf-8')
# print('file name',f.name)
# print('file mode',f.mode)
# print('file close',f.closed)
# # print('file close',f.close())
# print('file close',f.closed)
# # print('file redable',f.readable)
# # print('file writable',f.writable)
# print('file readable',f.readable())
# print('file writable',f.writable())
# print('file encoding',f.encoding)

# f=open('students.txt',mode='x',encoding='utf-8')
# print('file name',f.name)
# print('file mode',f.mode)
# print('file close',f.closed)
# # print('file close',f.close())
# print('file close',f.closed)
# # print('file redable',f.readable)
# # print('file writable',f.writable)
# print('file readable',f.readable())
# print('file writable',f.writable())
# print('file encoding',f.encoding)

# f=open('students.txt',mode='r+',encoding='utf-8')
# print('file name',f.name)
# print('file mode',f.mode)
# print('file close',f.closed)
# # print('file close',f.close())
# print('file close',f.closed)
# # print('file redable',f.readable)
# # print('file writable',f.writable)
# print('file readable',f.readable())
# print('file writable',f.writable())
# print('file encoding',f.encoding)

# f=open('students.txt',mode='a',encoding='utf-8')
# print('file name',f.name)
# print('file mode',f.mode)
# print('file close',f.closed)
# # print('file close',f.close())
# print('file close',f.closed)
# # print('file redable',f.readable)
# # print('file writable',f.writable)
# print('file readable',f.readable())
# print('file writable',f.writable())
# print('file encoding',f.encoding)

# f=open('students.txt',mode='a+',encoding='utf-8')
# print('file name',f.name)
# print('file mode',f.mode)
# print('file close',f.closed)
# # print('file close',f.close())
# print('file close',f.closed)
# # print('file redable',f.readable)
# # print('file writable',f.writable)
# print('file readable',f.readable())
# print('file writable',f.writable())
# print('file encoding',f.encoding)

# f=open('G:\All_project IMPORTANT\advance Python\students.txt',mode='r',encoding='utf-8')
# print(f.name)
# print(f.mode)
# print(f.close())
# # print(f.readable)
# # print(f.writable)
# print(f.readable())
# print(f.writable())
# print(f.encoding)

# f=open('students.txt',mode='rb')
# print('file name',f.name)
# print('file mode',f.mode)
# print('file close',f.closed)
# # print('file close',f.close())
# print('file close',f.closed)
# # print('file redable',f.readable)
# # print('file writable',f.writable)
# print('file readable',f.readable())
# print('file writable',f.writable())
# # print('file encoding',f.encoding)


# f=open('JPG File (.JPG)',mode='rb')
# print('file name',f.name)
# print('file mode',f.mode)
# print('file close',f.closed)
# # print('file close',f.close())
# print('file close',f.closed)
# # print('file redable',f.readable)
# # print('file writable',f.writable)
# print('file readable',f.readable())
# print('file writable',f.writable())
# # print('file encoding',f.encoding)


# f=open('students.txt',mode='w',encoding='utf-8')
# print(f.write('how are you'))
# # print(f.read())
# for i in f:
# 	print(i)
# print('ater than')
# print (f)

# f=open('ram.txt')
# print(f)

# import os				#check file is not
# print(os.path.isfile('students.txt'))
# f=os.path.isfile('students.txt')
# print(f)

# f=open('students.txt','w')
# f.write('sony')
# # print(f.name)
# # print(f)
# f.close()
# # print(f.name)
# print(f.read)

# f=os.path.isfile('ramu.txt')
# # f=os.path.isfile('Employee.txt')
# print(f)
# # print(f.name) #get error
# filename=input(enter filename:

# if os.path.isfile(input("enter filename:")):
# 	print('open file')


# if os.path.isfile(input("enter filename:")):
# 	# open(input("enter filename:"))
# 	print('open file')
# else:
# 	print('this file name is not avalaible')


# f=open('school1.txt','w')	#create broblem over write line
# # f.write('my name')
# f.write("[2,2,3,],(3,4,5)")
# # p=f.write('hello ashish')  #list in this case not allow
# lst=["ram\n",'sohan\n','raja']
# f.write(lst)
# # print(p)
# # print(f)
# f.close()

# f=open('employee.txt','a')
# lst=["ram\n",'sohan\n','raja','kunal\n','tata\n','room']
# f.writelines(lst)
# # f.writeline(lst)	#get error
# f.close()
# print('suceess')

# f=open('employee.txt','r')		#real data 
# # data1=f.read(3)
# # data2=f.read(5)
# # print(data1)
# # print(data2)
# data=f.readline()
# print(data)
# # data3=f.readlines()
# # print(data3)
# f.close()
# print('suceess')

# f=open('school.txt','r')	# use  tell() & seek()	
# print(f.tell())
# data=f.read(5)
# print(data)
# print(f.read(4))
# print(f.tell())
# f.close()


# f=open('school.txt','r+')	# use  r+,tell() & seek()	
# print(f.tell())
# f.write('youtube')
# data=f.read()
# print(data)
# print(f.tell())
# print(f.seek(5))
# print(f.tell())
# print(f.read())
# print(f.tell())
# f.close()

# f=open('school.txt','w+')	# use   w+ ,tell() & seek()	
# print(f.tell())
# # data=f.read()
# # print(data)
# f.write('youtube')
# # data=f.read()
# # print(data)
# print(f.tell())
# print(f.seek(5))
# print(f.tell())
# # print(f.read())
# print(f.tell())
# print(f.seek(0))
# data=f.read()
# print(data)
# f.close()

# f=open('school.txt','a+')	# use  a+ ,tell() & seek()	
# print(f.tell())
# f.write('GOLDEN')
# # data=f.read()
# # print(data)
# print(f.tell())
# print(f.seek(5))
# print(f.tell())
# # print(f.read())
# print(f.tell())
# print(f.seek(0))
# data=f.read()
# print(data)
# f.close()

# f1=open('school.txt','r')	#one file to another file convert data
# f2=open('employee.txt','w')
# f2.write('query code')
# data=f1.read()
# print(data)
# # data1=f2.read()
# # print(data1)
# f2.writelines(data)
# # data1=f2.read()
# # print(data1)
# f2.close()
# # f1.close()

# import io			#pickle and unpickle(Serializer & Deserializer)
# import pickle
# class Students:
# 	print('##1')
# 	def __init__(self,name,rollno,address):
# 		print('##2')
# 		self.name=name
# 		self.rollno=rollno
# 		self.address=address
# 	def display_data(self):
# 		print('##3')
# 		print(f'Name:{self.name} Rollno:{self.rollno} Address:{self.address}')

# with open('Student.dat',mode='wb') as f:
# 	print('$$$1')
# 	stu1=Students("ajay",101,"Noida")
# 	print('$$2')
# 	pickle.dump(stu1,f)
# 	print('$$3')
# 	print("pickle success")
# with open('Student.dat',mode='rb') as f:
# 	obj=pickle.load(f)
# 	print('unpickle done')
# 	obj.display_data()


# f=os.path.isfile('this PC/desktop/documents.txt')
# print(f)
# f=open('desktop/documents.txt',mode='r',encoding='utf-8')
# print(f.read())

# f=open('desktop/school.txt',mode='w',encoding='utf-8')
# f.write('hi ashish')
# f.close()


# print(os.path.isfile('school.txt'))
# print(f.tell())

# print(os.path.isfile('desktop/documents.txt'))

# f=open('ram.txt',mode='w+',encoding='utf-8')
# f.write('hi\n')
# f.write('my name is ashish\n')
# f.seek(0)
# print([f.read()])
# # print(f.tell())
# f.close()

# f=open('Employee.txt',mode='w',encoding='utf-8')
# f.write('ajay singh\n')
# f.write('ashish kumar\n')
# f.write('amar singh\n')
# f.write('prince singh')
# f.close()
# f=open('Employee.txt',mode='r',encoding='utf-8')
# print(f.read())
# # print(f.read.get(0))


# f = open("shop.txt", "r")
# content_list = f. readlines()
# print(content_list)
# for i in range(len(content_list)):
# 	# f.seek(0)
# 	print([content_list[i]])

# f = open("copy.txt", "r")
# content_list = f. readlines()
# print(content_list)
# for i in range(len(content_list)):
# 	print(['content_list[i]\n'])


# f = open("shop.txt", "r+")
# content_list = f. readlines()
# print(content_list)
# # for i in range(len(content_list)):
# # 	# f.seek(0)
# # 	print([content_list[i]])

# f=open("school.txt",'w+')
# f.write('how are you\n')
# f.write('ram is\n')
# f.write('very good')
# f.seek(0)
# print(f.read())
# f.seek(0)
# content_list=f.readlines()
# print(content_list)
# for i in range(len(content_list)):
# 	print(content_list[i])
# f.seek(0)
# print(f.truncate([2]))
# # print(content_list.get(f.read()))
# f.close()

# 3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333

# Reading an excel file using Python
# import xlrd
 
# # Give the location of the file
# loc = ("path of file")
 
# # To open Workbook
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
 
# # For row 0 and column 0
# print(sheet.cell_value(0, 0))

# f=open('ashish.txt',mode='w+')
# f.write('hi guru\n' )
# f.write('you are good person\n')
# f.write('but i am very good')
# print(f.tell())
# f.seek(0)
# print(f.tell())
# print(f.read())
# f.close()

#4444444444444444444444444444444444444444444444444444444444444444444444444444444444444

# a=int(input("enter one no:"))
# b=int(input("enter one no:"))
# c=int(input("enter one no:"))

# s=(a+b+c)*0.5
# print(s)
# A=s*(s-a)*(s-b)*(s-c)**0.5
# print("area of traingle:",A)


# def fact(name):
# 	name=input("enter name:")
# 	print("hi sir",name)
# fact("t")

# def fact(name,age=10):
# 	# name=input("enter name:")
# 	print("hi sir",name,"and my",age)
# fact("name=t","age=12")

# def sum(a,b=2):
# 	c=a+b
# 	# return c  #not show value in console
# 	print(c)	#show value in console
# a=int(input("enter a value:"))
# b=int(input("enter b value:"))
# print(a+b)
# sum(1)

# def sum(a,b):
# 	c=a+b
# 	# return c  #not show value in console
# 	print(c)	#show value in console
# 	a=int(input("enter a value:"))
# 	b=int(input("enter b value:"))
# 	print(a+b)
# sum(9,6)

# def li(list1):	#change list
# 	list1.append(2)
# 	list1.append(4)
# 	print("inner list",list1)

# list1=[20,30,45]
# li(list1)
# print('outer list:',list1)
# li(list1)




# def str(string1):
# 	string1=string1 + "you are boss"
# 	print("new inner string:",string1)

# string1="my name is ashish"

# str(string1)
# print("old sring outer:",string1)
# # str(string1)

# n=int(input("enter the number:")) 	#positive,negative and zero elements
# if 0<n:
# 	print('this element is positive no')
# elif 0>n:
# 	print('this element is negative')
# elif n==0:
# 	print('this element is zero')
# else:
# 	print('code is succuss')

# a=10	#swap two 
# b=20
# a,b=b,a
# print(a)
# print(b)


# n=int(input("enter tne number:")) #patters print() and using for loop
# for i in range(n):
# 	for j in range(n):
# 		print('*',end=" ")
# 	print()
# print("rest of code")

# n=int(input("enter tne number:"))
# for i in range(n):
# 	# print(i,"111")
# 	for j in range(i):
# 		# print(j,"222")
# 		print('*',end=" ")
# 	print()
# print("rest of code")


# n=int(input("enter tne number:"))
# for i in range(n):
# 	# print(i,"111")
# 	for j in range(i):
# 		# print(j,"222")
# 		print(j,end=" ")
# 	print()
# print("rest of code")


# n=int(input("enter tne number:"))
# for i in range(n):
# 	# print(i,"111")
# 	for j in range(n-i):
# 		# print(j,"222")
# 		print('*',end=" ")
# 	print()
# print("rest of code")

# n=int(input("enter tne number:"))
# for i in range(n):
# 	# print(i,"111")
# 	for j in range(n-i):
# 		# print(j,"222")
# 		print(j,end=" ")
# 	print()
# print("rest of code")

# n=int(input("enter tne number:"))
# for i in range(n):
# 	# print(i,"111")
# 	for j in range(n-i):
# 		# print(j,"222")
# 		print(i,end=" ")
# 	print()
# print("rest of code")

# n=int(input("enter tne number:"))
# for i in range(n):
# 	# print(i,"111")
# 	for j in range(n-i):
# 		# print(j,"222")
# 		print(i+1,end=" ")
# 	print()
# print("rest of code")

# n=int(input("enter tne number:"))
# for i in range(n):
# 	# print(i,"111")
# 	for j in range(i+1):
# 		# print(j,"222")
# 		print(j,end=" ")
# 	print()
# print("rest of code")

# n=int(input("enter tne number:")) #error
# for i in range(n):
# 	print(i,"111")
# 	for j in range(n-i):
# 		# print(j,"222")
# 		print(' ',end=" ")
# 	print()
# 	for i in range(n):
# 		for j in range(i):
# 			print("*",end=" ")
# 		print()

# n=int(input("enter tne number:"))
# for i in range(n):
# 	# print(i,"111")
# 	for j in range(i):
# 		# print(j,"222")
# 		print('#',end=" ")
# 	print()
# for i in range(n):
# 	for j in range(i):
# 		print("*",end=" ")
# 	print()

# n = int(input("Enter the number of rows: "))
# m = (2 * n) - 2.
# for i in range(0, n):
# 	for j in range(0, m):
# 		print(end=" ")
# # m = m - 1 
# for j in range(0, i + 1):


# str="";    
# for Row in range(0,7):    
#     for Col in range(0,7):     
#         if (Col == 1 or Col == 5 or (Row == Col and Col != 0 and Col != 6)):  
#             str=str+"*"    
#         else:      
#             str=str+" "    
#     str=str+"\n"    
# print(str); 



#1111111111111111111111111111111111111111111111111111111111111111111111  pattern

# n=int(input("enter the no of rows:"))
# for i in range(n):
# 	for j in range(i+1):
# 		print(i+1,end=" ")
# 	print()

# n=int(input("enter the no of rows:"))
# for i in range(n):
# 	for j in range(i+1):
# 		print(j+1,end=" ")
# 	print()
 
# n=int(input("enter the no of rows:"))
# for i in range(n):
# 	for j in range(n-i):
# 		print(n-j,end="")
# 	print()

 
# n=int(input("enter the no of rows:"))
# for i in range(n):
# 	for j in range(n-i):
# 		print(n-i,end="")
# 	print()

 
# n=int(input("enter the no of rows:"))
# for i in range(n):
# 	for j in range(n-1-i):
# 		print('&',end="")
# 	for j in range(i+1):
# 		print(j+1,end="")
# 	print()

# n=int(input("enter the no of rows:"))
# for i in range(n):
# 	for j in range(n-1-i):
# 		print(' ',end="[]")
# 	for j in range(i+1):
# 		print('*',end="[]")
# 	print()


# n=int(input("enter the no of rows:"))
# for i in range(n):
# 	for j in range(n-1-i):
# 		print(' ',end=" ")
# 	for j in range(i+1):
# 		print('*',end=" ")
# 	print()


# n=int(input("enter the no of rows:"))
# for i in range(n):
# 	for j in range(n-1-i):
# 		print(' ',end=" ")
# 	for j in range(i+1):
# 		print(j,end=" ")
# 	print()


# n=int(input("enter the no of rows:"))
# for i in range(n):
# 	for j in range(n-1-i):
# 		print(' ',end=" ")
# 	for j in range(i+1):
# 		print(j+1,end=" ")
# 	print()


# n=int(input("enter the no of rows:")) #maza aa gya 
# for i in range(n):
# 	for j in range(n-1-i):
# 		print(' ',end=" ")
# 	for j in range(i+1):
# 		print(i+1-j,end=" ")
# 	print()


# n=int(input("enter the no of rows:"))
# for i in range(n):
# 	for k in range(n-1-i):
# 		print(' ',end=" ")
# 	for j in range(i+1):
# 		print('*',end=" ")
# 	print()


# n=int(input("enter the no of rows:"))
# for i in range(n):
# 	for k in range(n-1-i):
# 		print(k,end=" ")
# 	for j in range(i+1):
# 		print('*',end=" ")
# 	print()


# n=int(input("enter the no of rows:"))
# for i in range(n):

# 	for j in range(i+1):
# 		print(i+1-j,end=" ")
# 	print()

# n=int(input("enter the no of rows:"))     #alphabates capitals
# for i in range(n):
# 	for j in range(i):
# 		print(chr(65+j),end=' ')
# 	print()

# n=int(input("enter the no of rows:"))     # alphabets smaller
# for i in range(n):
# 	for j in range(i):
# 		print(chr(97+j),end=' ')
# 	print()


# n=int(input('enter the no:'))
# for i in range(6):
# 	for j in range(i):
# 		print(n-i+1-4*j,end=' ')
# 	print()


# n=int(input('enter the no:'))
# for i in range(6):
# 	for j in range(i):
# 		print(n-i+1-4*j,end=' ')
# 	print()

# n=int(input('enter the no:'))
# for i in range(n):
# 	for j in range(n-i-1):
# 		print(' ',end=' ')
# 	for k in range(i+1):
# 		print('*',end=' ')
# 	print()
#pattern ##################################################################################################
					#String

# os="how are you.I am fine but you"
# s=input('enter string:')         #sub string
# print(os.find('you'))					#find()
# print(os.count('you'))				#count()
# print(os.rfind('you'))
# print(os.rfind('u'))
# print(os.rfind('ashish'))
# print(os.find('ashish'))
# print(os.find('you',2,11))
# print(os.find('you',2,10))
# print(os.index('i'))					#index()
# print(os.index('h'))		
# print(os.index('how'))		
# print(os.index(s))
# print(os.replace('fine','so'))		#replace()	
# print(os.replace('fine','you'))
# print(id(os))							#id()
# print(id(s))
# print(os.split())						#split()			
# print(os.split(' '))							
# print(os.split(','))							
# print(os.split(':'))							
# print(os.split('#'))

# s='I am an engineer'						
# for i in s:
# 	print(i)


# s='I am an engineer'
# s='22 01 2022'
# p=s.split()					
# for i in p:
# 	print(i)

# s='22-01-2022'
# s='ajay,ashish,ram'
# p=s.split(',')	
# print(p)				
# for i in p:
# 	print(i)

# s=('ajay','ashish','sandeep','mantu')  	#joining of strings
# p='-'.join(s)
# p='@'.join(s)
# p=':'.join(s)
# print(p)

# name='jay'									#format()
# age=23
# salary=34567
# print('{} is good person,your age is {}and salary is {}'.format(name,age,salary))
# print('{2} is good person,your age is {1}and salary is {0}'.format(name,age,salary))
# print('{x} is good person,your age is {y}and salary is {z}'.format(x=name,y=age,z=salary))

# s="you are very danger person" 				#reverse  1st method
# print(s[::-1])


# s="you are very danger person" 				#reverse  2nd method
# print(''.join(reversed(s)))



# s="you are very danger person" 				#reverse  3rd method
# i=len(s)-1
# os=''
# while i>=0:
# 	os=os+s[i]
# 	i=i-1
# print(os)



# s="you are very danger person" 				#while loop
# ns=[]
# p=s.split()
# i=len(p)-1
# while i>=0:
# 	ns.append(p[i])
# 	i=i-1
# output=''.join(p)
# print(output)

# s="you are very danger person" 				#for loop
# ns=[]
# p=s.split()
# for i in range(len(p)):
# 	ns.append(p[i])
# 	print(p[i])
# print(ns)

# s=input('enter string:')						#even and odd no print by slicing
# print('olny even string of value:',s[0::2])
# print('olny odd string of value:',s[1::2])

# s=input('enter string:')						#even and odd no print without slicing
# i=0
# print('even value of string:')
# while i<len(s):
# 	print(s[i],end=' ')
# 	i=i+2
# print('odd value of string:')
# i=1
# while i<len(s):
# 	print(s[i],end=' ')
# 	i=i+2

# os=input('enter the old string:')
# ns=''
# for i in os:
# 	if i.isupper()==True:
# 		print('22')
# 		ns=ns+i.lower()
		
# 	elif i.islower()==True:
# 		print('33')
# 		ns=ns+i.upper()
		
# 	elif i.isspace()==True:
# 		print('44')
# 		ns=ns+i
# print(os)
# print('get new string:',ns)

# os=input('enter the old string:')
# ns=''
# count1=0
# count2=0
# count3=0
# for i in os:
# 	if i.isupper()==True:
# 		count1+=1
# 		ns=ns+i.lower()
		
# 	elif i.islower()==True:
# 		count2+=1
# 		ns=ns+i.upper()
		
# 	elif i.isspace()==True:
# 		count3+=1
# 		ns=ns+i
# print(os)
# print('get new string:',ns)
# print('upper case:',count1)
# print('lower case:',count2)
# print('space case:',count3)

# s="Pmy name is ASHISH KUMAR and i am basically from BIHAR" #find upper,lower and space count no
# # s=input("enter string:") 			#given input string 
# s1=""
# # cout1=0
# # cout2=0
# # cout3=0
# for i in s:
#     if i.isupper() == True:
#         # cout1=cout1 + 1
#         s1=s1+i.upper()
#     elif i.islower() == True:
#         # cout2=cout2 + 1
#         s1=s1+i.upper()
#     elif i.isspace() == True:
#         # cout3=cout3 + 1
#         s1=s1+i
# print('old string',s)
# # print('upper case strings:',cout1)
# # print('lower case strings:',cout2)
# # print('space case strings:',cout3)
# print('changing after than new string:',s1)

# s="you are very good"
# print(s)
# print(len(s))



##############################################################################################################
#					list

# s=[1,3,4,5,5,6332,334,2,2,2,33,3] #append(),Extend() and new_list create
# # s=[1,1,2,3,4,4]
# # new_string=''
# count=0
# new_list=[]
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         if s[i] == s[j]:
#             count=count+1
#             new_list.append(s[j])
#             print('3333',s[j])
# print('dubalicate count',count)
# print('new list:',new_list)
# print('old list:',s)
# s.extend(new_list)
# print('Extented list:',s)

# old_string=input("enter the string:")
# count=0
# new_string=''
# for p in old_string:
#     if (p.isupper())==True:
#         count+=1
#         print(p)
#         new_string+=p.lower()
#     elif (p.islower()) == True:
#         new_string+=p.upper()
#     elif (p.isspace()) == True:
#         new_string+=p
# print("all upper case alphabate no:",count)
# print('new_string is:',new_string)

# list=[2,34,56,7,8,9]
# # print(max(list))

# s=[12,13,14,116,43]   #11111111111111111111111 same_code 
# for i in s:
#     print(i)

# s=[12,13,14,116,43]   #11111111111111111111111 same_code
# # print(range(len(s)))
# for i in range(len(s)):
#     print(s[i])

# s=[12,13,14,116,43]         #first and second max elements
# print('first max elements:',max(s))
# s.remove(max(s))
# print(s)
# print('second max elements:',max(s))

# def f1():			#function base programming
# 	print("hello")
# f1()
# print(f1())

# def sum(n):
# 	if n%2==0:
# 		print("even number")
# 	else:
# 	    print("odd number")
# # sum(3)
# sum(10)

# def sum(a,b):
# 	return a+b
# result=sum(2,45)
# print(sum(10,20))
# print(result)
# print("the sum:",sum(40,50))

# def fact(n):
# 	coun=1
# 	while coun>=1:
# 		coun=coun*n
# 		n=n-1
# 	return coun
# for i in range(1,5):
# 	print("the factorial of",i,"is:",fact(i))

# def fact(a,b):
# 	sum=a+b
# 	sub=a-b
# 	mult=a*b
# 	return sum,sub,mult
# print(fact(20,40))
# result=fact(90,30)
# print(result)

# def sum():
# 	print("hi")
# # sum()
# print(sum())
# class Sum:
# 	c1="ashish"
# 	c2=20
# 	def __init__(self):
# 		self.name
# 		self.age
# 	def fact(self,username,your_age):
# 		self.name=username
# 		self.age=your_age
# 		print("name:",self.name)
# p=sum
# # p.fact(username="ram",your_name=26)
# print(p.c1)

# dict={'a':1,'b':2,'c':3}	#dict,list and for loop
# set_dict={}
# l=[]
# s=""
# for i in dict:
# 	print(dict.get('a'))
# 	print(dict.get('p'))
# l.append(input("enter string:"))
# s.append(input('enter string:'))
# print('list:',s)
# set_dict['name']="ajay"
# set_dict['roll']=234
# set_dict['city']='noida'
# set_dict['name']=dict['a']
# print('new dictionary:',set_dict)
# print('rest of code')
# print('old dictionary:',dict)
# print("extend dict",set_dict)
# print('extand after than:',dict)
# print(l)
# s1=s.replace('a','b')
# print('replace after than:',s1)

# s="aaabbb"
# s1=s.replace('a','b')
# print(s)
# print(s1)

# s='hi hello'
# s=input('enter string:')
# s="ra is hello and hello hi ,you are hi"
# s1=s.replace('hi','hello')
# print(s1)

# s={1,3,4,53,2,1,2,4,3,22}
# print(s)
# print(len(s))
# # for i in range(len(s)):
# 	# print('index no',i,'and',max(s))
# print('first max value',max(s))
# s.remove(max(s))
# print(s)

# s1={1,3,4,53,2,1,2,4,3,22}
# s2={2,3,4,5,5,66,7}
# print(s1)
# print(s2)
# print(s1^s2)
# print(s1&s2)
# print(s1-s2)

# n=int(input('enter the no:'))
# s={}
# for i in range(n):
# 	s.append(2)
# print(s)

# from  numpy import*
# a=array([10,20,30,40,50]) #all() & any()
# print(a,id(a))
# b=a
# print(b,id(b))
# b[0]=1
# print(a,id(a))
# print(b,id(b))
# result= a==b
# print(all(result))
# print(any(result))

# a=array([10,20,30,40,50]) 
# b=array([10,20,30,40,50])
# print('a array',a,id(a)) 
# # result=a.view()
# result=a.copy()
# print('a with use view',result,id(result))
# result[1]=100
# print(result,id(result))
# print('view after than a array',a,id(a))
# # b.view()
# b.copy()
# b[1]=100
# print(b,id(b))

# a=array([1,2,3,4,5])
# b=a
# b.copy()
# print(a,id(a))
# print(b,id(b))
# c=b.copy()
# print(c,id(c))
# b[1]=1111
# print(a,id(a))
# print(b,id(b))



#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
#						datetime duration



# from datetime import time
# # print(datetime.now)
# print(time.now)

# from datetime import date

# today = date.today()

# # dd/mm/YY
# d1 = today.strftime("%d/%m/%Y")
# print("d1 =", d1)

# # Textual month, day and year	
# d2 = today.strftime("%B %d, %Y")
# print("d2 =", d2)

# from datetime import datetime
# # datetime object containing current date and time
# now = datetime.now()
# print("now =", now)
# dt_string = now.strftime("%d/ %H:%M:%S")
# print("date and time =", dt_string)

# import datetime
# from datetime import datetime
# a = datetime.timedelta(hours=36)
# b = datetime.timedelta(hours=4, minutes=46, seconds=23)
# c = a - b
# print(c)
# print(a)
# print(b)
# now=datetime.timedelta
# print('now',now)
# print(n1=datetime.timedelta(hour=3))

 
# from datetime import datetime, timedelta  
# n=int((input('enter no of hour:')))
# if n==24:
# 	present_time = datetime.now()  
# 	updated_time = datetime.now() + timedelta(hours=n)
# 	print('24 hour after than:',updated_time,'HELLO')
# elif n==168:
# 	present_time = datetime.now()  
# 	updated_time = datetime.now() + timedelta(hours=n)
# 	print('7 days after than:',updated_time,'Hi')
# else:
# 	print('plz enter given condition(24 and 168)')

# from datetime import datetime, timedelta   #first project   ****************
# n=int((input('enter no of days:')))
# if n==1:
# 	present_time = datetime.now()  
# 	updated_time = datetime.now() + timedelta(days=n)
# 	print('24 hour after than:',updated_time,'HELLO')
# elif n==7:
# 	present_time = datetime.now()  
# 	updated_time = datetime.now() + timedelta(days=n)
# 	print('7 days after than:',updated_time,'Hi')
# else:
# 	print('plz enter given condition out of range')

# from datetime import datetime, timedelta  
# n=int((input('enter no of hour:')))
# # p=int((input('Employees are update at many time:')))
# p=16
# for i in range(1,p):
# 	present_time = datetime.now()  
# 	updated_time = datetime.now() + timedelta(hours=i+1)
# 	print('you can update',updated_time)
# else:
# 	print('In this time only manager is update')
	

	

# from datetime import datetime, timedelta  
# n=int((input('enter no of hour:')))
# p=int((input('Employees are update at many time:')))
# while n>0:
# 	if p<21:
# 		present_time = datetime.now()  
# 	updated_time = datetime.now() + timedelta(hours=p)
# 	print('you can update',updated_time)	
# 	p=p+1
# else:
# 	print('In this time only manager is update')
	

# from datetime import datetime, timedelta   #second project     *******************
# p=int(input('how many hours do you want to work with Employee:'))
# n=int((input('enter no of hours:')))
# for i in range(n):
# 	if p>i:
# 		present_time = datetime.now()  
# 		updated_time = datetime.now() + timedelta(hours=i)
# 		print('you can update',updated_time)
# 	else:
# 		present_time = datetime.now()  
# 		updated_time = datetime.now() + timedelta(hours=i)
# 		print('In this time only manager is update',updated_time)


# from datetime import datetime, timedelta   #second project
# p=10
# for j in range(1,25):
# 	n=int((input('enter no of hours:')))
# 	for i in range(n):
# 		if p>i:
# 			present_time = datetime.now()  
# 			updated_time = datetime.now() + timedelta(hours=i)
# 			print('you can update',updated_time)
# 		else:
# 			present_time = datetime.now()  
# 			updated_time = datetime.now() + timedelta(hours=i)
# 			print('In this time only manager is update',updated_time)


# import datetime
# # yesterday = datetime.date.today () - datetime.timedelta (days=2)
# # t = datetime.time(hour=16, minute=00)
# # print(t)
# # print(datetime.datetime.combine(yesterday, t))
# t = datetime.time(hour=16, minute=00)
# for i in range():
# 	print(t)
# t=datetime.datetime.today()
# print(t)


# import datetime                   #present & yesterday date time
# n=int(input('enter many times:'))
# yesterday = datetime.date.today () - datetime.timedelta (days=1)
# t = datetime.time(hour=16, minute=00)
# p=datetime.datetime.combine(yesterday, t)
# print('yesterday time:',p,'pm')

# today= datetime.date.today () + datetime.timedelta (hours=13)
# c = datetime.time(hour=1, minute=00)
# k=datetime.datetime.combine(today, c)
# print('today end time for update:',k,'pm')



# from datetime import datetime, timedelta   #second project
# import datetime                  			 #present & yesterday date time
# # n=int(input('enter many times:'))
# yesterday = datetime.date.today () - datetime.timedelta (days=1)
# t = datetime.time(hour=16, minute=00)
# p=datetime.datetime.combine(yesterday, t)
# print('yesterday time:',p,'pm')

# from datetime import datetime,timedelta
# import datetime
# today= datetime.date.today () + datetime.timedelta (hours=13)
# print('today',today)
# today= datetime.date.today ()
# print('today111',today)
# c = datetime.time(hour=1, minute=00)
# k=datetime.datetime.combine(today, c)
# print('today end time for update:',k,'pm')
# n=int((input('enter no of hours:')))
# n=updated_time = datetime.datetime.now() + datetime.timedelta(hours=13)
# print(n)
# for i in range(n):
# 	if p<n and n<k:
# 		print('you can update')
# 	else:
# 		print('In this time only manager is update')


# import datetime
# today= datetime.date.Today ()
# print(today)
# c = datetime.time(hour=1, minute=00)
# print(c)
# k=datetime.datetime.combine(today, c)
# # print(k)

# import datetime
# today= datetime.date.today () + datetime.timedelta (hours=13)
# c=datetime.time(hour=1,minute=00)
# x=datetime.datetime.combine(today,c)
# print(x,'pm')
# yesterday=datetime.date.today () - datetime.timedelta (days=1)
# t=datetime.time(hour=1,minute=00)
# y=datetime.datetime.combine(yesterday,t)
# print(y,'pm')
# for i in range(1,5):
# 	# if x==
# # 	print('update')

# # import datetime
# # day_delta = datetime.timedelta(days=1)
# # start_date = datetime.date.today()
# # end_date = start_date + 7*day_delta
# # for i in range((end_date - start_date).days):
# #     print(start_date + i*day_delta)

# from datetime import datetime, timedelta   #second project     *******************
# p=int(input('how many hours do you want to work with Employee:'))
# n=int((input('enter no of hours:')))
# for i in range(n):
# 	if p>i:
# 		present_time = datetime.now()  
# 		updated_time = datetime.now() + timedelta(hours=i)
# 		print('you can update',updated_time)
# 	else:
# 		present_time = datetime.now()  
# 		updated_time = datetime.now() + timedelta(hours=i)
# 		print('In this time only manager is update',updated_time)

# from datetime import datetime,timedelta
# # start_time = datetime.now()  
# # end_time = datetime.now() + timedelta(days=1) + timedelta(hours=13)
# for i in range(n):
# 	if i<24:
# 		end_time = datetime.now() + timedelta(hours=i)
# 		print(end_time,'hello')
# 	elif i>24:
# 		end_time = datetime.now() + timedelta(days=1) + timedelta(hours=i)
# 		print(end_time,'hello')
# 	elif i==37:
# 		end_time = datetime.now() + timedelta(days=1) + timedelta(hours=i)
# 		print(end_time,'hello')
# 	elif i>37:
# 		end_time = datetime.now() + timedelta(days=1) + timedelta(hours=i)
# 		print(end_time,'hi')
# 	else:
# 		print(end_time,'out of range')


# from datetime import datetime,timedelta
# n=int(input('enter hours:'))
# start_time = datetime.now()  
# # end_time = datetime.now() + timedelta(days=1) + timedelta(hours=13)
# for i in range(n):
# 	if i<24:
# 		end_time = datetime.now() + timedelta(hours=i)
# 		print(end_time,'hello')
# 	elif i>24:
# 		end_time = datetime.now() + timedelta(days=1) + timedelta(hours=i)
# 		print(end_time,'hello')
# 	else:
# 		end_time = datetime.now() + timedelta(days=1) + timedelta(hours=i)
# 		print(end_time,'Hi')

# 	elif i==37:
# 		print('###')
# 		end_time = datetime.now() + timedelta(days=2) + timedelta(hours=i)
# 		print(end_time,'hello')
# 	elif i>37:
# 		print('@@@@')
# 		end_time = datetime.now() + timedelta(days=2) + timedelta(hours=i)
# 		print(end_time,'hi')
# print('rest')


# import datetime
# n=int(input('enter hours:'))
# for i in range(n):
# 	old_time=datetime.datetime(2021, 12, 14 ,i+1, 0)
# 	t_obj=old_time.time()
# 	print(old_time,'Hello')
# 	print(t_obj)
# 	if t_obj==24:
# 		old_time=t_obj + datetime.timedelta(days=1)	
# else:
# 	print("hi")

	# if i>23:
	# 	old_time=datetime.datetime(2021, 12, 14 ,i+1, 0) + datetime.timedelta(hours=i)
	# 	print('hi')
# # else:
# 	print()
# for i in range(n):
# 	after_one_day=datetime.datetime(2021,12,15,i+1,0)
# 	print(after_one_day)



# import datetime  									#third programming
# p_date=datetime.datetime(2021,12,14,1,00)
# print(p_date)
# q=p_date.date()+ datetime.timedelta(days=2)
# print(q,'###')
# c=datetime.time(hour=0,minute=00)
# k_obj=datetime.datetime.combine(q,c)
# print(k_obj)
# l_time=k_obj + datetime.timedelta(hours=9)+datetime.timedelta(days=1)
# print(l_time)


# k_date=p_date + datetime.timedelta(days=2) + datetime.timedelta(hours=36)
# print(k_date,'##')

# c_date=p_date + datetime.timedelta(days=2)
# print(c_date)
# c_obj=c_date.time()
# print(c_obj)

# w=datetime.datetime(int(c_obj))
# print(w,'@@@')
# latest_time=c_date + datetime.timedelta(hours=9)
# print(latest_time,'***')


# import datetime
# n=int(input('enter hours:'))
# 
# for i in range(n):
# 	
# 	# l_time=old_time + datetime.timedelta(hours=9)+datetime.timedelta(days=1)
# 	# print(l_time)
# 	print(old_time,'Hello')
# else:
# 	print("hi")


# import datetime
# start_date = datetime. date(2020, 1, 1)
# end_date = datetime. date(2020, 1, 4)
# delta = datetime. timedelta(days=1)
# while start_date <= end_date:
# 	print(start_date)
# start_date += delta



# from datetime import date, timedelta
# def daterange(start_date, end_date):
#     for n in range(int((end_date - start_date).days)):
#         yield start_date + timedelta(n)
# start_date = date(2013, 1, 1)
# end_date = date(2015, 6, 2)
# for single_date in daterange(start_date, end_date):
#     print(single_date.strftime("%Y-%m-%d"))

# import datetime
# yesterday=datetime.datetime(2021,12,13,1,0)
# m_datetime=yesterday + datetime.timedelta(days=1)
# print(m_datetime)
# last_datetime=m_datetime + datetime.timedelta(hours=13)
# print(last_datetime)
# if yesterday:
# 	print('yesterday',yesterday,'Hello')
# elif m_datetime:
# 	print('m_datetime',m_datetime,'Hello')
# elif last_datetime:
# 	print('m_datetime',last_datetime,'Hello')
# else:
# 	print('Hi')


# import datetime
# yesterday=datetime.datetime(2021,12,13,1,0)
# m_datetime=yesterday + datetime.timedelta(days=1)
# print(m_datetime)
# last_datetime=m_datetime + datetime.timedelta(hours=13)
# print(last_datetime)
# if yesterday and m_datetime and last_datetime:
# 	print('hello')
# else:
# 	print('Hi')

#111111111111111111111111111111111111111111111111111
# import datetime
# n=int(input('enter hours:'))
# for i in range(n):
# 	old_time=datetime.datetime(2021, 12, 14 ,i+1, 0)
# 	t_obj=old_time.time()
# 	print(old_time,'Hello')
# 	print(t_obj)
# 	if t_obj==24:
# 		old_time=t_obj + datetime.timedelta(days=1)	
# else:
# 	print("hi")



# from datetime import datetime,timedelta
# import datetime
# n=int(input('enter hours:'))
# start_time = datetime.datetime(2021,12,14,10,0)  
# for i in range(n):
# 		if i<27:
# 			end_time = start_time + timedelta(hours=i)
# 			print(end_time,'hello')
# 		else:
# 			end_time = start_time + timedelta(hours=i)
# 			print(end_time,'hi')

	# 	end_time = datetime.now() + timedelta(days=1) + timedelta(hours=i)
	# 	print(end_time,'hello')
	# else:
	# 	end_time = datetime.now() + timedelta(days=1) + timedelta(hours=i)
	# 	print(end_time,'Hi')
		
# 	elif i==37:
# 		print('###')
# 		end_time = datetime.now() + timedelta(days=2) + timedelta(hours=i)
# 		print(end_time,'hello')
# 	elif i>37:
# 		print('@@@@')
# 		end_time = datetime.now() + timedelta(days=2) + timedelta(hours=i)
# 		print(end_time,'hi')
# print('rest')

# from datetime import datetime,timedelta


# import datetime
# n=int(input('enter hours:'))

# start_time = datetime.datetime(2021,12,14,10,0)  
# # end_time = datetime.now() + timedelta(days=1) + timedelta(hours=13)
# for i in range(n):
# 	if i<24:
# 		if i<21:
# 			end_time = datetime.now() + timedelta(hours=i)
# 			print(end_time,'hello')
# 		else:
# 			end_time = datetime.now() + timedelta(hours=i)
# 			print(end_time,'hi')



# from datetime import datetime,timedelta		#forth programming
# import datetime
# n=int(input('enter hours:'))
# hours=24
# start_time = datetime.datetime(2021,12,14,10,0)  
# for i in range(n):
# 	if i < hours+3:
# 		end_time = start_time + timedelta(hours=i)
# 		print(end_time,'hello','you are updated')
# 	else:
# 		end_time = start_time + timedelta(hours=i)
# 		print(end_time,'hi')



#88888888888888888888888888888888888888888888888888888888888888888888888888888888

# n=int(input("enter the years:")) #leap year
# if n%4 == 0 and n%100 != 0:
# 	print('year',n,'is leap year')
# elif n%400==0:
# 	print('year',n,'is leap year')
# else:
# 	print('year',n,'is not leap year')


# n=int(input("enter the years:"))			#leap year
# if n%4 == 0 and n%100 != 0 or n%400 == 0:
# 	print('year',n,'is leap year')
# else:
# 	print('year',n,'is not leap year')



# a=int(input("enter the first element:"))	#add two number
# b=int(input("enter the second element:"))
# sum= a + b
# print('Add elements are',sum)


# a=int(input("enter the  element:"))	#square and squre_root
# square=a*a
# print('squre is',square)
# sqr=a**0.5
# print('square_root',sqr)

# a=int(input("enter the  element:")) #factorial
# sum=1
# for i in range(a):
# 	sum=sum*(a-i)
# print(sum)



# a=int(input("enter the a element:")) #find HCF values
# b=int(input("enter the b element:"))
# l=[]
# c=b if a>b else a 
# for i in range(2,c):
# 	if a%i==0 and b%i==0:
# 		l.append(i)	
# print('HCF of',a,'and',b,'equal',max(l))


# a=int(input("enter the a element:")) 		#find LCM values
# b=int(input("enter the b element:"))
# l=[]
# l1=[]
# l2=[]
# c=b if a>b else a 
# for i in range(1,c+1):
# 		l.append(a*i)	
# 		l1.append(b*i)
# for j in range(len(l)):
# 	for k in range(len(l)):
# 		if l[j]==l1[k]:
# 			l2.append(l[j])
# 		else:
# 			k=a*b
# if l2:
# 	print('LCM of',a,'and',b,'equal',max(l2))
# else:
# 	print('LCM of',a,'and',b,'equal',k)


# a=int(input("enter the a element:")) 			#prime no 
# flag=0
# for i in range(2,a):
# 	if a%i==0:
# 		print(a)
# 		flag=1
# 		print(flag)
# 		break
# if flag==0:
# 	print(a,'is prime no')
# else:	
# 	print(a,'is not prime no')


# a=[1,2,3,4]
# b=[1,3,5,6]
# for i in range(len(a)):
# 	for j in range(len(b)):
# 		if a[i]==b[j]:
# 			print(a[i])


# n=int(input('enter the no:'))  #armstrong number find
# sum=0
# temp=n
# while temp>0:
# 	digit=temp%10
# 	sum=sum+digit**3
# 	temp=temp//10
# print(sum)
# print(n)
# if sum==n:
# 	print('armstrong')
# else:
# 	print('not armstrong')



# n=int(input('enter the no:'))  #polidram no
# sum=0
# temp=n
# while n>0:
# 	digit = n%10
# 	sum = sum*10 + digit
# 	n = n//10
# print(temp,sum,n)
# if temp == sum:
# 	print('polidram no')
# else:
# 	print('not polidram no')


 
# import datetime
# day_delta = datetime.timedelta(days=1)
# start_date = datetime.date.today()
# end_date = start_date + 7*day_delta
# for i in range((end_date - start_date).days):
#     print(start_date + i*day_delta)

# a=int(input('enter the 1st no:'))
# b=int(input('enter the 2nd no:'))
# c=int(input('enter the 3rd no:'))
# square=(a+b)**2
# qube=(a+b+c)**2
# if square:
# 	print('a and b is square:',square)
# elif qube:
# 	print('a and b is square:',qube)
# else:
# 	print('plz select a and b')

# n=int(input('enter the no:'))     #fibonacci sequence
# n1=0
# n2=1
# if n <= 0:
# 	print('invalide',)
# elif n < 1:
# 	print(n2)
# else:
# 	for i in range(0,n):
# 		print(n1)
# 		c=n1+n2
# 		n2=n1
# 		n1=c

# nterms = int(input("How many terms? "))  #fibonacci sequence
# n1, n2 = 0, 1
# count = 0
# if nterms <0:
#    print("Please enter a positive integer")
# elif nterms == 0:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n2)
# else:
#    print("Fibonacci sequence:")
#    for i in range(1,nterms+1):
#        print(n1)
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count += 1

# n=eval(input('enter the no:'))
# print(n)						#math all expresion solve,type tuple

# n=eval(input('enter the no:'))
# l=[]
# l.append(n)
# print(l)						#math all expresion solve,list value get

# n=int(input('enter the no:'))
# l=[]
# for i in range(n):
# 	for j in range(n):
# 		print(i,end='')
# 	print()				

# from numpy import array
# a=array([2,3,4,5])
# l=[]
# for element in range(len(a)):
# 	l.append(a[element])
# 	print(a[element])
# print(l)


# from numpy import*
# a=array([2,3,4,5,23,44,5,6,7,7,8,8,9,9,90,0,])
# l=[]
# for element in range(len(a)):
# 	l.append(a[element])
# 	print(a[element])
# print(l)


# from numpy import*
# a=array([2,3,4,5])
# l=[]
# for element in range(len(a)):
# 	l.append(a[element])
# 	print(a[element])
# print(l)


# import numpy                 #add two matrix
# a=numpy.array([[1,2],[2,3]])
# b=numpy.array([[3,2],[6,3]])
# print('first matrix:',a)
# print('second matrix:',b)
# c=a+b
# print('add of two matrix:',c)

# import numpy as ashish               #add two matrix
# a=ashish.array([[1,2],[2,3]])
# b=ashish.array([[3,2],[6,3]])
# print('first matrix:',a)
# print('second matrix:',b)
# c=a+b
# print('add of two matrix:',c)





# #2222222222222222222222222222222222222222222222222222222222222222222222222@  Exel editor
# import pandas as pd  
# dict1 = {"number of storage arrays":20, "number of ports":2390}
# df = pd.DataFrame(data=dict1, index=[0])
# df = (df.T)
# print (df)
# df.to_excel('dict1.xlsx')

# import pandas as pd
# title = ['name', 'age', 'Saturation', 'Value',
#          'Lightness', 'AComponent', 'BComponent',
#          'Blue Channel', 'Green Channel', 'Red Channel']
# df = pd.DataFrame(columns = title)
# pd.read_excel('pythona.xlsx')


# dict1 = {"name":"ajay", "age":24,"city":"Noida"}
# df = pd.DataFrame(data=dict1, index=[0])
# df = (df.T)
# print (df)
# df.to_excel('dict1.xlsx')

# import xlsxwriter
# import searchbox
# import re
# try:
# 	searchbox_result = re.match("^.*(?=(\())", searchbox).group()
# 	workbook = xlsxwriter.Workbook('traizine.xlsx')
# 	worksheet = workbook.add_worksheet()
# 	worksheet.write('name', 'Hello..')
# 	worksheet.write('age', 'Geeks')
# 	worksheet.write('C1', 'For')
# 	worksheet.write('D1', 'Geeks')
# 	workbook.close()
# except AttributeError:
#     searchbox_result = re.match("^.*(?=(\())", searchbox)



# f=open("students.txt",mode='w+')
# data=f.read()
# print(data)
# # f.close()
# # print(f)
# f.write('name')



# import xlsxwriter
# workbook = xlsxwriter.Workbook('hello.xlsx')
# worksheet = workbook.add_worksheet()
# worksheet.write('A1', 'ajay')
# worksheet.write('B1', 'ashish')
# worksheet.write('C1', 'ram')
# worksheet.write('D1', 'jitendra')
# workbook.close()


# import xlsxwriter
# workbook = xlsxwriter.Workbook('Example2.xlsx')
# worksheet = workbook.add_worksheet()
# row = 0
# column = 0
# content = ["ajay", "rahul", "ashish", "harshita",
#                     "sumit", "neeraj", "shivam"]
# for item in content :
#     worksheet.write(row, column, item)
#     row += 1
# workbook.close()


# import xlsxwriter
# workbook = xlsxwriter.Workbook('Example4.xlsx')
# worksheet = workbook.add_worksheet()
# scores = (['ajay', 1000],['ashish',   100],['ram',  300],['harshita',    50],)
# row = 0
# col = 0
# for name, score in (scores):
# 	worksheet.write(row, col, name)
# 	worksheet.write(row, col, score)
# 	row += 1
# workbook.close()

# import xlsxwriter
# workbook = xlsxwriter.Workbook('Example5.xlsx')
# worksheet = workbook.add_worksheet()
# scores = (['ajay', 1000],['ashish',   100],['ram',  300],['harshita',    50],)
# row = 0
# col = 0
# for name, score in (scores):
# 	worksheet.write(row, col, name)
# 	row += 1
# workbook.close()

# import xlsxwriter
# workbook = xlsxwriter.Workbook('Example6.xlsx')		#error
# worksheet = workbook.add_worksheet()
# scores = [{'ajay': 1000},{'ashish' : 100},{'ram': 300},{'harshita' : 50}]
# row = 0
# col = 0
# for name,score in scores:
# 	worksheet.write(row, col, name)
# 	worksheet.write(row, col + 1, score)
# 	row += 1
# workbook.close()


# d ={"name:":"ajay singh"}        # d.items() in get key and value
# for key, value in d.items():
    # print(key,value)

# d ={"name:":"ajay singh","age":24}
# for key,value in d.items():   
#     print('keys:',key,'values:',value)
# 	# print('values:',value)
# print(d.get('f'))


# for key, value in d.iteritems():
    # print(key, value)



# import xlsxwriter
# workbook = xlsxwriter.Workbook('Example7.xlsx')
# worksheet = workbook.add_worksheet()
# scores = (['ajay', 1000],['ashish',   100],['ram',  300],['harshita',    50],)
# row = 0
# col = 0
# for name, score in (scores):
# 	worksheet.write(row, col, name)
# 	worksheet.write(row, col, score)
# 	row += 1


# import xlsxwriter
# workbook = xlsxwriter.Workbook('ajay.xlsx')
# worksheet = workbook.add_worksheet()
# scores = (['ajay', 1000],['ashish',   100],['ram',  300],['harshita',    50],)
# row = 0
# col = 0
# for name, p in (scores):
# 	worksheet.write(row, col, name)
# 	worksheet.write(row, col, p)
# 	row += 1
# workbook.close()


# import xlsxwriter
# workbook = xlsxwriter.Workbook('ajay1.xlsx')
# worksheet = workbook.add_worksheet()
# scores = (['ajay', 1000],['ashish',   100],['ram',  300],['harshita', 50],)
# row = 0
# col = 0
# for t, p in (scores):
# 	worksheet.write(row, col, p)
# 	worksheet.write(row, col+1, t)
# 	row += 1
# workbook.close()



# import xlsxwriter
# workbook = xlsxwriter.Workbook('ajay1.xlsx')
# worksheet = workbook.add_worksheet()
# scores = (['ajay', 1000],['ashish',   100],['ram',  300],['harshita', 50],)
# row = 0
# col = 0
# for t, p in (scores):
# 	worksheet.write(row, col, p)
# 	worksheet.write(row, col+1, t)
# 	row += 1
# workbook.close()

# import xlsxwriter                                   #json data which database list and dict 2data
# workbook = xlsxwriter.Workbook('computer24.xlsx')
# worksheet = workbook.add_worksheet('sheet of ashish')
# l=[{"name":"ajay","age":23,"city":"Noida"},{"name":"ashish","age":24,"city":"delhi"}]
# for i in range(len(l)):
# 	print(l[i])
# 	if i==0:
# 		col=0
# 		row=0
# 		for key,value in l[i].items():	
# 			worksheet.write(row,col,key)
# 			worksheet.write(row+1,col,value)
# 			col+=1
# 	if i==1:
# 		col=0
# 		row=2
# 		for key,value in l[i].items():	
# 			worksheet.write(row,col,value)
# 			col+=1
# workbook.close()

# import xlsxwriter                                   #json data which database list and dict 3data
# workbook = xlsxwriter.Workbook('computer25.xlsx')
# worksheet = workbook.add_worksheet('sheet of ashish')
# l=[{"name":"ajay","age":23,"city":"Noida"},{"name":"ashish","age":24,"city":"delhi"},{"name":"ruby","age":21,"city":"lamichaur"}]
# for i in range(len(l)):
# 	if i==0:
# 		col=0
# 		row=0
# 		for key,value in l[i].items():	
# 			worksheet.write(row,col,key)
# 			worksheet.write(row+1,col,value)
# 			col+=1
# 	if i==1:
# 		col=0
# 		row=2
# 		for key,value in l[i].items():	
# 			worksheet.write(row,col,value)
# 			col+=1
# 	if i==2:
# 		col=0
# 		row=3
# 		for key,value in l[i].items():	
# 			worksheet.write(row,col,value)
# 			col+=1
# workbook.close()


# import xlsxwriter                                   #json data which database list and dict 3data
# workbook = xlsxwriter.Workbook('computer27.xlsx')
# worksheet = workbook.add_worksheet('sheet of ashish')
# l=[{"name":"ajay","age":23,"city":"Noida"},{"name":"ashish","age":24,"city":"delhi"},{"name":"ruby","age":21,"city":"lamichaur"}]
# for i in range(len(l)):
# 	if i==0:
# 		col=0
# 		row=0
# 		for key,value in l[i].items():	
# 			worksheet.write(row,col,key)
# 			worksheet.write(row+1,col,value)
# 			col+=1
# 	if i==1:
# 		col=0
# 		row=2
# 		for key,value in l[i].items():	
# 			worksheet.write(row,col,value)
# 			col+=1
# 	if i==2:
# 		col=0
# 		row=3
# 		for key,value in l[i].items():	
# 			worksheet.write(row,col,value)
# 			col+=1
# workbook.close()

# import xlsxwriter                                   #direct json data to save all data in exel file
# workbook = xlsxwriter.Workbook('computer29.xlsx')
# worksheet = workbook.add_worksheet('sheet of ashish')
# l=[{"name":"ajay","age":23,"city":"Noida"},{"name":"ashish","age":24,"city":"delhi"},{"name":"ruby","age":21,"city":"lamichaur"},{"name":"KARAN","age":25,"city":"bhore"},{"name":"chunmun","age":21,"city":"bihar"}]
# for i in range(len(l)):
# 	col=0
# 	row=0
# 	for key,value in l[i].items():	
# 		worksheet.write(row,col,key)
# 		worksheet.write(row+i,col,value)
# 		col+=1
# workbook.close()



# import xlsxwriter                                   #project json data
# workbook = xlsxwriter.Workbook('computer28.xlsx')
# worksheet = workbook.add_worksheet('sheet of ashish')
# l=[
#     {
#         "brand_category": "apple",
#         "town_id": "noida",
#         "created_on": "2021-12-27T13:05:18.371962"
#     },
#     {
#         "brand_category": "cig",
#         "town_id": "delhi",
#         "created_on": "2021-12-27T13:06:14.654002"
#     },
#     {
#         "brand_category": "lpg",
#         "town_id": "lamichaur",
#         "created_on": "2021-12-27T13:07:09.946492"
#     }
# ]
# for i in range(len(l)):
# 	if i==0:
# 		col=0
# 		row=0
# 		for key,value in l[i].items():	
# 			worksheet.write(row,col,key)
# 			worksheet.write(row+1,col,value)
# 			col+=1
# 	if i==1:
# 		col=0
# 		row=2
# 		for key,value in l[i].items():	
# 			worksheet.write(row,col,value)
# 			col+=1
# 	if i==2:
# 		col=0
# 		row=3
# 		for key,value in l[i].items():	
# 			worksheet.write(row,col,value)
# 			col+=1
# workbook.close()



# l=[{"name":"ajay","age":23,"city":"Noida"},{"name":"ashish","age":24,"city":"delhi"}]
# l
# for i in range(len(l)):
# 	print(l[i])
# print(l[0].name)


# import xlsxwriter
# workbook = xlsxwriter.Workbook('computer.xlsx')
# worksheet = workbook.add_worksheet('sheet of ashish')
# l=[{"name":"ajay","age":24,"city":"Noida"},{"name":"puja","age":24,"city":"Gopalganj"}]
# print(len(l))
# for i in range(len(l)):
# 	print(l[i])
# print('external',l[i])
# # print(l[0])
# d={"name":"ajay","age":24,"city":"Noida"}
# col=0
# row=0
# for key,value in l[0].items():
# 	print(row,col,key)
# 	print(row+1,col+1,value)
# 	col+=1
# workbook.close()

# import pandas as pd
# raw_data = {'first_name': ['Sam','Ziva','Kia','Robin'], 
#         'degree': ['PhD','MBA','','MS'],
#         'age': [25, 29, 19, 21]}
# df = pd.DataFrame(raw_data)
# df
# df.to_excel(r'ashish.xlsx')

# import pandas as pd					#dict and list of data show exel file
# data = {'name': ['ajay','ashish','Robin'], 'city': ['Noida','Deoria','chandigarth'],'age': [25, 24, 19]}
# df = pd.DataFrame(data)
# print(df)
# df.to_excel(r'ashish2.xlsx')

# import pandas as pd					#dict and list of data show exel file
# data = {'name': ['ajay','ashish','Robin','sonia','sunita ','suman','puja','muskan','ram','sandeep'],
#  'city': ['Noida','Deoria','chandigarth','Noida','Deoria','chandigarth','Noida','Deoria','chandigarth','semrauna'],
#  'age': [25, 24, 19,25, 24, 19,25, 24, 19,35]}
# df = pd.DataFrame(data)
# print(df)
# df.to_excel(r'ashish3.xlsx')



# import xlsxwriter
# workbook = xlsxwriter.Workbook('ajay3.xlsx')
# worksheet = workbook.add_worksheet()
# scores = ({'name':'ajay'},)
# row = 0
# col = 0
# for t, p in (scores):
# 	c=worksheet.write(row, col, t)
# 	d=worksheet.write(row, col+1,p)
# 	row += 1
# print(c,d)

# import xlsxwriter
# workbook = xlsxwriter.Workbook('myexel.xlsx')
# worksheet = workbook.add_worksheet('mysheet')
# worksheet.write('A1', 'name')
# worksheet.write('B1', 'age')
# worksheet.write('C1', 'city')
# worksheet.write('D1', 'salary')
# # workbook.close()

# import xlrd
# d = {}
# wb = xlrd.open_workbook('pythona.xlsl')
# sh = wb.sheet_by_index(2)   
# for i in range(138):
#     cell_value_class = sh.cell(i,2).value
#     cell_value_id = sh.cell(i,0).value
#     d[cell_value_class] = cell_value_id


# import os
# print(os.path.isfile('ajay.xlsx'))

# import xlsxwriter
# import xlrd
# wb = xlrd.open_workbook('G:/All_project IMPORTANT/advance Python/basic/Example4.xlsx','rb')
# sh = wb.sheet_by_index(2)   
# for i in range(138):
#     cell_value_class = sh.cell(i,2).value
#     cell_value_id = sh.cell(i,0).value



# import datetime
# day_delta = datetime.timedelta(days=1)
# start_date = datetime.date.today()
# end_date = start_date + 7*day_delta
# for i in range((end_date - start_date).days):
#     print(start_date + i*day_delta)


# import datetime            # 1 to 9 days in list
# from datetime import date
# n=int(input('enter days:'))
# list=[]
# for i in range(n):
# 	if i<9:
# 		date=datetime.datetime(2021, 12, 1+i )
# 		t_obj=date.date()
# 		print(t_obj)
# 		list.append(date.date())
# 	else:
# 		pass
# print(list)

# a=[12,122,1234,3454,999999999999999999999999999999999999999999999999999999999999999999999999999999999999999]
# print(a)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! list
# list=[4,6,3,45,67,0]
# n1=list[0]
# n2=list[5]
# print(n1,n2)
# n1,n2=n2,n1
# print('swaping after than',n1,n2) #fist and last elements are swap elements

# list=[4,6,3,45,67,0]
# n1=list[0]
# n2=list[5]
# print(n1,n2)
# n1,n2=n2,n1
# print('swaping after than',n1,n2) #fist and last elements are swap elements
# print(len(list)) #find length

# list=[4,6,3,45,67,0]
# count=0
# for i in range(len(list)):
# 	count+=1
# 	print(list[i])
# print('length of list',count)
# print(len(list)) #find length

# list=[4,5,6,7,34,45,0]
# min_value=min(list)
# print(min_value)
# min_obj=list.index(min_value)
# print('qq',min_obj)
# print('index',list[min_obj])
# print(list)
# list[0],list[min_obj]=list[min_obj],list[0]
# print('swap after than:',list)

# print('index',list[min_obj])
# print(list[0])

# l=[100,13,99,66,77,88,2]
# min_val=min(l)
# # print(min_val)
# min_indexno=l.index(min_val)
# # print(min_indexno)
# print('your list:',l)
# l[0],l[min_indexno]=l[min_indexno],l[0]
# print('swap after than list:',l)


# l=[100,55,99,66,77,88,2] 					 #sort min value
# print(l)
# for i in range(len(l)):
# 	min_val=min(l[i:])
# 	print(min_val)
# 	min_indexno=l.index(min_val)
# 	l[i],l[min_indexno]=l[min_indexno],l[i]
# print('sort after than',l)

# l=[100,55,99,35,77,88,66] 				 #sort max value
# print(l)
# for i in range(len(l)):
# 	max_val=max(l[i:])
# 	# print('v',max_val)
# 	max_indexno=l.index(max_val)
# 	# print('in',max_indexno)
# 	l[i],l[max_indexno]=l[max_indexno],l[i]
# print('sort after than',l)

# l=[100,55,99,66,77,88,80,80]  			#sort max value
# print(l)
# for i in range(len(l)-1):
# 	max_val=max(l[i:])
# 	max_indexno=l.index(max_val,i)
# 	if l[i]!=l[max_indexno]:
# 		l[i],l[max_indexno]=l[max_indexno],l[i]
# 	print('sort after than',l)

# l=[100,55,99,66,77,88,80,80]  			#sort min value
# print(l)
# for i in range(len(l)):
# 	min_val=l[i]
# 	for j in range(i+1,len(l)):
# 		if min_val > l[j]:
# 			min_val=l[j]
# 	min_indexno=l.index(min_val,i)
# 	if l[i]!=l[min_indexno]:
# 		l[i],l[min_indexno]=l[min_indexno],l[i]
# 	print('sort after than',l)

# l=[100,55,99,66,77,88,80,80]  			#sort max value
# print(l)
# for i in range(len(l)):
# 	min_val=l[i]
# 	for j in range(i+1,len(l)):
# 		if min_val < l[j]:
# 			min_val=l[j]
# 	min_indexno=l.index(min_val,i)
# 	if l[i]!=l[min_indexno]:
# 		l[i],l[min_indexno]=l[min_indexno],l[i]
# 	print('sort after than',l)


# print('dubalicate elements:') #find  dubalicate elements between two list
# dubalicate_list=[]
# list=[4,6,3,45,67,0]
# l2=[3,46,6,74,5,5,4,0,67]
# for i in range(len(list)):
# 	for j in range(len(l2)):
# 		if list[i]==l2[j]:
# 			dubalicate_list.append(list[i])
# print(dubalicate_list)

#99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
#						STATIC AND INSTANCE
#			class variable and static variable are same
#			classmethod,staticmethod and instancemethod are differance

# class College:		#instacce variable & instance method
# 	def __init__(self,name):
# 		self.college_name=name
# 	def show(self):
# 		print('my college name:',self.college_name)
# obj=College('adesh')
# print(obj.college_name)
# obj.show()

# class College:
# 	def __init__(self,name):
# 		self.college_name=name
# 	# def show(self):
# 	def show(self,sname,sroll):
# 		# sname="ashish kumar"
# 		# sroll=16
# 		print('my college name:',self.college_name)
# 		print('Students name:',sname)
# 		print('Student roll number:',sroll)
# obj=College('adesh')
# # print(obj.college_name)
# obj.show("ashish kumar",1630231)
# # obj.show(sroll=123,sname='ajay')#error
# # obj.show()


# class College:			#instance method 
# 	def __init__(self,name):
# 		self.college_name=name
# 	def show(self,sname,sroll):
# 		# print('my college name:',self.college_name,'Students name:',sname,'Student roll number:',sroll)
# 		print('my college name:{}\nStudents name:{}\nStudent roll number:{}\n'.format(self.college_name,sname,sroll))
# obj=College('adesh')
# obj.show("ashish kumar",1630231)
# print(id(obj))
# print()
# obj1=College('adesh')
# obj.show("ashish kumar",1630231)
# print(id(obj1))
# print()
# obj2=College('adesh')
# obj.show("ashish kumar",1630231)
# print(id(obj2))

# class College:			#instance method 
# 	def __init__(self,name,roll,salary):  			#dict in store data
# 		self.college_name=name
# 		self.roll=roll
# 		self.salary=salary
# 	def show(self,sname,sroll):
# 		# print('my college name:',self.college_name,'Students name:',sname,'Student roll number:',sroll)
# 		print('my college name:{}\nStudents name:{}\nStudent roll number:{}\n'.format(self.college_name,sname,sroll))
# obj=College('adesh',3456,5000)
# obj.show("ashish kumar",1630231)
# print(id(obj))
# print(obj.__dict__)


# class College:			#class variable and  method 
# 	string="i am an intalligent person"	#static variable
# 	print(string)
# 	@classmethod
# 	def show(cls,sname,sroll): #static method
# 		print('Students name:',sname,',''Student roll number:',sroll)
# 		# print('my college name:{}\nStudents name:{}\nStudent roll number:{}\n'.format(cls.string,sroll))
# obj=College()
# College.string
# n1=obj.show('ajay',12345)
# print(id(n1))
# print()
# n2=College.show('ajay',12345)
# print(id(n2))

# class College:			#class variable and  method 
# 	string="i am an intalligent person"	#static variable
# 	print(string)
# 	@classmethod
# 	def show(cls): #static method
# 		cls.sname='ashish'
# 		cls.sroll=3456
# 		print('Students name:',cls.sname,',''Student roll number:',cls.sroll)
# obj=College()
# College.string
# College.show()


# class College:			#static variable and  method 
# 	string="i am an intalligent person"	#static variable
# 	print(string)
# 	@classmethod
# 	def show(cls,sname,sroll): #class method
# 		print('Students name:',sname,',''Student roll number:',sroll,',''static variable value:',cls.string)
# 		# print('my college name:{}\nStudents name:{}\nStudent roll number:{}\n'.format(cls.string,sroll))
# obj1=College()
# College.string
# n2=College.show('ajay',12345)
# print(id(obj1))
# print()
# obj2=College()
# College.string
# n2=College.show('ajay',12345)
# print(id(obj2))
# print()
# obj3=College()
# College.string
# n2=College.show('ajay',12345)
# print(id(obj3))
# print('before string:',obj1.string)
# print('before string:',obj2.string)
# print('before string:',obj3.string)

# College.string="ajay"
# print('after string:',obj1.string)
# print('after string:',obj2.string)
# print('after string:',obj3.string)


# class Mobile:        		#without parameter staticmethod
# 	fb='ajay'				#class/static variable
# 	@staticmethod
# 	def show():				#staticmethod
# 		print(Mobile.fb)
# obj=Mobile()
# Mobile.show()

# class Mobile:              #with parameter staticmethod
# 	@staticmethod		#decorator
# 	def show(name,p):		#staticmethod
# 		name=name
# 		price=p
# 		print(name,price)
# obj=Mobile()
# Mobile.show('ashish',23456)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#						Inheritance & constructure

# class parant(): 			#single inheritance
# class parant:
# class Parant(object):
# 	money=100000
# 	@classmethod
# 	def showmoney(cls,age):						#class method
# 		cls.ram=age
# 		print('all proverty:',cls.money,'your age:',cls.ram)
# 	@staticmethod
# 	def static(name):							#static method
# 		your_name=name
# 		print('static your name:',your_name)
# class Son(Parant):
# 	def disp(property):
# 		property=property
# 		print('earn money by son',property)
# sonobj=Son()
# print(sonobj.money)
# Son.disp(356789)
# Son.showmoney(34)
# Son.static('ajay')

# class Parant(object):				#single inheritance
# 	money=100000
# 	def __init__(self):
# 		self.body='hand'						#instance variable
# 	def instance(self):							#instance method
# 		print('instance variable access:',self.body)
# 	@classmethod
# 	def showmoney(cls,age):						#class method
# 		cls.ram=age
# 		print('all proverty:',cls.money,'your age:',cls.ram)
# 	@staticmethod
# 	def static(name):							#static method
# 		your_name=name
# 		print('static your name:',your_name)
# class Son(Parant):								#child class
# 	def disp(property):							
# 		property=property
# 		print('earn money by son',property)
# sonobj=Son()
# print(sonobj.money)
# Son.disp(356789)
# Son.showmoney(34)
# Son.static('ajay')
# sonobj.instance()				#instace variable and method


# class Grandfather(object):						#multilable inheritance
# 	money=100000
# 	def __init__(self):
# 		self.body='hand'						#instance variable
# 	def instance(self):							#instance method
# 		print('instance variable access:',self.body)
# 	@classmethod
# 	def showmoney(cls,age):						#class method
# 		cls.ram=age
# 		print('all proverty:',cls.money,'your age:',cls.ram)
# 	@staticmethod
# 	def static(name):							#static method
# 		your_name=name
# 		print('static your name:',your_name)
# class Father(Grandfather):								#child class
# 	def disp(property):							
# 		property=property
# 		print('earn money by father',property)
# class Son(Father):
# 	def shop():
# 		company='Triazinesoft.com'
# 		print('my company name is',company)
# sonobj=Son()
# print(sonobj.money)
# Son.disp(356789)
# Son.showmoney(34)
# Son.static('ajay')
# sonobj.instance()				#instace variable and method
# Son.shop()

# class Bussiness(object):			#mutiple inheritance
# 	def disp():
# 		name='ajay'
# 		print('my name is',name)
# class Shop(object):
# 	def disp1(age,salary):
# 		print('shopper of age',age,'and salary',salary)
# class Customer(Bussiness,Shop):
# 	fb=2345678
# 	@classmethod
# 	def pay(cls,name):
# 		cls.aaa=name
# 		print('name of customer:',cls.aaa,'and earn of customers:',Customer.fb)
# cuobj=Customer()
# Customer.disp()
# Customer.disp1(23,234567)
# Customer.pay('ashish')
# # cuobj.disp()				#error








#88888888888888888888888888888888888888888888888888888888*******************************************************
            #ABSTRACT CLASS,abstract method,concerete method and INTERFACE

# from abc import ABC,abstractmethod
# class Father(ABC):
# 	@abstractmethod
# 	def disp(self):   #decleare		#abstract method
# 		pass
# 	def show(self):					#concerete method
# 		print('concerete method')
# # a=Father()                        #this step can't create object
# # a.disp()
# # a.show()
# class Child(Father):     #defination
# 	def disp(self):
# 		print('child class')
# 		print('disp abstract')
# a=Child()							#this step can create object
# a.disp()
# a.show()


# from abc import ABC,abstractmethod
# class Father(ABC):
# 	@abstractmethod					#%%%%%%
# 	def disp1(self): 
# 		pass
# 	@abstractmethod					#%%%%%  Abstract class
# 	def disp2(self): 
# 		pass
# 	def show(self):					#%%%%%%
# 		print('concerete method')
# class Child(Father):    
# 	def disp1(self):
# 		print('child class')
# 		print('disp1 abstract method')
# # c=Child()							#get error beacause all abstracts method are not giving defination		
# # c.disp1()
# # c.show()
# class Grandchild(Child):
# 	def disp2(self):
# 		print('grandchild class')
# 		print('disp2 abstract method')
# gc=Grandchild()
# gc.disp1()
# print()
# gc.disp2()
# print()
# gc.show()

# from abc import ABC,abstractmethod
# class Father(ABC):
# 	@abstractmethod         #%%%%   Interface ,  ask but In python is not available interface concept but other language available for example java
# 	def disp1(self): 
# 		pass
# 	@abstractmethod          #%%%%
# 	def disp2(self): 
# 		pass
# class Child(Father):    
# 	def disp1(self):
# 		print('child class')
# 		print('disp1 abstract method')
# class Grandchild(Child):
# 	def disp2(self):
# 		print('grandchild class')
# 		print('disp2 abstract method')
# gc=Grandchild()
# gc.disp1()
# print()
# gc.disp2()

# from abc import ABC,abstractmethod
# class DefanceForce(ABC):
# 	@abstractmethod
# 	def area(self): 
# 		pass
# 	def gun(self):					
# 		print('AK 47')
# class Army(DefanceForce):    
# 	def area(self):
# 		print('area of Army LAND')
# class AirForce(DefanceForce):
# 	def area(self):
# 		print('area of Army SKY')
# class Navy(DefanceForce):
# 	def area(self):
# 		print('area of Army SEA')
# x=Army()                           #single create obj
# x.area()
# x.gun()
# print()
# x=AirForce()
# x.area()
# x.gun()
# print()
# x=Navy()
# x.area()
# x.gun()

# from abc import ABC,abstractmethod
# class DefanceForce(ABC):
# 	@abstractmethod
# 	def area(self): 
# 		pass
# 	def gun(self):					
# 		print('AK 47')
# class Army(DefanceForce):    
# 	def area(self):
# 		print('area of Army LAND')
# class AirForce(DefanceForce):
# 	def area(self):
# 		print('area of Army SKY')
# class Navy(DefanceForce):
# 	def area(self):
# 		print('area of Army SEA')
# x=Army()                          # multiple create obj
# x.area()
# x.gun()
# print()
# y=AirForce()
# y.area()
# y.gun()
# print()
# z=Navy()
# z.area()
# z.gun()

# from abc import ABC,abstractmethod 	#used constructure,abstract class and method,concerete method
# class DefanceForce(ABC):
# 	def __init__(self):
# 		self.id=140
# 	@abstractmethod
# 	def area(self): 
# 		pass
# 	def gun(self):					
# 		print('AK 47',self.id)
# class Army(DefanceForce):    
# 	def area(self):
# 		print('area of Army LAND')
# class AirForce(DefanceForce):
# 	def area(self):
# 		print('area of Army SKY')
# class Navy(DefanceForce):
# 	def area(self):
# 		print('area of Army SEA')
# x=Army()                          # multiple create obj
# x.area()
# x.gun()
# print()
# y=AirForce()
# y.area()
# y.gun()
# print()
# z=Navy()
# z.area()
# z.gun()

# from abc import ABC,abstractmethod 	#used constructure,abstract class and method,concerete method
# class DefanceForce(ABC):
# 	def __init__(self,sid,sname):
# 		self.id=140
# 		self.sid=sid
# 		self.sname=sname
# 	@abstractmethod
# 	def area(self): 
# 		pass
# 	def gun(self):					
# 		print('AK 47',self.id)
# class Army(DefanceForce):    
# 	def area(self):
# 		print('area of Army LAND')
# class AirForce(DefanceForce):
# 	def area(self):
# 		print('area of Army SKY')
# class Navy(DefanceForce):
# 	def area(self):
# 		print('area of Army SEA')
# x=Army(234,'ajay')                          # multiple create obj
# print(x.__dict__)					#dict data store
# x.area()
# x.gun()
















