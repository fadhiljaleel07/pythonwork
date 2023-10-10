lst=[2,3,4,6,7,8]
cubes=[n**3 for n in lst]
print(cubes)

squares=[n**2 for n in lst]
print(squares)

# squares=[]
# for n in lst:
#     sq=n**2
#     squares.append(sq)

# print(squares)

# add_two=[n+2 for n in lst]
# print(add_two)

evens=[n for n in lst if n%2==0]
print(evens)
odd=[n for n in lst if n%2!=0]
print(odd)


# years 1800-2025

years=[y for y in range(1800,2026)]
print(years)


# century years

century_years=[y for y in years if y%100==0]
print(century_years)

# non century years

non_century=[y for y in years if y%100!=0]
print(non_century)

