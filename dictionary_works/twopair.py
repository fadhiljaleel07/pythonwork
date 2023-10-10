lst=[2,3,5,7,8,9,10]
sum=19
lst.sort()
low=0
upper=len(lst)-1
while(low<upper):
    cur_sum=lst[low]+lst[upper]
    if cur_sum==sum:
        print("pairs",lst[low],lst[upper])
        break
    elif cur_sum < sum:
        low+=1
    else:
        upper-=1
