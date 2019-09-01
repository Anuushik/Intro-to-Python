t2 = (5, 2 ,"A", 7, 9)
print("t2: ", t2)
lst = list(t2)
lst[4] = 'hello'
t2 = tuple(lst)
print("final: ", t2)
