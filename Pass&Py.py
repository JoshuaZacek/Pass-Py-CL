#=========================================PASS&PY CL=========================================
#=========================================ERROR CATCHING=========================================
try:
#=========================================IMPORTS=========================================
	import sys #USED FOR SYSTEM EXITS
	import csv #USED FOR READING/WRITING TO .CSV FILES
	import os #USED TO INTERACT WITH THE OS
	import random #USED FOR RANDON NUMBERS
	import smtplib #USED FOR SENDING EMAIl
	import socket #USED FOR EMAIL ERROR HANDLING
	from smtplib import SMTP, SMTPException, SMTPAuthenticationError #USED FOR EMAIL ERROR HANDLING
	from socket import gethostbyname, gaierror #USED FOR EMAIL ERROR HANDLING
	import platform #USED TO IDENTIFY CLINET OS
	import rlcompleter #USED FOR COMMAND LINE
	if platform.system() == "Darwin" or platform.system() == "Linux":
		import readline #USED FOR COMMAND LINE
	import re #USED FOR VALIDATING EMAIL
	import hashlib #USED FOR PASSWORD HASHING
	import base64 #UESD FOR ENCODING HASHED PASSWORDS IN BASE64
#=========================================STARTUP=========================================
	if sys.version_info<(3,0,0):
		print("ERROR: THIS PROGRAM DOES NOT SUPPORT VERSION OF PYTHON BELOW 3")
		sys.exit()
	elif (3,0,0) <= sys.version_info <= (3,8,0):
		while True:
 			desicion=input("WARNING: THIS PROGRAM MAY NOT RUN CORRECTLY ON OLDER VERSIONS OF PYTHON. ARE YOU SURE YOU WANT TO CONTINUE? (Y/N) ")
 			if desicion.lower() == "n":
 				sys.exit()
 			elif desicion.lower() == "y":
 				break
	clversion="Beta 5"
	clbuild="2020-ZF-AG-A"
	cldirectory = os.path.dirname(os.path.realpath(__file__))
	print("Welcome to Pass&Py CL "+clversion+" Build "+clbuild)
#=========================================DOES DATABASE EXIST?=========================================
	try:
		f = open(os.path.join(cldirectory,'passandpy.csv'))
		f.close()
	except FileNotFoundError:
		header = ['Username', 'Password', 'Recovery Key', 'Firstname', 'Surname', 'Email', 'Phone', '2FA', 'Banned', 'Locked', 'Passcode','2FA length','Passcode Length','Ban Note','Failed Attempts','Admin','Verified?','.\r\n']
		with open(os.path.join(cldirectory,'passandpy.csv'), 'w') as database_file:
			database_writer = csv.writer(database_file)
			database_writer.writerow(header)
		print("WARNING: NO DATABASE WAS FOUND, SO A NEW ONE WAS CREATED.")
#=========================================FUNCTIONS=========================================
#=========================================CLOUMNS=========================================
	def columns():
		passandpydatabase = []
		csvfileread = [line for line in csv.reader(open(os.path.join(cldirectory,'passandpy.csv'),'r'))]
		for line in csvfileread:
			if line == []:
				continue
			passandpydatabase.append(line)
		global column0
		global column1
		global column2
		global column3
		global column4
		global column5
		global column6
		global column7
		global column8
		global column9
		global column10
		global column11
		global column12
		global column13
		global column14
		global column15
		global column16
		column0 = [x[0] for x in passandpydatabase]
		column1 = [x[1] for x in passandpydatabase]
		column2 = [x[2] for x in passandpydatabase]
		column3 = [x[3] for x in passandpydatabase]
		column4 = [x[4] for x in passandpydatabase]
		column5 = [x[5] for x in passandpydatabase]
		column6 = [x[6] for x in passandpydatabase]
		column7 = [x[7] for x in passandpydatabase]
		column8 = [x[8] for x in passandpydatabase]
		column9 = [x[9] for x in passandpydatabase]
		column10 = [x[10] for x in passandpydatabase]
		column11 = [x[11] for x in passandpydatabase]
		column12 = [x[12] for x in passandpydatabase]
		column13 = [x[13] for x in passandpydatabase]
		column14 = [x[14] for x in passandpydatabase]
		column15 = [x[15] for x in passandpydatabase]
		column16 = [x[16] for x in passandpydatabase]
