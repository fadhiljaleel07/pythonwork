source_word="decreased"
target_word="dress"
wc={}

for ch in source_word:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
for ch in target_word:
    for ch in wc and wc.get[ch]>0:

    #ch="d"
        if ch in wc:
            current_value=wc[ch]
        if current_value>0:
            wc[ch]-=1
            is_kangaroo=False
            break
        else:
            is_kangaroo=False
print(is_kangaroo)