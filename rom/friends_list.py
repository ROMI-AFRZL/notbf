#!usr/bin/python2.7
# coding=utf-8

import os, re, sys, json
from bs4 import BeautifulSoup as parser
from datetime import datetime

def main(self, cookie, url, config):
	id = []
	flist = url+'/friends/center/friends/'
	output = 'dump/friends_list.json'
	print('')
	while True:
		try:
			response = config.httpRequest(flist, cookie).encode('utf-8')
			html = parser(response, 'html.parser')
			for x in html.find_all(style='vertical-align: middle'):
				find = x.find('a')
				if '+' in str(find) or find == None:
					continue
				else:
					full_name = str(find.text.encode('utf-8'))
					if '/?uid=' in str(find):
						uid = re.findall('/\?uid=(.*?)&',find['href'])
					else:
						uid = re.findall('/(.*?)\?fref=',find['href'])
					if len(uid) == 1:
						id.append({'uid': uid[0], 'name': full_name})
					sys.stdout.write("\r\033[0;95m\xe2\x80\xa2 \033[0;91m->\033[0;93m %s                                        \r\n\033[0;95m\xe2\x80\xa2 \033[0;92m%s\033[0;91m [\033[0;93m%s\033[0;91m] \033[0;93mSedang proses dump ! "%(
						full_name, datetime.now().strftime('%H:%M:%S'), len(id)
					)); sys.stdout.flush()
			if 'Lihat selengkapnya' in str(html):
				flist = url+html.find('a', string='Lihat selengkapnya')['href']
			else: break
		except KeyboardInterrupt:
			print('\n\033[0;95m\xe2\x80\xa2 \033[0;91mKeyboard Interrupt error, berhenti!\033[0m')
			break
	try:
		for filename in os.listdir('dump'):
			os.remove('dump/'+filename)
	except: pass
	print('\n\033[0;95m\xe2\x80\xa2 \033[0;97mOutput \033[0;91m:\033[0;93m '+output)
	save = open(output, 'w')
	save.write(json.dumps(id))
	save.close()
