employee={"name":"fadhil","age":22,"salary":"25000","id":"2416"}

print(employee["age"])
print(employee["id"])
print(employee["name"])
print(employee["salary"])

if("salary" in employee):
    print("present")

else:
    print("not present")

#update
employee["salary"]=20000
print(employee["salary"])

employee["salary"]+=5000
print(employee)