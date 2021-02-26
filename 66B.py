words=[]
while True:
       s=input()
       if s=="":
              break
       else:
              nom,word=s.split(".")
              words.append(word)
words.sort()
print(",".join(words))
