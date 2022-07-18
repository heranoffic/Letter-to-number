# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 19:40:25 2022

@author: Administrator
"""
def f(a):
    if a==0:
        print("000000",end="")
    if a==1:
        print("000001",end="")
    if a==2:
        print("000010",end="")
    if a==3:
        print("000011",end="")
    if a==4:
        print("000100",end="")
    if a==5:
        print("000101",end="")
    if a==6:
        print("000110",end="")
    if a==7:
        print("000111",end="")
    if a==8:
        print("001000",end="")
    if a==9:
        print("001001",end="")
    if a=="a":
        print("001010",end="")
    if a=="b":
        print("001011",end="")
    if a=="c":
        print("001100",end="")
    if a=="d":
        print("001101",end="")
    if a=="e":
        print("001110",end="")
    if a=="f":
        print("001111",end="")
    if a=="g":
        print("010000",end="")
    if a=="h":
        print("010001",end="")
    if a=="i":
        print("010010",end="")
    if a=="j":
        print("010011",end="")
    if a=="k":
        print("010100",end="")
    if a=="l":
        print("010101",end="") 
    if a=="m":
        print("010110",end="")
    if a=="n":
        print("010111",end="")
    if a=="o":
        print("011000",end="")
    if a=="p":
        print("011001",end="")
    if a=="q":
        print("011010",end="")
    if a=="r":
        print("011011",end="")
    if a=="s":
        print("011100",end="")
    if a=="t":
        print("011101",end="")
    if a=="u":
        print("011110",end="")
    if a=="v":
        print("011111",end="")
    if a=="x":
        print("100001",end="")
    if a=="y":
        print("100010",end="")
    if a=="z":
        print("100011",end="")
a=input("print:")
b=[]
for i in a:
    ord(i)
    b.append(i)
print(b)
for j in range(len(b)):
    f(b[j])
    