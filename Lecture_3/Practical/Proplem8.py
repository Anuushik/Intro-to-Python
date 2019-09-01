import sys
set1 = {2, "l",3}
print ('set1: ', set1)
set1.update(sys.argv[1:])
print('final set: ', set1)


