import argparse

parser = argparse.ArgumentParser()

parser.add_argument( "-text",  help = "Number of symbols",type= str)
parser.add_argument("-word1", help = "First word", type=str)
parser.add_argument("-word2", help="Second word", type=str)

args = parser.parse_args()

if args.text:
   print('The old text is: ', args.text)
if args.word1:
   print("First word: ", args.word1)
if args.word2:
   print("Second word: ", args.word2)
   print("Final: ", args.text.replace(args.word1, args.word2))
