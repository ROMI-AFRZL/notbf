#!usr/bin/python2.7
# coding=utf-8

import os, re, sys, json
from bs4 import BeautifulSoup as parser
from datetime import datetime

def main(self, cookie, url, config):
	ask = raw_input('\n\033[0;95m\xe2\x80\xa2 \033[0;96mMasukan nama \033[0;91m:\033[0;93m ')
	if ask.strip() == '':
		exit("\n\033[0;95m\xe2\x80\xa2 \033[0;97mTidak boleh kosong.\033[0m")
	try:
		max = int(raw_input('\033[0;97mBerapa banyak? \033[0;97m[\033[0;93mMax\033[0;91m:\033[0;93m2000\033[0;97m]\033[0;91m :\033[0;93m '))
	except ValueError:
		exit("\n\033[0;95m\xe2\x80\xa2 \033[0;91mIsi Yg Benar.\033[0m")
	if max == 0:
		exit("\n\033[0;95m\xe2\x80\xa2 \033[0;91mTidak boleh kosong.\033[0m")

	url_search = url+'/search/people/?q='+ask

	statusStop = False
	output = 'dump/'+ask.replace(' ', '_')+'.json'.strip()
	id = []
	print('')

	while True:
		try:
			response = config.httpRequest(url_search, cookie).encode('utf-8')
			html = parser(response, 'html.parser')
			find = html.find_all('a')
			for i in find:
				name = i.find('div')
				if '+' in str(name) or name == None:
					continue
				else:
					full_name = str(name.text.encode('utf-8'))
					if 'profile.php?id=' in str(i):
						uid = re.findall(r'\?id=(.*?)&', str(i))
					else:
						uid = re.findall('/(.*?)\?refid=', str(i))
					if len(uid) == 1:
						id.append({'uid': uid[0], 'name': full_name})
					sys.stdout.write("\r\033[0;95m\xe2\x80\xa2 \033[0;91m->\033[0;93m %s                                        \r\n\033[0;95m\xe2\x80\xa2 \033[0;92m%s\033[0;91m [\033[0;93m%s\033[0;91m] \033[0;93mSedang proses dump !"%(
						full_name, datetime.now().strftime('%H:%M:%S'), len(id)
					)); sys.stdout.flush()
					if len(id) == max or len(id) > max:
						statusStop = True
						break
			if statusStop == False:
				if 'Lihat Hasil Selanjutnya' in str(html):
					url_search = html.find('a', string='Lihat Hasil Selanjutnya')['href']
				else: break
			else: break
		except KeyboardInterrupt:
			print('\n\033[0;95m\xe2\x80\xa2 \033[0;91mKey Interrupt, berhenti!!\033[0m')
			break
	try:
		for filename in os.listdir('dump'):
			os.remove('dump/'+filename)
	except: pass
	print('\n\033[0;95m\xe2\x80\xa2 \033[0;97mOutput \033[0;91m:\033[0;93m '+output)
	save = open(output, 'w')
	save.write(json.dumps(id))
	save.close()
