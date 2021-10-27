#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("n="))
asal = 1
for i in range(2,n,1):
    if n % i == 0 :
        asal = 0
if asal == 0:
    print(n,"sayısı asal değildir.")
else:
    print(n,"sayısı asaldır.")


# In[3]:


n = int(input("n="))
asal = 1
for i in range(2,n,1):
    if n % i == 0:
        asal =0
if asal ==0:
    print(n,"sayısı asal değildir")
else:
    print(n,"sayısı asaldır")


# In[4]:


n = int(input("n="))
Acarpan = 2
while n>1:
    if n%Acarpan == 0:
        n = n / Acarpan
        print(Acarpan)
    else:
        Acarpan = Acarpan + 1


# In[1]:


n = int(input("n="))
carpim = 1
print("sonhane"," ", "carpim")
while n>0:
    sonhane = int(n%10)
    carpim = carpim * sonhane
    print("  ", sonhane,"        ",carpim)
    n = (n - sonhane) / 10


# In[7]:


n = int(input("n="))
while n>9:
    carpim = 1
    while n>0:
        sonhane = int(n%10)
        carpim = carpim * sonhane
        n = (n - sonhane) / 10
    print(carpim)
    n = carpim


# In[10]:


h = 5
yol = 0
print(yol,"  ", h)
yol = yol + h
h = h*0.8
print(yol , "  ", h)
while h>1:
    yol = yol + 2*h
    h = h*0.8
    print(yol,"  ",h)


# In[ ]:




