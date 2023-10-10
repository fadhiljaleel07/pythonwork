from json import load
path="C:\\Users\\fadhi\\OneDrive\\Desktop\\Pythonworks\\countries\\countries.json"

with open(path,encoding="utf-8")as f:
    countries=load(f)

# start_withc=[c.get("name") for c in countries if c.get("name").startswith("c")]
# print(start_withc)

# name_capital=[[c.get("name"),c.get("capital")] for c in countries]
# print(name_capital)

# c_with_borders=[c for c in countries if "borders" in c]
# max_border_country=max(countries,key=lambda c:len(c.get("borders")))

# print(max_border_country.get("name"))

india_borders=[c.get("borders") for c in countries if c.get("name")=="India"]
print(india_borders)

india_borders=[c.get("borders")for c in countries if c.get("names")=="Afghanistan"][0]
india_borders_names=[c.get("name") for c in countries if c.get("alpha3code") in india_borders]
print(india_borders_names)

for
