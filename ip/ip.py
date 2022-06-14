import geocoder
import os



def clear():
	os.system("cls||clear")

def rgb(r, g, b):
	return f'\x1b[38;2;{r};{g};{b}m'
print(f"""{rgb(0, 225, 0)}
 ___ ____    _____ _           _           
|_ _|  _ \  |  ___(_)_ __   __| | ___ _ __ 
 | || |_) | | |_  | | '_ \ / _` |/ _ \ '__|
 | ||  __/  |  _| | | | | | (_| |  __/ |   
|___|_|     |_|   |_|_| |_|\__,_|\___|_|  

[1] Trace my ip

[2] Trace other ip""")
option = input("[+] Enter the option : ")
if option == "1":
	clear()
	MyIp = geocoder.ip("me")
	print(f"""-ip        : {MyIp.ip}
-status    : {MyIp.status_code} 
-country   : {MyIp.country}
-state     : {MyIp.state}
-city      : {MyIp.city}
-zip code  : {MyIp.postal}
-longtitude: {MyIp.lng}
-latitude  : {MyIp.lat}""")
if option == "2":
	clear()
	ip = input("[+] Enter The Target Ip: ")
	MyIp = geocoder.ip(ip)
	print(f"""-ip        : {MyIp.ip}
-status    : {MyIp.status_code} 
-country   : {MyIp.country}
-state     : {MyIp.state}
-city      : {MyIp.city}
-zip code  : {MyIp.postal}
-longtitude: {MyIp.lng}
-latitude  : {MyIp.lat}""")

