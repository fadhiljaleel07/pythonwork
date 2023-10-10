arr=[
    [2,0,1],
    [1,1,0],
    [2,0,3]
]
# position value matrix

for row in range(0,3):
    for col in range(0,3):
        value=row+col-arr[row][col]
        print(value,end="\t")
    print()