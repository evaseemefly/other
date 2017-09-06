
import shutil
import os
import sys

age=23
d1={'name':'123',}


def myfunc(age,**kwargs):
    print(age,kwargs)

def myfunc1(name,**kwargs):
    print(name,kwargs)

def myCopy(source,target):
    shutil.copytree(source,target)
    # shutil.copy(source,target)


myfunc(age,**d1)
# myfunc1("123",**d1)
source=r'E:\03协同开发\other\04python-日常开发的小程序\SOURCE'
target=r'E:\03协同开发\other\04python-日常开发的小程序\TARGET\1'
myCopy(source,target)


