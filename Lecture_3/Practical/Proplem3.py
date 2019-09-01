import argparse
parser = argparse.ArgumentParser()
parser.add_argument('list2', help = "list of numbers", type = int)
args = parser.parse_args()
list2 = [args.list2]
print('list2: ', list2, "\n"'# of 2s in list2: ', list2.count(2))
