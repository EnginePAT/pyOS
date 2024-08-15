import time
import os
from getpass import getpass
from tqdm import tqdm
import sys, random
import boot_menu

running = True
update_size = round(random.uniform(0.20, 100.00))
update_len = 1000
if update_size >= 5:
	update_len == 1000

os.system('clear')
def progressBar(count_value, total, suffix=''):
    bar_length = 100
    filled_up_Length = int(round(bar_length* count_value / float(total)))
    percentage = round(100.0 * count_value/float(total),1)
    bar = '#' * filled_up_Length + '.' * (bar_length - filled_up_Length)
    sys.stdout.write('[%s] %s%s ...%s\r' %(bar, percentage, '%', suffix))
    sys.stdout.flush()
#for i in range(11):
    #time.sleep(random.random())
    #progressBar(i,10)
#print('Complete.')
#time.sleep(1)

# functions
def reboot():
	print("reboot...")
	os.system('clear')
	time.sleep(4)
	login()
	clear()
	print("pyOS v2024.01 lts\n")

def root():
	while running:
		root = input("C:/User/pyOS@root> ")

		if root == 'exit':
			exit()
		else:
			print(f"pyos: command not found: {root}")

def clear():
	os.system('clear')

def mkdir():
	mkdir = input("> ")
	if mkdir == 'Desktop':
		print("Cannot Make Folder")
	elif mkdir == 'Documents':
		print("Cannot Make Folder")
	elif mkdir == 'Downloads':
		print("Cannot Make Folder")
	else:
		os.mkdir(f'file-sys/home/{mkdir}')

def rmdir():
	rmdir = input("> ")
	if rmdir == 'Desktop':
		print("Cannot Remove Folder")
	elif rmdir == 'Documents':
		print("Cannot Remove Folder")
	elif rmdir == 'Downloads':
		print("Cannot Remove Folder")
	else:
		os.rmdir(f'file-sys/home/{rmdir}')

def cd():
	cd = input("> ")
	os.chdir(f'file-sys/home/{cd}')

def update():
	print("scanning for packages")
	time.sleep(random.random())
	print("found packages")
	time.sleep(random.random())
	print("unpacking")
	time.sleep(random.random())
	print("installing")
	time.sleep(random.random())
	print("err: could not find package libsq==4.42")
	time.sleep(random.random())
	print("found: python3.12")
	time.sleep(random.random())
	print("found: gcc")
	time.sleep(random.random())
	print("found: g++")
	time.sleep(random.random())
	print("found: gsl")
	time.sleep(random.random())
	print("found: pyos-kernel-camera-drivers")
	time.sleep(random.random())
	print("found: pyos-kernel-drivers")
	time.sleep(random.random())
	print("found: kernel-update")
	time.sleep(random.random())
	print("found: pyos update 2024.01")
	time.sleep(random.random())
	print(f"update will take up {update_size} Mib")
	time.sleep(random.random())
	print("installing...")
	time.sleep(random.random())
	print("unpacking...")
	time.sleep(random.random())
	print("installing")
	time.sleep(random.random())
	for i in tqdm (range (update_len), 
	    desc="Loading...", 
	    ascii=False, ncols=75):
		time.sleep(0.01)
	     
	print("Complete.")

def create_user():
	while running:
		createUSER = input("Username > ")

		if createUSER == '':
			print("please put in a username")
		else:
			continue

		createUSER_PASS = input("Password > ")

		if createUSER_PASS == '':
			check = input(f'are you sure you dont want a password for the user {createUSER} [Y/n]')
			if check == 'y' or check == 'Y':
				createUSER_PASS
			else:
				print('Continue...')
				break

def login():
	clear()
	print("\n\nLogin\n")
	while running:
		login_user = input("Username > ")
		if login_user == 'pyos':
			break
		else:
			print("err 404: could not find user " + login_user)
	while running:
		login_pass = getpass("Password > ")
		if login_pass == 'pyos':
			break
		else:
			print("incorrect password for " + login_user)
			clear()

def sudo():
	print("looking for sudo permissions (which may require your password)")
	while running:
		sudo = getpass("Password > ")

		if sudo == 'pyos':
			break
		else:
			print("incorrect password. please try again")

clear()

print("Welcome to pyOS")
print("""
		[1] Create User > Currently Unavailable
		[2] Login
		[3] EXIT
	""")

while running:
	startup = input("> ")

	if startup == '1':
		create_user()
	elif startup == '2':
		login()
		break;
	elif startup == '3':
		exit()
	else:
		print("Invalid Input...")

clear()
print("pyOS v2024.01 lts\n")

while running:
	cmd = input("C:/Users/pyOS> ")

	if cmd == '':
		pass
	elif cmd == 'shutdown':
		print("shutdown...")
		time.sleep(2)
		clear()
		break
	elif cmd == 'reboot':
		reboot()
	elif cmd == 'sudo apt-get update':
		sudo()
		update()
	elif cmd == 'clear':
		clear()
		print("pyOS v2024.01 lts\n")
	elif cmd == 'mkdir':
		mkdir()
	elif cmd == 'rmdir':
		rmdir()
	elif cmd == 'rm':
		rm = input('> ')
		try: os.remove(f'file-sys/home/{rm}')
		except FileNotFoundError: print(f'err: file not found {rm}')
	elif cmd == 'ls':
		print(os.listdir(f'file-sys/home/'))
	elif cmd == 'sudo su':
		sudo()
		root()
	elif cmd == 'cd':
		cd()
	elif cmd == 'touch':
		touch = input("> ")
		touch_file_extension = input('extension> ')
		with open(f'file-sys/home/{touch}{touch_file_extension}', "w") as fp:
			pass
	elif cmd == 'echo':
		echo = input('> ')
		print(echo)
	else:
		print(f'pyos: command not found: {cmd}')
