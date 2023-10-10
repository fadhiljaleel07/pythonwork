from json import load
path="C:\\Users\\fadhi\\OneDrive\\Desktop\\Pythonworks\\movies\\mdb.json"
with open(path,encoding="utf-8") as f:
    movies=load(f)
# print(len(movies))

# movie_name=[m.get("title")for m in movies]
# print(movie_name)

# movie_year=[m.get("title")for m in movies if m.get("year")=="2005"]
# print(movie_year)

# lengthy_movie=max(movies,key=lambda m:int(m.get("runtime")))
# print(lengthy_movie)

# genres={g for m in movies for g in m.get("genres")}
# print(movies)

comedy_movies=[m.get("title")for m in movies if "comedy" in m.get("genres")and m.get("year")=="2015"]
print(comedy_movies)

wc={}
for m in movies:
    years=m.get("years")
    if years in wc:
        wc[years]+=1
        pass
    else:
        wc[years]=1
print(max(wc))