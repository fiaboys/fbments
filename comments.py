import threading
import time
import os

try:
	import requests
except ImportError:
	os.system('pip install requests')
	
os.system('clear')
notdata = '''

'''
banner = '''
'''

def home():
	os.system('clear')
	print(banner)
	token = input('โทเค็นของคุณ : ')
	response = requests.get(f'https://graph.facebook.com/me?access_token={token}')
	if (response.status_code == 200):
		id = input('ไอดีโพสต์ : ')
		msg = input('ข้อความ : ')
		total = int(input('จำนวน : '))
		type = input('คอมเม้นต์เร็วหรือไม่เร็ว (y,n) : ')
		print()
		if (type == "y" or type == "Y"):
			print('คอมเม้นต์แบบรวดเร็ว !')
			print()
			time.sleep(2)
			
			def api():
				req = requests.post(f'https://graph.facebook.com/{id}/comments?method=post&message={msg}&access_token={token}')
				if (req.status_code == 200):
					print(f' คอมเม้นต์แล้ว')
				else:
					print(' กรุณาตรวจสอบไอดีโพสต์ของคุณ !')
					time.sleep(2)
					home()
			
			for g in range(total):
				threading.Thread(target=api).start()
		else:
			print('คอมเม้นต์แบบช้าๆ !')
			time.sleep(2)
			
			def api():
				req = requests.post(f'https://graph.facebook.com/{id}/comments?method=post&message={msg}&access_token={token}')
				if (req.status_code == 200):
					print(f' คอมเม้นต์แล้ว')
				else:
					print(' กรุณาตรวจสอบไอดีโพสต์ของคุณ !')
					time.sleep(2)
					home()
			for x in range(total):
				api()
	else:
		print()
		print('   โทเค็นของคุณไม่ถูกต้อง กรุณาตรวจสอบและลองใหม่อีกครั้ง !')
		time.sleep(2)
		home()
	
print(notdata)
print()
print('                  กรุณาอ่านเงื่อนไขการใช้งาน')
print()
print(' คำเตือน : สคริปต์ปั๊มเม้นต์มีโอกาศโดนแบน 80% หากโดนแบนทางเราจะไม่รับผิดชอบทุกกรณี หากจะปั้มต้องใช้เฟสสมัครใหม่หรือไม่ใช้งานแล้ว')
print()
print('           ฝากกดติดตามช่อง GENIX SHOP ด้วยนะครับ')
print()
print(' โปรดรอ...')
time.sleep(10)
home()