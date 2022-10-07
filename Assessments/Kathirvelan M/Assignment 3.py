# -*- coding: utf-8 -*-
"""DA_Assignment_3_Python_Kathirvelan_M.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TzmjXfeeKKpJSrtkOM7lFLOFqfG-pg2K

## Exercises

Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

** What is 7 to the power of 4?**
"""

print(pow(7,4))

"""** Split this string:**

    s = "Hi there Sam!"
    
**into a list. **
"""

s = "Hi there Sam!"
print(s.split())



"""** Given the variables:**

    planet = "Earth"
    diameter = 12742

** Use .format() to print the following string: **

    The diameter of Earth is 12742 kilometers.
"""

planet = "Earth"
diameter = 12742
print('The diameter of {one} is {two} kilometers'.format (one=planet,two=diameter))



"""** Given this nested list, use indexing to grab the word "hello" **"""

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
s = lst[3][1][2]
print(s)

"""** Given this nest dictionary grab the word "hello". Be prepared, this will be annoying/tricky **"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])

"""** What is the main difference between a tuple and a list? **"""

print("The list are mutable whereas Tupeles are Immutable")

"""** Create a function that grabs the email website domain from a string in the form: **

    user@domain.com
    
**So for example, passing "user@domain.com" would return: domain.com**
"""

def domain(mail):
    print(mail.split('@')[-1])

mail = "user@domain.com"
domain(mail)



"""** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **"""

pet = "dog"
if(pet == "dog"):
  print("True")
else:
  print("False")



"""** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **"""

sentence = "dog is a pet animal my dog name is jacky my dog ig a good dog"
list = sentence.split()
count = 0
for i in range(0,len(list)):
  if (list[i] == "dog"):
    count = count +1
print("The Word Dog occurs",count,"times!")



"""### Problem
**You are driving a little too fast, and a police officer stops you. Write a function
  to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
  If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
  and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
  cases. **
"""

def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'

caught_speeding(86,True)

caught_speeding(61,False)

"""Create an employee list with basic salary values(at least 5 values for 5 employees)  and using a for loop retreive each employee salary and calculate total salary expenditure. """

emp_salary = [20000,25000,30000,35000,40000]
sum = 0
for i in range(0,len(emp_salary)):
  sum += emp_salary[i]
print(sum)

"""Create two dictionaries in Python:

First one to contain fields as Empid,  Empname,  Basicpay

Second dictionary to contain fields as DeptName,  DeptId.

Combine both dictionaries. 
"""

dic1 = { 'Empid': [101,102], 'EmpName':["Kathir","Velan"] }
dic2 = {'DeptName': ["IT","ECE"], 'Deptid':[205,206]}
dic3 = {**dic1, **dic2}
print(dic3)