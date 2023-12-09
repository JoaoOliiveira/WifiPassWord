import os
import subprocess

print('============== Wifi KEY =============')
print('Lembrando só redes conectadas serão mostradas')

os.system('netsh wlan show profile')
print('nome da rede: ')
rede =  input()
os.system('netsh wlan show profile ' + rede +  ' key=clear')
