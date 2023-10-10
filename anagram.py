text1=input("Enter a text:")
text2=input("Enter a text:")

word1=sorted(text1)
word2=sorted(text2)

if word1==word2:
    print("is anagram")
else:
    print("is not anagram")    
    