#=========================================NUMBER GENERATOR=========================================
	def numbergenerate(length):
		global number
		number=random.randrange(10**(length-1), (10**length)-1)
#=========================================EMAIL=========================================
	def sendemail(body,subject,sendto):
		smtp_port=587
		smtp_server='smtp.gmail.com'
		sender_email="passandpy@gmail.com"
		sender_password="joshjosh22"
		with smtplib.SMTP(smtp_server, smtp_port) as smtp:
			smtp.ehlo()
			smtp.starttls()
			smtp.ehlo()
			smtp.login(sender_email, sender_password)
			msg = f'Subject: {subject}\n\n{body}'
			smtp.sendmail(sender_email, sendto, msg)
#=========================================COUNTER=========================================
	failedattempts=0
	def counter():
		columns()
		global failedattempts
		if failedattempts >= 9:
			for k in range(len(column0)):
				if username == column0[k]:
					csvfilemodified = []
					csvfileread = [line for line in csv.reader(open(os.path.join(cldirectory,'passandpy.csv'),'r'))]
					for line in csvfileread:
						if line == []:
							continue
						csvfilemodified.append(line)
					csvfilemodified[k][9] = 1
					csv.writer(open(os.path.join(cldirectory,'passandpy.csv'), 'w')).writerows(csvfilemodified)		
		else:
			if username in column0:
				for k in range(len(column0)):
					if username == column0[k]:
						failedattempts = int(column14[k])
						failedattempts = failedattempts + 1
						csvfilemodified = []
						csvfileread = [line for line in csv.reader(open(os.path.join(cldirectory,'passandpy.csv'),'r'))]
						for line in csvfileread:
							if line == []:
								continue
							csvfilemodified.append(line)
						csvfilemodified[k][14] = failedattempts
						csv.writer(open(os.path.join(cldirectory,'passandpy.csv'), 'w')).writerows(csvfilemodified)
					else:
						pass
#=========================================CSV CELL EDITER=========================================
	def information_modification(column,value,letter):
		csvfilemodified = []
		csvfileread = [line for line in csv.reader(open(os.path.join(cldirectory,'passandpy.csv'),'r'))]
		for line in csvfileread:
			if line == []:
				continue
			csvfilemodified.append(line)
		csvfilemodified[letter][column] = value
		csv.writer(open(os.path.join(cldirectory,'passandpy.csv'), 'w')).writerows(csvfilemodified)
	def newpasscode(state):
		while True:
			passcodelength=input("CHOOSE PASSCODE LENGTH (4 OR 6) ")
			try:
				int(passcodelength)
				if passcodelength == "4" or passcodelength == "6":
					passcode=input("ENTER YOUR NEW PASSCODE. ")
					if passcode == "0000":
						print("ERROR: PASSCODE IS INSCEURE.")
					else:
						if int(len(passcode)) > int(passcodelength):
							print("ERROR: YOUR PASSCODE MUST BE "+str(passcodelength)+" DIGITS LONG.")
						else:
							passcodeconfirm=input("CONFIRM YOUR NEW PASSCODE. ")
							if int(len(passcodeconfirm)) > int(passcodelength):
								print("ERROR: YOUR PASSCODE MUST BE "+str(passcodelength)+" DIGITS LONG.")
							else:
								if passcodeconfirm == passcode:
									information_modification(12,passcodelength,k)
									information_modification(10,passcodeconfirm,k)
									if state == "enable":
										print("PASSCODE ENABLED SUCCESSFULLY.")
									elif state == "modified":
										print("PASSCODE MODIFIED")
									break
								else:
									print("ERROR: PASSCODES DON'T MATCH")
				else:
					print("ERROR: NOT A VALID OPTION. CHOOSE BETWEEN 4 OR 6.")
			except ValueError:
				print("ERROR: NOT AN INTERGER")
	def newpassword():
		newpassword=input("ENTER NEW PASSWORD: ")
		confirmnewpassword=input("CONFRIM NEW PASSWORD: ")
		if newpassword == confirmnewpassword:
			confirmnewpassword=hashlib.pbkdf2_hmac('sha256', confirmnewpassword.encode('utf-8'), b'\xff\x15\t\xcfx4H\x9a\xa0B.I\xcb\xae\x96\xd7\xa3x\xcc\xc9\xedd\xc8{I\x0b>\x9b43[\xbd', 100000)
			confirmnewpassword=base64.b64encode(confirmnewpassword)
			information_modification(1,confirmnewpassword,k)
			print("PASSWORD MODIFIED")
		else:
			print("ERROR: PASSWORDS DO NOT MATCH")
