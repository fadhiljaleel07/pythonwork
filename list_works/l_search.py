lst=[10,2,13,14,5]
element=13
i=0
limit=len(lst)
is_present=False
while(i<limit):
    cur_value=lst[i]
    if cur_value==element:
        is_present=True
        break
    i+=1

print(is_present)