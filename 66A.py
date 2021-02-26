words=[]
for i in range(5):
  s=input()
  nom,word=s.split(".")
  words.append(word)
words.sort()
print(",".join(words))
