x=[100,110,120,130,140,150]
multiply=[a*5 for a in x]
print(multiply)

def divisible_by_three(n):
    n=20
    d=range(n)
    for a in d:
        if a%3==0:
            print(a)
        else:
            print()
x=[[1,2],[3,4],[5,6]]
for a in x:
    print(x)
def smallest(g):
    x=[3,6,8,2,4,1,5,7]
    x.sort()
    print(x.index[0])
def deplicate(x):
    x=["a","b","a","e","d","c","e","f","g","h"]
    w=[]
    w.extend(x)
    y=set(x)
    z=set(w)
    t=y.union(z)
    s=list(t)
    print(s)
def divisible_by_seven():
    r=range(100,200)
    for a in r:
        if a%7==0:
            print("divisible by seven")
        else:
            print(a) 
def greet():
    students=[{"age":19,"name":"Eunice"},{"age":21,"name":"Agnes"},{"age":18,"name":"Teresa"},{"age":22,"name":"Asha"}]
    for a in students:
        print("Hello {}, you were born in the year {}".format,a.key("name"),a.key("age"))           