#=========================================COMMANDS=========================================
	validcommands = ["/register","/login","/logout","/exit","/about","/admin","/help","/account","/modify","/settings","/forgot"] #list of valid commands
	programstatus = "notloggedin"
	while True:
		rawcommand=input()
		rawcommand=rawcommand.split(" ")
		command = rawcommand[0]
		command = command.lower()
		if command in validcommands:
#=========================================EXIT=========================================
			if command=="/exit":
				sys.exit()
#=========================================COMMAND HELP=========================================
			if command=="/help":
				if programstatus == "notloggedin":
					print("-- /login [username/email] [password]\n\n-- /register [firstname] [surname] [username] [email] [phone] [password] [confirmpassword]\n\n-- /exit\n\n-- /about")
				if programstatus == "loggedin":
					print("-- /logout\n\n-- /modify [password/email/phone/email/passcode/accountkey]\n\n-- /settings [2fa/passcode] [enable/disable]\n\n-- /account [delete/verify]")
				if programstatus == "loggedinadmin":
					print("-- /logout\n\n-- /modify [password/email/phone/email/passcode/accountkey]\n\n-- /settings [2fa/passcode] [enable/disable]\n\n-- /account [delete/verify]\n\n-- /admin [disableaccount/enableaccount/restrictaccount/removerestrictions] [username] \n\n-- /exit")
#=========================================ABOUT=========================================
			if command=="/about":
				print("Pass&Py CL "+clversion+"\nBuild "+clbuild+"\nMade by Joshua Zacek\nCopyright 2020")
#=========================================LOGOUT=========================================
			if command=="/logout":
				if programstatus == "notloggedin":
					print("ERROR: YOU ARE NOT LOGGED IN")
				else:
					programstatus="notloggedin"
					print("YOU HAVE BEEN LOGGED OUT")
#=========================================LOGIN=========================================
			if command=="/login":
				if programstatus == "loggedin" or programstatus == "loggedinadmin":
					print("ERROR: YOU ARE ALREADY LOGGED IN")
				else:
					try:
						columns()
						username=rawcommand[1]
						password=rawcommand[2]
						password=base64.b64encode(hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), b'\xff\x15\t\xcfx4H\x9a\xa0B.I\xcb\xae\x96\xd7\xa3x\xcc\xc9\xedd\xc8{I\x0b>\x9b43[\xbd', 100000))
						if len(rawcommand) > 3:
							print("ERROR: TOO MANY PARAMETERS")
						else:
							if (username in column0) or (username in column5):
								for k in range(len(column0)):
									if column0[k] == username and column1[k] == "b'"+password.decode('utf-8')+"'" or column5[k] == username and column1[k] == "b'"+password.decode('utf-8')+"'":
										username=column0[k]
										if column0[k] == username and column8[k] == "1":
											print("THIS ACCOUNT HAS BEEN BANNED. YOU HAVE BEEN LOGGED OUT.")
											programstatus="notloggedin"
											break
										else:
											if column0[k] == username and column9[k] == "1":
												accountkeyfromdatabase=column3[k]
												print("YOUR ACCOUNT IS HAS BEEN SECURITY LOCKED.\nPLEASE ENTER YOUR ACCOUNT KEY.")
												accountkeyfromuser=input()
												if accountkeyfromuser == accountkeyfromdatabase:
													print("YOUR SECURITY LOCK HAVE BEEN LIFTED.")
													information_modification(9,0,k)
												elif accountkeyfromuser.lower() == "/exit":
													sys.exit()
												else:
													information_modification(8,1,k)
													print("ERROR: INCORRECT ACCOUNT KEY\nYOUR ACCOUNT HAS BEEN BANNED.")
												break
											else:
												if column7[k] == "1":
													numbergenerate(int(column11[k]))
													sendemail("Your Two-Factor Authentication code is "+str(number),"[Pass&Py] Two-Factor Authentication",column5[k])
													user2facode=input("A CODE HAS BEEN SENT TO YOUR EMAIL. PLEASE ENTER THE CODE TO LOGIN. ")
													if user2facode == str(number):
														columns()
														print("YOU ARE LOGGED IN AS: "+username)
														if column15[k] == "1":
															programstatus="loggedinadmin"
															print("THIS ACCOUNT HAS ADMINISTRATIVE PRIVILEGES.")
														else:
															programstatus="loggedin"
														if column16[k] == "0":
															print("NOTICE: YOUR ACCOUNT IS NOT VERIFIED. DO /ACCOUNT VERIFY.")
														information_modification(14,0,k)
														break
													else:
														print("ERROR: TWO-FACTOR AUTHENTICATION FAILED, INCORRECT CODE. YOU HAVE BEEN LOGGED OUT.")
														programstatus="notloggedin"
														break
												else:
													if column10[k] != "0":
														userpasscode=input("ENTER PASSCODE: ")
														if userpasscode!=column10[k]:
															print("ERROR: LOGIN FAILED, INCORRECT PASSCODE. YOU HAVE BEEN LOGGED OUT.")
															break
													columns()
													print("YOU ARE LOGGED IN AS: "+username)
													if column15[k] == "1":
														programstatus="loggedinadmin"
														print("THIS ACCOUNT HAS ADMINISTRATIVE PRIVILEGES.")
													else:
														programstatus="loggedin"
													if column16[k] == "0":
														print("NOTICE: YOUR ACCOUNT IS NOT VERIFIED. DO /ACCOUNT VERIFY.")
													information_modification(14,0,k)
													break
								else:
									print("ERROR: INCORRECT PASSWORD")
									counter()
							else:
								print("ERROR: ACCOUNT DOESN'T EXIST")
					except IndexError:
						print("ERROR: MISSING PARAMETERS")
