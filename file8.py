#eg-3

'''
def profile(name,age,place):
    print(name,age,place)
profile("sid",28,"kadapa")



def profile(name, age, place):
    txt = "My name is {}. I am {} years old. I am from {}."
    print(txt.format(name, age, place))
profile("Shashank", 21,"KSRM")
'''

# ! return
#1.) A variable declared inside the function can be accessed outside the function
#using return
#2.) return does not prrint anything
#3.) we cannot write any code below return statement

'''
def f1(a,b):
    c=a*b
    return c
#print(f1(6,8))
obj=f1(6,8)
obj1=f1(4,6)

def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)
'''

'''
n=123
def palindrome(n):
    print(n)
'''
'''
def palindrome(n):
    string=str(n)
    rev=str(n)[::-1]
    if string==rev:
        print(n,"palindrome")
    else:
         print("not palindrome")
a=int(input("enter the value:" ))
palindrome(a)
'''
#Based on the declaration of parameter
#? functions are divided into 5 catagories
#Positional args
#keyword args
#default args
#variable length args
# keyword variable length args
# Positional args


# * Positional args
# ? The position of parameter have to be same as position as arguments

'''
def profile(name,phone,mark):
    txt="My name is{}. My phone number{}. I got{} marks{}."
    print(txt.format(name,phone,mark))
profile(96668686,"Usman",100) #unexpected
'''
# ! Eg:1
#? To overcome the disadvantage of position args, we use keyword args
# ? it is process of initiating the parameter with args while calling the
# funtions

'''
def profile(name,phone,mark):
    txt="My name is{}. My phone number{}. I got{} marks."
    print(txt.format(name,phone,mark))
profile(name="Usman",mark=100,phone=96668686)
'''

# * todo --> Exception of keyword args function
'''
def profile(name, phone, mark):
     txt="My name is{}. My phone number{}. I got{} marks{}."
     print(txt.format(name,phone,mark))

profile(name = "shashank", mark=99, phone=9876543210) # Error
profile(9876543210,name= "shashank", mark=99) # error
profile("shashank",mark=98,phone=9876543210)
'''

# * default args
# the method of assigning the arguement to the parameter while declaring the function

# eg:1
'''
def profile(name,phone,place="kadapa"):
    txt="my name is {}.my phone number is {}. i am from {}"
    print(txt.format(name,phone,place))
profile("arjun",7569329040,)    
    



#eg-2
def profile(name,phone,place="kadapa"):
    txt="my name is {}.my phone number is {}. i am from {}"
    print(txt.format(name,phone,place))
profile("arjun",7569329040,"kadapa")    
  

#Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
#The length of the string is variable. The task is to find the minimum number of ‘*’ 
#or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
#and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
#Note : The output will be a positive or negative integer based on number of ‘*’ 
#and ‘#’ in the input string.

#-->(*>#): positive integer
#-->(#>*): negative integer
#->(#=*): 0
'''
#Example 1:
#Input 1:

###***   -> Value of S
#Output :

#0   → number of * and # are equal
'''
# variable length parameter

Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal

eg:2
# ! Exception
def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
    if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
     txt="My name is{}. My phone number{}. I got{} marks{}."
     print(txt.format(name,phone,place))
    else:
        print("You are not eligible to Signup")
file("Shashank",9876543210)


# ! Eg:1
#To pass more then 1 arg to a paremeter means we use variable length args
# To convert normal paremeter to variable length param, add to ther prefix of param

#name="Usman", " Charan ", " NAresh "
#print(name)
 

def profile(*name):
    for val in name:
        print(" My name is",val)
profile("ashok", 'goa', 'Alone')

eg:2
def profile(*name,age):
    #for val in name:
       # print("My name is",val,"My age is",age)
#profile("ashok",'name2','name3',28)#erroe-->age has no args

''' 
def profile(age,*name):
    for val in name:
        print("My name is",val,"My age is",age)
profile(28,"ashok",'name2','name3')

#keyword variable length args
#kwargs--->which is used to provide the args in the form
#of key value pair.
#eg:1
def price(**price_list):
    print(price_list)
price(shirt=1000,iphone=80000)

n=5
{1:1,2:4,3:9,4:16,5:25}

n=int(input("enter the number:"))
d1={}
for val in range(1,n+1):
    d1[val]=val**2
print(d1)
    

def dict1(n):
    d1={}
    for val in range(1,n+1):
        d1[val]=val**2
    print(d1)
dict1(5)

#--->object oriented programming
#the paradigms of objects oriented programming are

#class
#objects
#inheritance
#polymorphism
#abstraction
#encapsulation
   

#class is a blue print of an object
l1=[1,2,3,4,5,6]

eg:1
class c1:
    name1="sidhu"
    print(name1)


eg:2
class person:
    name="sidhu"
c=person()#c is object
#the process of creation of an object is called as instantiation
print(c.name)


eg:3
#creat of a method
#when the function is created with a class is called as method
'''
class person:
    def display(person):#it is amethod
        print("hello welcome to classes")
    p=person()
    p.display()
'''

eg:4
class person:
    fname="sidu"#atteibute or static variable
    def first_name(self):
        print(self.fname)
    def full_name(self):
        print(self.fname+" "+self.lname)
p=person1()
p.first_name()
p.full_name()































