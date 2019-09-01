#import sys
#dict1 = {'key1': 1, 'key2': 2, 'key3': 3}
#print('before: ', dict1 )
#dict1[str(sys.argv[1])]= str(sys.argv[2])
#print('after: ', dict1 )

import argparse
dict1 = {'key1': 1, 'key2': 2, 'key3': 3}
print('before: ', dict1)
parser = argparse.ArgumentParser()
parser.add_argument('key4', type = str)
parser.add_argument('value4', type = str)
args = parser.parse_args()
dict1[args.key4] = args.value4
print('after: ', dict1)
