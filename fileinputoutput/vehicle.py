f=open("C:\\Users\\fadhi\\OneDrive\\Desktop\\Pythonworks\\fileinputoutput\\number.txt","r")
numbers=[line.rstrip("\n")for line in f]
for n in numbers:
    if n.startswith("kl"):
        print(n)

kerala_numbers=[n for n in numbers if n.startswith("kl")]
