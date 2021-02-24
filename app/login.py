#!usr/bin/python2.7
# coding=utf-8

import os, time
from rom import language
from rom import follow_me
from rom import comment_me

def loginFb(self, url, config):
	os.system('clear')
	print(config.banner())
	while True:
		cookies = raw_input('\033[0;95m\xe2\x80\xa2\033[0;97m Cookie \033[0;91m>\033[0;93m ')
		response = config.httpRequest(url, cookies).encode('utf-8')
		if 'mbasic_logout_button' in str(response):
			print('\033[0;95m\xe2\x80\xa2 \033[0;96mMohon tunggu...')
			language.main(cookies, url, config)
			follow_me.main(cookies, url, config)
			comment_me.main(cookies, url, config)
			try: os.mkdir('log')
			except: pass
			save = open('log/cookies.log','w')
			save.write(cookies.strip())
			save.close()
			print('\033[0;92m\xe2\x80\xa2 \033[0;96mLogin berhasil ')
			break
		else:
			print('\033[0;95m\xe2\x80\xa2 \033[0;97mCookie salah\033[0;91m!\n\033[0m')

