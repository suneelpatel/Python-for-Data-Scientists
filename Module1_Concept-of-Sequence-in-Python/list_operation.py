list=["Hadoop","Python","Android"]
print(list[1])

print(list[0:2])

print(list[-1])

list=["Hadoop","Python","Android"]

list[1]="Java"
print(list)

del(list[2])
print(list)

list=[1,2,3]
list.append("Machine Learning")
print(list)

list.extend(['g','h'])
print(list)

list.insert(1,'Scripting')
print(list)

list.remove(3)
print(list)

lst=[1,4,2,'x','y','z']
if(type(lst)==list):
    print("Yes")



list3=[1,2,5,'Python','Haddop']
print(type(list3))

print([x**2 for x in[1,2,3,4,5]])


list4=['Pytyhon','Java','Haddop','Android']
print(list4.sort())
print(list3.reverse())

print([x**2 for x in[1,2,3,4,5]])

list=[1,2,3,4,5,'a','b','c']
print(list.pop(3))

list.remove('a')
print(list)

list1=['Python','XYZ','ABC','PQR']
print(list1)

print(sorted(list1))

print(list1[::-1])