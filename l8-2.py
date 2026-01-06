set1 = {1,2,2,2,3,3,3,4,4,5,5,5,5,5,5}
print(set1)

set1.add(6)
print(set1)


set2 = {3,4,5,6,7,8}


diff = set1.difference(set2)
print(diff)

symm = set1.symmetric_difference(set2)
print(symm)