#=========================================ACCOUNT COMMANDS=========================================
			if command=="/settings":
				if programstatus == "loggedin" or programstatus == "loggedinadmin":
					try:
						setting=rawcommand[1].lower()
						enableordisable=rawcommand[2].lower()
						if len(rawcommand) > 3:
							print("ERROR: TOO MANY PARAMETERS")
						else:
							columns()
							if setting == "2fa":
								if enableordisable == "enable":
									if column16[k] == "0":
										print("ERROR: YOU MUST VERIFY YOUR ACCOUNT BEFORE YOU USE TWO-FACTOR AUTHENTICATION")
									else:
										if column7[k] == "1":
											print("ERROR: TWO-FACTOR AUTHENTICATION IS ALREADY ENABLED.")
										else:
											while True:
												length2fa=input("ENTER 2FA CODE LENGTH (4-10)")
												try:
													length2fa=int(length2fa)
													if 4 <= length2fa <= 10:
														information_modification(7,1,k)
														information_modification(11,length2fa,k)
														print("TWO-FACTOR AUTHENTICATION ENABLED")
														break
													else:
														print("ERROR: ENTER AN INTERGER BETWEEN 4 AND 10. ")
												except ValueError:
													print("ERROR: NOT A VALID INTERGER.")											
								elif enableordisable == "disable":
									if column7[k] == "0":
										print("ERROR: TWO-FACTOR AUTHENTICATION IS ALREADY DISABLED.")
									else:
										information_modification(7,0,k)
										print("TWO-FACTOR AUTHENTICATION DISABLED")
								else:
									print("ERROR: INVALID PARAMETERS")
							elif setting == "passcode":
								if enableordisable == "enable":
									if column10[k] == "0":
										newpasscode("enable")
									else:
										print("ERROR: PASSCODE IS ALREADY ENABLED.")
								elif enableordisable == "disable":
									if column10[k] == "0":
										print("ERROR: PASSCODE IS ALREADY DISABLED")
									else:
										information_modification(10,0,k)
										print("PASSCODE DISABLED SUCCESSFULLY.")
							else:
								print("ERROR: INVALID PARAMETER")
					except IndexError:
						print("ERROR: MISSING PARAMETERS")
				else:
					print("ERROR: YOU MUST BE LOGGED IN TO USE THIS COMMAND")
			if command=="/account":
				if programstatus == "notloggedin":
					print("ERROR: YOU MUST BE LOGGED IN TO USE THIS COMMAND.")
				else:
					try:
						verifyordelete=rawcommand[1].lower()
						if len(rawcommand) > 2:
							print("ERROR: TOO MANY PARAMETERS")
						else:
							if verifyordelete == "verify":
								numbergenerate(8)
								number = str(number)
								sendemail("Your account verification code is "+number,"[Pass&Py] Verify Your Account",column5[k])
								userverifycode=input("ENTER THE CODE SENT TO YOUR EMAIL.")
								if userverifycode == number:
									print("YOUR ACCOUNT IS NOW VERIFIED.")
									information_modification(16,1,k)
								else:
									print("ERROR: VERIFICTION FAILED, INCORRECT CODE")
							elif verifyordelete == "delete":
								while True:
									option = input("WARNING: ARE YOU SURE YOU WANT TO PROCEED? THIS CAN NOT BE REVERSED. (Y/N)").lower()
									if option == "y":
										information_modification(8,1,k)
										programstatus="notloggedin"
										print("YOU HAVE DELETED YOUR ACCOUNT. YOU HAVE BEEN LOGGED OUT.")
										break
									elif option == "n":
										print("OPERATION CANCELLED.")
										break
									else:
										print("PLEASE ENTER Y (YES) OR N (NO).")
							else:
								print("ERROR: INVALID PARAMETERS")
					except IndexError:
						print("ERROR: MISSING PARAMETERS")
