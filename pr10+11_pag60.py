a=set()
for i in range(4):
    c=input()
    if ord(c)<65:
        c=int(c)
        a.add(c)
    else:
        a.update(c)
b,x,y,z=set(),set(),set(),[]
x=a.copy()
b=a.copy()
print(a)
for i in b:
    z.append(i)
    x.remove(i)
    print(x)
    print(a.difference(x))
    x.add(i)
y.add(z[0])
for l in range(1,len(a)):
    y.add(z[l])
    print(y)
    print(a.difference(y))
    y.remove(z[l])
a.clear()
print(a)