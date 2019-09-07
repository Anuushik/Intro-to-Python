import sys

a = str(sys.argv[1:])

print('# of USA:', a.find("USA"))
print('# of arguments:', len(sys.argv[1:]))
print("The text is: ", a)
print("Final text: ", a.replace("USA","Armenia"))

#import argparse

#parser = argparse.ArgumentParser()

#parser.add_argument( "text",  help = "Just a text", type= str)

#args = parser.parse_args()

#print('Number of "USA" in the text is: ', args.text.find("USA"))
#print('the text is: ', args.text )
