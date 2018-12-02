
# coding: utf-8

# In[1]:


# Hello World program in Python
    
from random import *;
def randomA ():
    s = randint(0,3);
    n = randint (1,26); 
    p = randint (0,9); 
    k = randint (1,3); 
    value = 0; 
    if (s == 0):
        value = 64+n; 
        if(value > 90):
            value -= 90;
            value +=64
    elif (s == 1):
        value = 97+n; 
        if(value > 122):
            value -= 122;
            value += 97;
    elif ( s == 2):
        value = 34+k; 
    else:
        value = p; 
    return value; 

def randomLetter():
    s= randint (0,1); 
    n= randint(1,26)
    if (s == 0):
        value = 64+n; 
        if(value > 90):
            value -= 90;
            value +=64
    elif (s == 1):
        value = 97+n; 
        if(value > 122):
            value -= 122;
            value += 97;
    return value; 

def randomNumber ():
    p = randint (0,9); 
    return p; 

def randSymbol():
    n = randint (1,3); 
    value = 34+n; 
    return value; 

def password ():
    l = randint(10,26);
    m = randomLetter();
    k = randomNumber();
    h = randSymbol();
    pas = chr(m)+str(k)+chr(h);
    for i in range(3,l):
        s = randomA()
        if ( s>= 0 and s<=9):
            n = str(s);
        else:
            n = chr(s);
        pas += n; 
    return pas; 

print(password())

