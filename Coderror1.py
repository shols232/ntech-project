user_details = {}
container = []

def main():
	def randomString(stringLength=5):
		import random
		import string
		letters= string.ascii_lowercase
		return ''.join(random.sample(letters,stringLength))

	fname = input("Enter your first name: ")
	lname = input("Enter your lastname: ")
	email = input("Enter your email address: ")

	user_password = (fname[0:2] + lname[-2:] + randomString(5))
	print ("We suggested this password:", user_password)
	while True:
		User_choice = input("Are you ok with this suggested password ? Enter : Yes or No ").lower()
		if User_choice == 'yes':
			break
		elif User_choice =='no':
			user_password= input ("please enter your desired password")
			while len(user_password) < 7:
				print("Please enter a passwors that is greater than 7 characters")
				user_password=input(" password that is greater than 7: TRY AGAIN: ")
				break
			break
		else:
			continue
	user_details = {
		'firstname': fname,
		'lastname': lname,
		'E-mail': email,
		'password': user_password
	}
	container.append(user_details)
	restart_bool = True
	while restart_bool:
		restart =input ("Do you want to register a new user : Enter yes or No:\n ").lower()
		if restart =='yes':
			main()
		elif restart == 'no':
			print ("Your Account have been created successfully \n Below are your details")
			restart_bool=False
		else:
			continue
	print(container)
	exit()

main()
