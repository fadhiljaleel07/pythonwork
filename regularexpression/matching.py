from re import *
text="fAdhiljaleel8547"
pattern="[AEIOUaeiou]"
# matcher=finditer("dhil",text)
# count=0
# for m in matcher:
#     print(m.start(),m.group())
#     count+=1
# print(count)

matcher=finditer(pattern,text)
count=0

for m in matcher:
    print("location:",m.start(),"Group: ",m.group())