#=========================================REGISTER=========================================
			if command=="/register":
				if programstatus == "loggedin" or programstatus == "loggedinadmin":
					print("ERROR: LOGOUT BEFORE REGISTERING FOR AN ACCOUNT.")
				else:
					try:
						firstname=rawcommand[1]
						lastname=rawcommand[2]
						username=rawcommand[3]
						email=rawcommand[4]
						phone=rawcommand[5]
						password=rawcommand[6]
						passwordconfirm=rawcommand[7]
#=========================================DATA VALIDATION=========================================
						if len(rawcommand) > 8:
							print("ERROR: TOO MANY PARAMETERS")
						else:
							columns()
							if len(column0) == 1:
								isthisuseradmin=1
							else:
								isthisuseradmin=0
							if username in column0:
								print("ERROR: USERNAME TAKEN")
							else:
								if email in column5:
									print("ERROR: EMAIL LINKED TO ANOTHER ACCOUNT")
								else:
									if phone in column6:
										print("ERROR: PHONE LINKED TO ANOTHER ACCOUNT")
									else:
										if(re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',email)):
											if len(username) >= 20:
												print("ERROR: USERNAME IS TOO LONG")
											else:
												if password == passwordconfirm:
													password=hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), b'\xff\x15\t\xcfx4H\x9a\xa0B.I\xcb\xae\x96\xd7\xa3x\xcc\xc9\xedd\xc8{I\x0b>\x9b43[\xbd', 100000)
													password=base64.b64encode(password)
													numbergenerate(6)
