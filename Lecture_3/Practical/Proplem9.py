import argparse
parser = argparse.ArgumentParser()
parser.add_argument('set2', help = "list of numbers", type = str)
set2 = {2,"A",3}
args = parser.parse_args()
set2.remove(args.set2)
print('set2: ', set2, )


