list1 = ["al", "abc", "xyz", "as", "aba","1221"]
print(list1)
L2 = [x for x in range(len(list1)) if  x>2 ] #-?
L3= [ word for word in list1 if word[0]==word[-1]]
print(L2)
print(L3)



