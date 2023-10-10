text="ABBCDCE"
wc={}
dup_lst=[]
for ch in text:
    if ch in text:
        dup_lst.append(ch)
    else:
        wc[ch]=1
print(dup_lst[1])
