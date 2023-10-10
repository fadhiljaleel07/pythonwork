lst=[10,2,3,14,6]
element=2
low=0
upper=len(lst)-1
lst.sort()
is_present=False
while(low<upper):
    mid=(low+upper)//2
    if element==lst[mid]:
        is_present=True
        break
    elif element<lst[mid]:
        upper=mid-1
    elif element>lst[mid]:
        low=mid+1

print(is_present)