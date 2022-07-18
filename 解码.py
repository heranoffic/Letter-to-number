# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 20:18:36 2022

@author: Administrator
"""
def f(a):
    if a=="000000":
        print("0",end="")
    if a=="000001":
        print("1",end="")
    if a=="000010":
        print("2",end="")
    if a=="000011":
        print("3",end="")
    if a=="000100":
        print("4",end="")
    if a=="000101":
        print("5",end="")
    if a=="000110":
        print("6",end="")
    if a=="000111":
        print("7",end="")
    if a=="001000":
        print("8",end="")
    if a=="001001":
        print("9",end="")
    if a=="001010":
        print("a",end="")
    if a=="001011":
        print("b",end="")
    if a=="001100":
        print("c",end="")
    if a=="001101":
        print("d",end="")
    if a=="001110":
        print("e",end="")
    if a=="001111":
        print("f",end="")
    if a=="010000":
        print("g",end="")
    if a=="010001":
        print("h",end="")
    if a=="010010":
        print("i",end="")
    if a=="010011":
        print("j",end="")
    if a=="010100":
        print("k",end="")
    if a=="010101":
        print("l",end="") 
    if a=="010110":
        print("m",end="")
    if a=="010111":
        print("n",end="")
    if a=="011000":
        print("o",end="")
    if a=="011001":
        print("p",end="")
    if a=="011010":
        print("q",end="")
    if a=="011011":
        print("r",end="")
    if a=="011100":
        print("s",end="")
    if a=="011101":
        print("t",end="")
    if a=="011110":
        print("u",end="")
    if a=="011111":
        print("v",end="")
    if a=="100001":
        print("x",end="")
    if a=="100010":
        print("y",end="")
    if a=="100011":
        print("z",end="")
a=str(input("expassword："))
for i in range(int(len(a)/6)):
    i=i*6
    b=a[i]+a[i+1]+a[i+2]+a[i+3]+a[i+4]+a[i+5]
    f(b)
        