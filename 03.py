# zip
l1=[1,2,3,4,5]
l2=[11,22,33,44,55]
z=zip(l1,l2)
print(type(z))
for i in z:
    print(i)

#enumerate
l1=[11,22,33,44,55]
em=enumerate(l1)
l2=[i for i in em]
print(l2)

em=enumerate(l1,start=100)
l2=[i for i in em]
print(l2)

# collections
import collections
# namedtuple
Point=collections.namedtuple("Point",['x','y'])
p=Point(11,22)
print(p.x)
print(p[0])
#deque
q=collections.deque(['a','b','c'])
print(q)
q.append("d")
q.appendleft("e")
print(q)
#defaultdict
func=lambda :"jane"
d1 = collections.defaultdict(func)
d1["one"]=1
d1["two"]=2
print(d1['one'])
print(d1['three'])

#Counter
c=collections.Counter("dsffdsjcdsvfmc dsfd")
print(c)