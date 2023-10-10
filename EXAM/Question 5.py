from re import *

pass_chk=input("Enter the password:")


rule="[a-z+A-Z+\W]{6}+"
matcher=fullmatch(rule,pass_chk)

if matcher==None:
    print("valid")
else:
    print("invalid")     