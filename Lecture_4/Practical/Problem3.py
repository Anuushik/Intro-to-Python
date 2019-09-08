age = int(input("Please enter your age: "))
name = str(input("Please eneter your name: "))
password = input("Enter a password: ")
if name == "Batman":
    print("Welcome Mr. Batman!")
elif age<16:
   print("Dear %s, you are too young" %name)
elif "*" and "&" not in password:
       input("Enter a strong password: ") 
print ("Thank you %s! you are registered." %name) 