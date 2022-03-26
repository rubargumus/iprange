#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import time 
import requests

os.system("cls")

print("-"*90)
print("Hoş Geldiniz")
print("-"*90)
time.sleep(2)
os.system("cls")



banner = """ 
    _   ____  ____ __ ______   __________  ____  __       __ __ __________
   / | / / / / / //_// ____/  /_  __/ __ \/ __ \/ /      / //_//  _/_  __/
  /  |/ / / / / ,<  / __/      / / / / / / / / / /      / ,<   / /  / /   
 / /|  / /_/ / /| |/ /___     / / / /_/ / /_/ / /___   / /| |_/ /  / /    
/_/ |_/\____/_/ |_/_____/    /_/  \____/\____/_____/  /_/ |_/___/ /_/     
                                                                          

"""
a = """ 
   		Developed By NUKE
"""
print("-"*90)
print(banner)
print("-"*90)
print(a)
print("-"*90)


ip = input("Enter IP? : ")
parts = ip.split('.')
print(parts)
a='.'

start = int(input("Start Number? : "))
end = int(input("End Number? : "))
time = int(input("Timeout? : "))


for x in range(start, end + 1):
	look = parts[0]+a+parts[1]+a+parts[2]+a+str(x)
	try :
		r = requests.get("http://" + look , verify=False, timeout=time)
	
		if r.status_code == 200 or 404 or 403:
			print("_"*40,"\n")
			print(r.status_code,"Bulunan İP: {} ".format(look))
			print("_"*40)
			f = open("ip.txt", "a")
			arg = look + "\n"
			f.write(arg)

		else:
			print("""
Sunucu Şu Yanıtı Döndü 
	İP : {}
	Status Code : {}
			""".format(look,r.status_code))
	except requests.exceptions.RequestException as err:
		print("-"*40 )
		print("Bu İP Yanıt Dönmedi => {} ".format(look))
		print("-"*40)
	except requests.exceptions.HTTPError as errh:
		print("-"*40)
		print("Bu İP Yanıt Dönmedi => {} ".format(look))
		print("-"*40)
	except requests.exceptions.ConnectionError as errc:
		print("-"*40)
		print("Bu İP Yanıt Dönmedi => {} ".format(look))
		print("-"*40)
	except requests.exceptions.Timeout as errt:
		print("-"*40)
		print("Bu İP Zaman Aşımına Uğradı => {} ".format(look))
		print("-"*40)
   

		




os.system("cls")
print("İşlem Başarılı")

