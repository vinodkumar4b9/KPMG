# In this Python script as per the requirement , I am able to fetch the value for Example in this case if you run this script you  will get "a" as output 
# I have used a python  module named bunch to get the required output , SO If you want to run this python script you need to have a module name bunch , please use the below steps to install the same 
# pip install --trusted-host pypi.python.org bunch
# Attaching the output on read me file with screenshots 

from bunch import bunchify
d = {'x':{'y':{'z':'a'}}}
p = bunchify(d)
print(p.x.y.z)
