X=set('Welcome To Edureka')
print(X)

A={1,2,3,4}
B={3,4,5,6}
print(A|B)
print(A&B)

A={1,2,3,4,5}
B={4,5,6,7,8}
print(A-B)

s={'a','b','c','d','e','f','o','v'}
set1={'a','b','d','o','v'}
set2={'a','c','d','o','e'}
print(set1|set2)
print(set1&set2)
print(set1-set2)

#add

s={1,2,3,'a','b'}
set1={1,'a','b'}
print(1 in s)

print(set1.issubset(s))

print(5 not in s)

print(s.issuperset(set1))

print(s.union(set1))

print(s.intersection(set1))

print(s.difference(set1))

print(s.symmetric_difference(set1))


s={1,2,3,'a','b'}
s.add('c')
print(s)

s.remove(1)
print(s)

s.discard(3)
print(s)

s.pop()
print(s)

s.clear()
print(s)