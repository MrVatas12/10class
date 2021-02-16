'''9.41
q=input()
for i in q:
    print(i)
'''
'''9.42
  
q=input()
q2= q[::-1]
print(q2)
'''
'''9.43
i = input("Введите слово")
i=i[::2]
i=i[1:]
print(i)
'''
'''
9.44
q=input()
q2= q[::-1]
print('Слово t = ' + q2)
'''
'''9.45 
zvezda="*"
print(zvezda*5)
'''
'''9.46
line="-"
print(line*8)
'''
'''9.47
a=int(input())
b=input()
print( a*b)
'''
'''9.48
i = input("Вводи слово")
print('*'*4+i+5*'-')
'''
'''9.49
i = input("Вводи слово")
print('*'*len(i)+i+len(i)*'-')
'''
'''9.51
s=input()
for i in s:
       if i=="и" or i=="И":
              print(i)
              
'''
'''9.52
s=input()
b=input()
for i in s:
       if i==b:
              print(i)
'''
'''9.54
s=input()
for i in s:
       if i=="м" or i=="н":
              print(i)
'''
'''9.55
s=input()
b=input()
d=input()
for i in s:
       if i==b or i==d:
              print(i)
'''
'''9.56
s=input()
print(s.count("нн"))
'''
'''9.57
a=input()
print(a)
b=''
g=0
j=1
for i in a:
    if g!=j:
        g+=1
    else:
        j+=1
        print(i)
'''


'''9.59
a=input()
b=0
for i in a:
    if i !=" ":
        b+=1
        print(i)
print(b)
'''


'''9.60
c=input()
p=0
for i in c:
    if i ==" ":
        p+=1
print(p)
'''

'''9.61
q=input()
h=input("Введите символ")
print(q.count(h))
'''


'''9.63
i=input("Введите текст со знаками")
j=0
c=0
for g in i:
    if g =="*":
        j+=1
    if g=="-":
        c+=1
print(j,c)
'''
'''9.64
a=input("Введите текст со знаками")
j=0
for i in a:
    if a == a:
        j+=1
print(j)
'''


'''9.68
q= input()
c=q.count("*")
g=q.count("-")
b=c+g
print(b)
'''
'''9.69
q=input("ВВедите предложения")
print(q.count("."))
'''


'''9.70
q=input("Введите предложения")
g=0
for i in q:
    if i =="А" or i =="а" or i =="О" or i =="о" or i =="у" or i=="У" or i =="Ё" or i =="ё" or i=="И" or i=="и" or i=="Ы" or i=="ы" or i=="Я" or i =="я" or i=="Э" or i=="э":        
        g+=1
print(g)
'''


'''9.71
q=input("Введите предложения")
a=q.count("м")
b=q.count("н")
if a>b:
    print ("Букв м больше")
else:
    print("Букв н больше")
'''
