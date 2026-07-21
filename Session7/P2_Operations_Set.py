set1=set()

set1.add(1)
set1.add(2)
set1.add(3)
set1.add(4)
print(set1)

set2 = set()
set2.add(2)
set2.add(5)
set2.add(6)
set2.add(7)
set2.add(4)
print(set2)

union=set1.union(set2)
print("Union =",union)

intersection=set1.intersection(set2)
print("Intersection= ", intersection)

set_difference=set1.difference(set2)
print("Set Difference =",set_difference)


#Homework : set={}  datatype of it
set={}
print(type(set))

