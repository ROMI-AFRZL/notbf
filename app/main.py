#!usr/bin/python2.7
# coding=utf-8

import os, time
from app import config
from app import login
from app import crack
from rom import friends_list
from rom import friends
from rom import search_name
from rom import likes
from bs4 import BeautifulSoup as parser

class Brute(object):
	def __init__(self, url):
		self.url = url
		self.config = config.Config()
		self.cookie = self.config.loadCookie()
		self.menu = ''
		self.menu += '\n\033[0;95m\xe2\x80\xa2 \033[0;93m01 \033[0;93mDump Uid teman\n'
		self.menu += '\033[0;95m\xe2\x80\xa2 \033[0;93m02 \033[0;93mDump Uid daftar teman\n'
		self.menu += '\033[0;95m\xe2\x80\xa2 \033[0;93m03 \033[0;93mDump Pencarian nama\n'
		self.menu += '\033[0;95m\xe2\x80\xa2 \033[0;93m04 \033[0;93mDump Uid dari like status\n'
		self.menu += '\033[0;95m\xe2\x80\xa2 \033[0;93m05 \033[0;93mMulai Crack\n'
		self.menu += '\033[0;95m\xe2\x80\xa2 \033[0;93m06 \033[0;93mJoin group\n'
		self.menu += '\033[0;95m\xe2\x80\xa2 \033[0;93m07 \033[0;93mHapus cookies\n'
		self.menu += '\033[0;95m\xe2\x80\xa2 \033[0;91m00 \033[0;93mUpdate tools '
		if self.cookie == False:
			login.loginFb(self, self.url, self.config)
			self.cookie = self.config.loadCookie()

	def start(self):
		response = self.config.httpRequest(self.url+'/profile.php', self.cookie).encode('utf-8')
		if 'mbasic_logout_button' in str(response):
			self.main(response)
		else:
			os.remove('log/cookies.log')
			print('\033[0;95m\xe2\x80\xa2 \033[0;91mCokiies fb salah!\033[0m')
			raw_input('\033[0;95m\xe2\x80\xa2\033[0;97m Tekan Enter ')
			login.loginFb(self, self.url, self.config)
			self.cookie = self.config.loadCookie()
			self.start()
			exit()

	def main(self, response):
		os.system('clear')
		print(self.config.banner())
		html = parser(response, 'html.parser')
		print('\033[0;95m\xe2\x80\xa2 Welcome \033[0;93m '.decode('utf-8')+html.title.text.upper())
		print(self.menu)
		try:
			choose = int(raw_input('\n\033[0;95m\xe2\x80\xa2\033[0;91m --> \033[0;93m'))
		except ValueError:
			exit('\n\033[0;95m\xe2\x80\xa2 \033[0;96mJalankan kembali perintah nya! python2 crack.py\033[0;97m')
		if choose == 1:
			exit(friends_list.main(self, self.cookie, self.url, self.config))
		elif choose == 2:
			exit(friends.main(self, self.cookie, self.url, self.config))
		elif choose == 3:
			exit(search_name.main(self, self.cookie, self.url, self.config))
		elif choose == 4:
			exit(likes.main(self, self.cookie, self.url, self.config))
		elif choose == 5:
			exit(crack.Brute().main())
		elif choose == 0:
			os.system('git pull')
		elif choose == 6:
			ask = raw_input('\n\033[0;95m\xe2\x80\xa2\033[0;97m Tekan enter untuk lanjut ')
			print '\033[0;95m\xe2\x80\xa2\033[0;96m Mohon tunggu... '
			os.system ('xdg-open https://www.facebook.com/453688872336137')
		elif choose == 7:
			ask = raw_input('\n\033[0;95m\xe2\x80\xa2\033[0;97m Apakah anda yakin [\033[0;92mY\033[0;97m/\033[0;91mN\033[0;97m]\033[0;91m :\033[0;93m ')
			if ask.lower() == 'y':
				print('\033[0;95m\xe2\x80\xa2\033[0;91m Menghapus cokiies...')
				time.sleep(2)
				os.remove('log/cookies.log')
				print('\033[0;95m\xe2\x80\xa2 \033[0;92mberhasil terhapus!\033[0m')
				time.sleep(2)
				login.loginFb(self, self.url, self.config)
				self.cookie = self.config.loadCookie()
				self.start()
			else:
				self.cookie = self.config.loadCookie()
				print('\033[0;95m\xe2\x80\xa2 \033[0;91mbatal!')
				self.start()
		else: exit('\n\033[0;95m\xe2\x80\xa2\033[0;91mlihat menu dong ajg\033[0m')

