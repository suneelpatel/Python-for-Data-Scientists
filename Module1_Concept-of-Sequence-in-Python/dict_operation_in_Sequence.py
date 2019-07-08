dict={1:"Python",2:"Android"}
print(dict)
print(dict[1])

dict[1]="Javascript"
print(dict)

del(dict[2])
print(dict)

print(len(dict))
print(str(dict))
print(type(dict))

print(dict.copy())
dict.clear()
print(dict)

#add
dict1={1:'Python',2:'Android'}
print(dict1.items())

print(dict1.keys())

print(dict1.values())

print(dict1.setdefault(1,4))


dic={3:'Python',1:'Java',2:'Big Data'}
ks=list(dic.keys())
print(ks)

sk=sorted(ks)
print(sk)

for key in sk:
    print(key,'=>',dic[key])



rec = {'name': {'first': 'Bob', 'last': 'Smith'},
'jobs': ['dev', 'mgr'],'age': 40.5}
print(rec.get('name'))
