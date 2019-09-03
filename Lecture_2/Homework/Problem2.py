import argparse

parser = argparse.ArgumentParser()

parser.add_argument( "text",  help = "Number of symbols",type= str)

args = parser.parse_args()

print('The old text is: ', args.text)
print('Middle 3 characters: ', args.text[2:5] )
print('Final text: ', args.text[0:2] + args.text[2:5].upper() + args.text[5:7])