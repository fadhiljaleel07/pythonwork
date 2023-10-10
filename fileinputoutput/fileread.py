f=open("C:\\Users\\fadhi\\OneDrive\\Desktop\\Pythonworks\\fileinputoutput\\data.txt","r")
# lst=[]
# for line in f:
#     lst.append(line.rstrip("\n"))
# print(lst)
# longest_word=max(lst,key=lambda w:len(w))
# print(longest_word)

words=[line.rstrip("\n") for line in f]
longest_word=max(words,key=lambda w:len(w))
print(longest_word)