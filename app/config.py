# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:47:43) 
import requests

class Config:

    def loadCookie(self):
        try:
            file = open('log/cookies.log', 'r')
            cookie = file.read()
            file.close()
            return cookie.strip()
        except IOError:
            return False

    def banner(self):
        return ' \033[1;91m\xe2\x80\xa2\033[1;93m\xe2\x80\xa2\033[1;92m\xe2\x80\xa2                                       \033[1;91m\xe2\x80\xa2\033[1;93m\xe2\x80\xa2\033[1;92m\xe2\x80\xa2\n\033[1;91m    _______  ______ _______ _______ _     _\n    |       |_____/ |_____| |       |____/ \n\033[1;97m    |_____  |    \_ |     | |_____  |    \_ \n\n \033[1;91m\xe2\x80\xa2\033[1;93m\xe2\x80\xa2\033[1;92m\xe2\x80\xa2                                       \033[1;91m\xe2\x80\xa2\033[1;93m\xe2\x80\xa2\033[1;92m\xe2\x80\xa2 \n \033[1;95m\xe2\x80\xa2 \033[1;96mCreated\033[1;95m \xe2\x80\xa2 \033[1;96mCyber Lampung\n \033[1;95m\xe2\x80\xa2 \033[1;96mGithub\033[1;95m \xe2\x80\xa2 \033[1;96mgithub.com/ROMI-AFRZL\n \033[1;95m\xe2\x80\xa2 \033[1;96mGroup\033[1;95m \xe2\x80\xa2 \033[1;96mVIRAL  \n \033[1;91m\xe2\x80\xa2\033[1;93m\xe2\x80\xa2\033[1;92m\xe2\x80\xa2                                       \033[1;91m\xe2\x80\xa2\033[1;93m\xe2\x80\xa2\033[1;92m\xe2\x80\xa2 \n '
                                    

    def httpRequest(self, url, cookies):
        try:
            return requests.get(url, cookies={'cookie': cookies}).text
        except requests.exceptions.RequestException:
            exit('\n\033[0;95m\xe2\x80\xa2 \033[0;91mKesalahan koneksi, periksa koneksi Anda!\x1b[0m')

    def httpRequestPost(self, url, cookies, params):
        try:
            return requests.post(url, data=params, cookies={'cookie': cookies}).text
        except requests.exceptions.RequestException:
            exit('\n\033[0;95m\xe2\x80\xa2\033[0;91m Kesalahan koneksi, periksa koneksi Anda!\x1b[0m')