#=========================================ACCOUNT STORAGE=========================================
													accountrow=[username,password,number,firstname,lastname,email,phone,0,0,0,0,0,0,0,0,isthisuseradmin,0,".\r\n"]
													with open(os.path.join(cldirectory,'passandpy.csv'), 'a') as database_file:
														database_writer = csv.writer(database_file)
														database_writer.writerow(accountrow)
													print("YOUR ACCOUNT HAS BEEN SUCCESSFULLY REGISTERED.")
													number = str(number)
													print("YOUR ACCOUNT KEY IS: "+number)
												else:
													print("ERROR: PASSWORDS DO NOT MATCH")
										else:
											print("ERROR: INVALID EMAIL")
												
					except IndexError:
						print("ERROR: MISSING PARAMETERS")
			if command == "/modify":
				try:
					if programstatus == "loggedin" or programstatus == "loggedinadmin":
						modify=rawcommand[1].lower()
						if len(rawcommand) > 2:
							print("ERROR: TOO MANY PARAMETERS")
						else:
							if modify == "email":
								columns()
								currentemail=input("ENTER CURRENT EMAIL: ")
								if currentemail == column5[k]:
									newemail=input("ENTER NEW EMAIL: ")
									if(re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',newemail)):
										information_modification(5,newemail,k)
										information_modification(16,0,k)
										print("EMAIL MODIFIED")
										print("NOTICE: YOUR ACCOUNT IS NOT VERIFIED. DO /ACCOUNT VERIFY.")
									else:
										print("ERROR: INVALID EMAIL.")
								else:
									print("ERROR: THIS IS NOT YOUR CURRENT EMAIL")
							else:
								if modify == "phone":
									newphone=input("ENTER NEW PHONE NUMBER: ")
									information_modification(6, newphone,k)
									print("PHONE NUMBER MODIFIED")
								else:
									if modify == "name":
										firstname=input("ENTER FIRSTNAME: ")
										surname=input("ENTER SURNAME: ")
										information_modification(3, firstname,k)
										information_modification(4, surname,k)
										print("NAME MODIFIED")
									else:
										if modify == "password":
											currentpassword=input("ENTER CURRENT PASSWORD: ")
											currentpassword=base64.b64encode(hashlib.pbkdf2_hmac('sha256', currentpassword.encode('utf-8'), b'\xff\x15\t\xcfx4H\x9a\xa0B.I\xcb\xae\x96\xd7\xa3x\xcc\xc9\xedd\xc8{I\x0b>\x9b43[\xbd', 100000))
											if str(currentpassword) == str(column1[k]):
												newpassword()
											else:
												print("ERROR: THIS IS NOT YOUR CURRENT PASSWORD")
										else:
											if modify=="accountkey":
												numbergenerate(6)
												information_modification(2, number,k)
												print("YOUR NEW ACCOUNT KEY IS: "+str(number))
											else:
												if modify=="passcode":
													if column10[k] == "0":
														print("YOU MUST HAVE PASSCODE ENABLED TO USE THIS COMMAND.")
													else:
														columns()
														currentpasscode=input("ENTER CURRENT PASSCODE: ")
														if currentpasscode == column10[k]:
															newpasscode("modified")
														else:
															print("ERROR: THIS IS NOT YOUR CURRENT PASSCODE")
												else:
													print("ERROR: INVALID PARAMETER")
					else:
						print("ERROR: YOU MUST BE LOGGED IN TO USE THIS COMMAND.")
				except IndexError:
					print("ERROR: MISSING PARAMETERS")
			if command=="/admin":
				if programstatus == "notloggedin":
					print("ERROR: YOU MUST BE LOGGED IN TO USE THIS COMMAND.")
				else:
					columns()
					if username == column0[k] and column15[k] == "1":
						try:
							action = rawcommand[1].lower()
							victim = rawcommand[2]
							if victim == username:
								print("ERROR: YOU CAN NOT EXECUTE ADMIN COMMANDS ON YOURSELF.")
							else:
								if action == "ban":
									if victim in column0:
										for a in range(len(column0)):
											if victim == column0[a]:
												if column8[a] == "0":
													if column15[a] == "1":
														print("ERROR: THIS USER IS AN ADMIN")
													else:
														information_modification(8,1,a)
														print("SUCCESSFULLY BANNED ACCOUNT")
												else:
													print("ERROR: THIS ACCOUNT IS ALREADY BANNED")
										else:
											pass
									else:
										print("ERROR: USERNAME DOESN'T EXIST")
								elif action == "unban":
									if victim in column0:
										for a in range(len(column0)):
											if victim == column0[a]:
												if column8[a] == "1":
													information_modification(8,0,a)
													print("SUCCESSFULLY UNBANNED ACCOUNT")
												else:
													print("ERROR: THIS ACCOUNT IS ALREADY UNBANNED")
										else:
											pass
									else:
										print("ERROR: USERNAME DOESN'T EXIST")
								elif action == "lock":
									if victim in column0:
										for a in range(len(column0)):
											if column9[a] == "0":
												if victim == column0[a]:
													information_modification(9,1,a)
													print("SUCCESSFULLY LOCKED ACCOUNT")
											else:
												print("ERROR: THIS ACCOUNT IS ALREADY LOCKED")
									else:
										print("ERROR: USERNAME DOESN'T EXIST")
								elif action == "unlock":
									if victim in column0:
										for a in range(len(column0)):
											if victim == column0[a]:
												if column9[a] == "1":
													information_modification(9,0,a)
													print("SUCCESSFULLY UNLOCKED ACCOUNT")
												else:
													print("ERROR: THIS ACCOUNT IS ALREADY UNLOCKED")
										else:
											pass
									else:
										print("ERROR: USERNAME DOESN'T EXIST")
								elif action == "grant":
									if victim in column0:
										for a in range(len(column0)):
											if victim == column0[a]:
												if column15[a] == "0":
													information_modification(15,1,a)
													print("SUCCESSFULLY GRANTED ADMINISTRATIVE PRIVILEGES")
												else:
													print("ERROR: THIS ACCOUNT ALREADY HAS ADMINISTRATIVE PRIVILEGES")
										else:
											pass
									else:
										print("ERROR: USERNAME DOESN'T EXIST")
								elif action == "revoke":
									if victim in column0:
										for a in range(len(column0)):
											if victim == column0[a]:
												if column15[a] == "1":
													information_modification(15,0,a)
													print("SUCCESSFULLY REOVKED ADMINISTRATIVE PRIVILEGES")
												else:
													print("ERROR: THIS IS NOT AN ADMINISTRATIVE ACCOUNT")
										else:
											pass
									else:
										print("ERROR: USERNAME DOESN'T EXIST")
								elif action == "status":
									if victim in column0:
										for a in range(len(column0)):
											if victim == column0[a]:
												columns()
												if column9[a] == "0":
													restrictstatus="NOT LOCKED"
												else:
													restrictstatus="LOCKED"
												if column8[a] == "0":
													disablestatus="NOT BANNED"
												else:
													disablestatus="BANNED"
												if column15[a] == "0":
													adminstatus="IS NOT AN ADMIN"
												else:
													adminstatus="IS AN ADMIN"
												print("USER "+victim+" IS "+restrictstatus+", IS "+disablestatus+" AND "+adminstatus+".")
										else:
											pass
									else:
										print("ERROR: USERNAME DOESN'T EXIST")
								else:
									print("ERROR: INVALID PARAMETER")
						except IndexError:
							print("ERROR: MISSING PARAMETERS")
					else:
						print("ERROR: YOU ARE NOT AN ADMIN")
			if command == "/forgot":
				columns()
				if programstatus == "loggedin" or programstatus == "loggedinadmin":
					print("ERROR: YOU NEED TO LOGGED OUT TO USE THIS COMMAND")
				else:
					try:
						username=rawcommand[1]
						if len(rawcommand) > 2:
							print("ERROR: TOO MANY PARAMETERS")
						else:
							if username in column0:
								for k in range(len(column0)):
									if username == column0[k]:
										if column16[k] == "0":
											account_key_by_user=input("ENTER YOUR ACCOUNT KEY: ")
											if account_key_by_user == column2[k]:
												newpassword()
											else:
												print("ERROR: INCORRECT ACCOUNT KEY")
												counter()	
										else:
											numbergenerate(6)
											sendemail('Your Account Temporary Account Key is '+str(number),'[Pass&Py] Temporary Account Key',column5[k])
											number_code_by_user=input("ENTER THE CODE SENT TO YOUR EMAIL: ")
											if number_code_by_user == str(number):
												newpassword()
											else:
												print("ERROR: INCORRECT CODE")
												counter()
							else:
								print("ERROR: USERNAME DOESN'T EXIST")
					except IndexError:
						print("ERROR: MISSING PARAMETERS")
#=========================================INVALID COMMANDS=========================================	
		else:
			if command[:1] == "/":
				print("ERROR: INVALID COMMAND. DO /HELP")
			else:
				print("SYNTAX: COMMANDS BEGIN WITH /")
#=========================================ERROR HANDLING=========================================
except socket.gaierror:
	print("ERROR: FAILED TO CONNECT. HAVE YOU CHANGED SMTP ADDRESS YET?")
except SMTPAuthenticationError:
	print("ERROR: FAILED TO AUTHENTICATE. HAVE YOU CHANGED EMAIL, PASSWORD AND SMTP PORT YET?")
except Exception:
	while True:
		desicion=input("AN UNKNOWN ERROR OCCURED. WOULD YOU LIKE TO SEE ADVANCED INFORMATION? (Y/N)")
		if desicion.lower() == "y":
			raise
		elif desicion.lower() == "n":
			sys.exit()
		else:
			print("SYNTAX: MUST BE Y OR N")
