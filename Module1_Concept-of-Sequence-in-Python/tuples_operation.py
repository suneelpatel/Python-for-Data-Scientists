tup1=("Haddop","Python","Java")

print(len(tup1))
print(max(tup1))
print(min(tup1))





tup1=("Haddop","Python","Java")

print(len(tup1))

print(tup1*2)

print("Java" in tup1)

tup2=(1,3,5,7)
tup3=(2,4,6,8)
tup4=tup2+tup3
print(tup4)

del(tup2)
print(tup2)


tup=(1,3,5,2)

print(sorted(tup))

print(tup[::-1])


tuple1=(1,3,5,7,'a','b')
lst=list(tuple1)

print(lst)

lst[1]="Python"
print(lst)

tuple2=tuple(lst)
print(tuple2)