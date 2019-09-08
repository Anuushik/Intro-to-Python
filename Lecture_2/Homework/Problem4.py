import sys

a = str(sys.argv[1:])

print('# of USA:', a.upper().count("USA"))
print("The text is: ", a)
print("Final text: ", a.replace("usa","Armenia"). replace("USA","Armenia"))

