import argparse


tax = 0.09

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('no_tip', type=int, help='Display total cost without tips')
parser.add_argument('-f', '--fair', action='store_true', help='Plus 10% tips')
parser.add_argument('-g', '--great', type=int, help='Give 15% ~ 20% tips')
args = parser.parse_args()

total = args.no_tip*(1+tax)

if args.fair:
	total = args.no_tip*(1+tax+0.10)
elif args.great >= 0:
	total = args.no_tip*(1+tax+args.great/100.0)

print('Total: $' + str(total))