import time, requests, os
from colorama import Fore
os.system('pip install requests')
os.system('pip install colorama')
os.system('cls')
os.system(f'Title Spammer By Qu3ti')
print(f"""{Fore.RED}
╔╗ ┌─┐┌─┐┌┬┐  
╠╩╗├┤ └─┐ │                                          
╚═╝└─┘└─┘ ┴   
███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝                               
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
===================Webhook Spammer By Qu3ti===================
==============Github: https://github.com/qu3tiiii ============                                                           
"""+Fore.RESET)

webhook = input(Fore.RED+'Ingresa Tu Webhook: '+Fore.RESET)

username = input(f"{Fore.RED}Nombre De Webhook: "+Fore.RESET)
if not username:
    username='WH-Sp4m'
message = input(f"{Fore.RED}Mensaje Para Spamear: "+Fore.RESET)
if not message:
    message='@everyone fucked //Script By Qu3ti!'
picture = input(f"{Fore.RED}Foto de perfil"+Fore.RESET)
if not picture:

   picture='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgvFxdeTDVc0o-Yfwtn6pQ5dofIrde5pgAVSSLrpG9ZilYIBciZcyM5ApkMOadw7kT5UM&usqp=CAU'
data = {
	    'content': message,
	    'username': username,
	    'avatar_url': picture
	}

mnd = 0
mal = 0
###############
#             #
#Te veo       #
#Leyendo      #
#Mi           #
#Codigo:)     #
#             #
###############
while True:
		r = requests.post(webhook, data=data)

		if r.status_code == 204:
			mnd += 1
			print(f"{Fore.GREEN}[$] - '{message}' Enviado Correctamente [$]{Fore.RESET}")
			os.system(f'title Spammer By Qu3ti  - Enviados : {mnd} ^/ Errores : {mal}')
		else:
			mal += 1
			print(f"{Fore.RED}[-] - Error/Espera - [-]{Fore.RESET}")
			os.system(f'title Spammer By Qu3ti  - Enviados : {mnd} ^/ Errores : {mal}')
###############
#             #
#Te veo       #
#Leyendo      #
#Mi           #
#Codigo:)     #
#             #
###############
