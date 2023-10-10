student={"name":"fadhil","roll":7,"course":"django"}
print(student["course"])


print(student.get("salary"))
if "total" in student:
    print("present")

else:
    print("not present")


student["grade"]="A"
print(student)

for k in student.keys():#to print all the keys in the dictionary
    print(k)


for v in student.values():# to print all the values in the dictionary
    print(v)


for k,v in student.items(): #to print all the values and keys in the dictionary
    print(k,v)
