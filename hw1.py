
# coding: utf-8

# In[12]:

def sum(ar):
    sum = 0;
    for elem in ar:
        sum = sum+elem;
    return sum


# In[13]:

def factorial(n):
    product = 1;
    i=1;
    if(n<0):
        print("No solution")
    else:
        while(i<n):
            i=i+1;
            product = i*product;
        return product


# In[14]:

def combinatorics(m,n):
    i=0;
    a=1;
    for b in range (0,n):
        a=a*(m-i);
        i=i+1;
    i=1;
    for b in range (0,n):
        a=a/i;
        i=i+1;
    
    return int(a)


# In[15]:

def linearity(a,b,c):
    x=0;
    y=0;
    m=0;
    n=0;
    if (a[0]==b[0]==c[0] or a[1]==b[1]==c[1]):
        return True
    else:
        x=a[0]-b[0];
        y=a[1]-b[1];
        m=y/x;
        x=a[0]-c[0];
        y=a[1]-c[1];
        n=y/x;
        if(m==n):
            return True
        else:
            return False


# In[16]:

def is_palindrome(string):
    p=list(string);
    i=int(len(p)/2);
    c=True;
    for b in range (0,i):
        if (p[b]!=p[len(p)-b-1]):
            c=False;
    return c


# In[17]:

def n_n_times(n):
    x = 0;
    y = 0;
    exp = 0;
    for i in range (1,n):
        exp = exp+i
    exp=exp-1;
    for i in range (1,n):
        for j in range (0,i):
            x=x+i*10**exp;
            exp=exp-1;
    return str(x)


# In[18]:

def is_prime(n):
    x=True;
    m=n**0.5;
    m=int(m);
    for i in range (2,m):
        if (n%i==0):
            x=False;
    if(n==2):
        x=True
    return x
        


# In[19]:

def fibonacci(n):
    a=0;
    b=1;
    for i in range (0,n):
        if (i%2==0):
            b=b+a;
        else:
            a=a+b;
    if (n==0):
        return 0
    else:
        return max([a,b])


# In[20]:

def every_other_num(n,m):
    x=[];
    if ((m-n)%2==0):
        for i in range (0,int((m-n)/2)+1):
            x.append(n+2*i);
    else:
        for i in range (0,int((m-n)/2)+1):

            x.append(n+2*i);
    return x          


# In[21]:




# In[ ]:




# In[ ]:




# In[ ]:



