import os
os.system('tput setaf 1')
print("WELCOME TO LINUX MENU DRIVEN")	
while(1):
	os.system('tput setaf 2')
	print('Select the option')
	print("1.Display calender","2.Display Date","3.Display the Files","4.Create Directory",sep='\n')
	print("5.Create File","6.Delete File","7.Delete Folder","8.exit",sep='\n')
	n=int(input())
	os.system('clear')
	os.system('tput setaf 1')
	if(n==1):
		os.system('cal')
	elif(n==2):
		os.system('date')
	elif(n==3):
		os.system('ls')
	elif(n==4):
		t=input("Enter the name for creating Directory:\n")
		t='mkdir '+t
		os.system(t)
	elif(n==5):
		t=input("Enter the name for creating File:\n")
		t='touch '+t
		os.system(t)
	elif(n==6):
		t=input("Enter the name for Deleting Directory:\n")
		t='rm -r '+t
		os.system(t)
	elif(n==7):
		t=input("Enter the name for Deleting File:\n")
		t='rm -r '+t
		os.system(t)
	elif(n==8):
		exit()
			

		
