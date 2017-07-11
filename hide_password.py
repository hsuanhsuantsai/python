import getpass

# Self-defined verification function
def check(user, passwd):
	if user == 'Homer' and passwd == 'YOLO':
		return True
	return False

user = raw_input("Enter username: ")

try:
	passwd = getpass.getpass()
except Exception as e:
	print(e)

if check(user, passwd):
   print('Correct!')
else:
   print('Wrong!')