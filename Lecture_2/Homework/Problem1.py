import datetime
import argparse
import time
tday = datetime.datetime.now()

parser = argparse.ArgumentParser()

#parser.add_argument("num_d", help="display number of days", type=int)
parser.add_argument("num_y", help="display number of years", type=int)

args = parser.parse_args()

#day = datetime.timedelta(days = args.num_d)
#year = datetime.timedelta(years = args.num_y)

year = datetime.timedelta(years = 2)


print ("Local current time :", tday)

#print("After %s days" % (args.num_d), tday + day )
print("After %s years" % (args.num_y), tday + year  )


