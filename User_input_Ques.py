#!/usr/bin/env python
# coding: utf-8

# In[2]:


# WAP and take the input from the user and check whtr an alpha is vowel or consonent?
x=input("enter the character:")
if (x == 'a' or x == 'e' or
        x == 'i' or x == 'o' or x == 'u' or x == 'A' or x == 'E' or
        x == 'I' or x == 'O' or x == 'U'):
    print('yes it is vowel')
else:
    print("it is a consonant")


# In[10]:


# WAP and take the input from the user and check whthr a number is divible by 2 or not?
x=int(input("enter the number--> ")) #x=11 #x=14
if x%2==0: #11%2==0 False #14%2==0 True
    print("Divisible by 2")
else:
    print("Not divisible by 2")


# In[11]:


# WAP and take the input from the user if the age of the user is above 18 thn he/she can vote?
x=int(input("enter the number--> ")) #x=21 #x=14
if x>=18: # 21>=18 True #14>=18 False
    print("He/She can vote") #he/she can vote
else:
    print("Cannot vote")


# In[12]:


# WAP and take the input from the user and check whtr the input is alphabet or not?
x=input("enter the string--> ") #x=2
if x.isalpha(): # kya mera 2 alphabet hota hh? False
    print("Yes it is")
else:
    print('No ')


# In[13]:


# WAP and take the input from the user and check whtr an alpha is vowel or consonent? 
#DIFFERENT APPROACH
x=input("enter the string--> ")
if x in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Consonent")


# In[5]:


# WAP nd take the input from the user and check the string is palindrome or not?

x=input("enter the string:")
if x[::-1]==x:
    print("yes")
else:
    print("no")


# In[9]:


# WAP and take the input from the user if the len of the user is above 3 thn print hiii if the len of the user is below three or equal to 3 thn reverse the string
x=input("enter the string:")
if(len(x)>3):
    print("hii")
else:
    print(x[::-1])


# In[14]:


# WAP nd take the input from the user and check the string is palindrome or not?

x=input("Enter the string--> ") 
if x==x[::-1]: 
    print("Palindrome")
else:
    print("Not Plaindrome")


# In[ ]:




