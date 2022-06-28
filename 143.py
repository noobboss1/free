from XFORD import login
import os
import platform
import webbrowser
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('mkdir XFORD-DATA')
except:pass
try:os.system('mkdir DATA')
except:pass
try:os.system('mkdir results')
except:pass
try:os.system('mkdir OK')
except:pass
try:os.system('mkdir CP')
except:pass
try:os.system('mkdir TAP-A2F')
except:pass
try:os.system('mkdir /sdcard/XFORD-DATA')
except:pass
try:os.system('mkdir /sdcard/XFORD-DATA/results')
except:pass
try:os.system('mkdir /sdcard/XFORD-DATA/OK')
except:pass
try:os.system('mkdir /sdcard/XFORD-DATA/CP')
except:pass
try:os.system('mkdir /sdcard/XFORD-DATA/TAP-A2F')
except:pass
try:os.system('touch .prox.txt')
except:pass
P = '\x1b[1;97m'
import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print('%s\nBAD INTERNET CONNECTION\n'%(P))
	exit()

login()
