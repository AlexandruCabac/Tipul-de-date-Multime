a,c=eval(input()),1
for i in a:
    if type(i)!=type(1):
        c=0
b=eval(input())
for i in b: 
    if type(i)!=type(1):
        c=0
if c==1:
    print("Intersectia multimilor",a.intersection(b))
    print("Reuniunea multimilor",a.union(b))
    print("Diferenta dintre multimea A si B",a.difference(b))
    print("Diferenta dintre multimea B si A",b.difference(a))
else:
    print("Error")