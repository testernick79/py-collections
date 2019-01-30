set1 =  set(range(10))
set2 = {0,1,2,3,5,7,11,13,17,19,23}

set.union(set2)
print(set2)
print(set1)

print("Displayed Union")
print(set1 | set2)#displays both

# Get Difference of the 2 sets
set1.difference(set2)
print("set1.difference(set2)")
print(set1.difference(set2))
print("OR")


set2.difference(set1)
print("IM THE DIFF OF SET1")
print(set2.difference(set1))

print(set1 - set2)

print("Symetric difference")
print(set1 ^ set2)

print("intersection differences")
print(set1 & set2)

