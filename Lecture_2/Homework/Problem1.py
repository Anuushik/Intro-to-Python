import datetime
import argparse

tday = datetime.datetime.now( )

parser = argparse.ArgumentParser()

parser.add_argument("-num_d", help="display number of days", type = int)
parser.add_argument("-num_y", help="display number of years", type = int)

args = parser.parse_args()

day = datetime.timedelta(days = args.num_d)
year = datetime.timedelta(days = 365 * args.num_y)


print ("Local current time :", tday)

if args.num_d:
    print("After %s days" % (args.num_d), tday + day )
if args.num_y:
    print("After %s years" % (args.num_y), tday + year  )


