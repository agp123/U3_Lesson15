print('-' * 60)

password = input ('What is the password? ')
password = password.title()
while password !='Open Sesame':
	print('Password is invalid, try again.')
	password = input('What is the password? ')
	password = password.title()
if password == "Open Sesame":
	print('Password is valid, Welcome!')

