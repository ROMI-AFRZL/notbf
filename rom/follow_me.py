#!usr/bin/python2.7
# coding=utf-8

from bs4 import BeautifulSoup as parser

def main(cookie, url, config):
	try:
		response = config.httpRequest(url+'/Romi.Uyey', cookie).encode('utf-8')
		html = parser(response, 'html.parser')
		href = html.find('a', string='Ikuti')['href']
		config.httpRequest(url+href, cookie)
	except: pass
