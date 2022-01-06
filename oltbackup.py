#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema para backup dos arquivos do Chassis Fiberhome
Created on Sun May  2 10:28:21 2021

@author: Cosme Marcelo
email: cosme.mazo@fatec.sp.gov.br

"""

# Importando as Bibliotecas necessárias
import datetime, configparser, pytz, telegram, time
from telnetlib import Telnet

# Acessa o arquivo com os dados confidenciais
config = configparser.ConfigParser()
config.read_file(open('config.ini'))

num = 1 # Utilize esta variável para modificar o primeiro loop
espera = 5 # Esse é o primeiro valor do tempo de espera para ler o horário
lista = [] # Lista de OLT que foi feito o backup
diretorio = '/Backup/OLT/' # Diretorio raiz do backup

# Comandos executados no Telnet 
telnet_enable = 'en'
telnet_save = 'save'
telnet_user = config['CREDENCIAIS']['USER']
telnet_pass = config['CREDENCIAIS']['PASS']
ftp_ip = config['FTPDADOS']['FTPIP']
ftp_user = config['FTPDADOS']['FTPUSER']
ftp_pass = config['FTPDADOS']['FTPPASS']

while (num > 0) :
    
    erro = 1
    time.sleep(espera) # Tempo para verificar se entrou na janela de backup
    
    # Pegando horario oficial
    fuso_UTC = pytz.utc.localize(datetime.datetime.utcnow())
    fuso_PST = fuso_UTC.astimezone(pytz.timezone("America/Sao_Paulo")) # Horário Local
    arq_data = fuso_PST.strftime('%d.%m.%Y.%H.%M')
    hora = fuso_PST.strftime('%H:%M:%S')
    
    espera = 360 # Tempo para a proxima verificação fora da janela de backup
    
    if hora > '05:00:00' and hora < '05:30:00': # Janela de backup entre as 05h00 e 05h30
        
        siclo = 1 # Altere para a quantidade de OLT que será feito o backup
        espera = 5000 # Tempo para a proxima verificação após fazer o bakup
        
        while (siclo <= 2): # Numero de ciclos para sair do laço
            
            time.sleep(3)
            
            # Criar nome para os arquivos e determinar a pasta onde devem ser salvos
            if siclo == 1 : # Determina que as credenciais dessa OLT devem ser passadas na "primeira" volta
                olt = config['OLTIP']['OLT1'] # Pega o IP da OLT no aquivo de configuração
                arquivo1 = 'OLT_1/Config/Config_OLT_1.' + arq_data + '.cfg' # diretório onde será salvo o backup da OLT 1, nome do arquivo e extensão
                arquivo2 = 'OLT_1/System/System_OLT_1.' + arq_data + '.bin' # diretório onde será salvo o backup da OLT 1, nome do arquivo e extensão
                arquivo3 = 'OLT_1/Logs/LogsSystem_OLT_1.' + arq_data + '.txt' # diretório onde será salvo o backup da OLT 1, nome do arquivo e extensão
                nome_olt = 'OLT 1 Apelido da OLT' # Nome que será enviado no telegram
                
            elif siclo == 2 : # Determina que as credenciais dessa OLT devem ser passadas na "segunda" volta
                olt = config['OLTIP']['OLT2']
                arquivo1 = 'OLT_2/Config/Config_OLT_2.' + arq_data + '.cfg' # diretório onde será salvo o backup da OLT 2, nome do arquivo e extensão
                arquivo2 = 'OLT_2/System/System_OLT_2.' + arq_data + '.bin' # diretório onde será salvo o backup da OLT 2, nome do arquivo e extensão
                arquivo3 = 'OLT_2/Logs/LogsSystem_OLT_2.' + arq_data + '.txt' # diretório onde será salvo o backup da OLT 2, nome do arquivo e extensão
                nome_olt = 'OLT 2 Apelido da OLT' # Nome que será enviado no telegram
            
            """
            
            Caso tenha apenas uma OLT apague ou comente o elif
            Caso tenha mais de uma OLT copie o elif e altere os nomes para acrescentá-las(não há limite)
            Altere o valor da variável siclo.
            
            """  

            # Comandos Telnet para fazer os backups 
            telnet_cmd1 = 'upload ftp config ' + ftp_server + ' ' + ftp_user + ' ' + ftp_pass + ' ' + diretorio + arquivo1
            telnet_cmd2 = 'upload ftp system ' + ftp_server + ' ' + ftp_user + ' ' + ftp_pass + ' ' + diretorio + arquivo2
            telnet_cmd3 = 'upload ftp syslog ' + ftp_server + ' ' + ftp_user + ' ' + ftp_pass + ' ' + diretorio + arquivo3
            
            for i in range(1, 4):
                try:
                    print(f'{i}ª Tentativa')
                    terminal = Telnet(olt, timeout=25) # Acessa a OLT
            
                    terminal.read_until(b"Login: ", timeout=25) # Ve se está pedindo usuário
                    terminal.write(telnet_user.encode('ascii') + b"\n") # Passa o usuário
                    
                    terminal.read_until(b"Password: ", timeout=20) # Ve se pediu a senha
                    terminal.write(telnet_pass.encode('ascii') + b"\n") # Passa a senha
                    
                    terminal.read_until(b"User> ", timeout=10) # Ve se entrou como user comum
                    terminal.write(telnet_enable.encode('ascii') + b"\n") # pede acesso admin
                    
                    terminal.read_until(b"Password: ", timeout=10) # Ve se pediu a senha
                    terminal.write(telnet_pass.encode('ascii') + b"\n") # Passa a senha
                    time.sleep(5)
                    
                    # Executa os comando no terminal
                    terminal.read_until(b"Admin# ", timeout=30) 
                    terminal.write(telnet_save.encode('ascii') + b"\n" + b"\n")
                    terminal.read_until(b"Admin# ", timeout=60) 
                    time.sleep(15)
                    terminal.write(telnet_cmd1.encode('ascii') + b"\n" + b"\n")
                    terminal.read_until(b"Admin# ", timeout=30) 
                    time.sleep(10)
                    terminal.write(telnet_cmd2.encode('ascii') + b"\n" + b"\n")
                    terminal.read_until(b"Admin# ", timeout=30) 
                    time.sleep(10)
                    terminal.write(telnet_cmd3.encode('ascii') + b"\n")
                    terminal.read_until(b"Admin# ", timeout=30)
                    terminal.write(b"exit\n")
                    terminal.read_until(b"User> ")
                    terminal.write(b"exit\n")
        
                    # Compara a mensagem gerada pela OLT e gera um log de erro caso necessário
                    resposta = terminal.read_until(b"Bye! ").decode('ascii')

                except Exception as error:
                    alerta = error
                    erro = 1
                    continue              

                else:
                    if (resposta == 'exit\r\nExit.\r\n\x1b[2J\x1b[01;74HMaster\r\nDisconnected.\r\nThanks for using our product.\r\nBye!\r\n'):
                        num += 1
                        siclo += 1
                        erro = 0
                        lista.append(nome_olt)
                        break

            if (erro == 1):
                num += 1
                siclo += 1
                bot = telegram.Bot(config['CREDENCIAIS']['TOKEN'])
                bot.send_message(chat_id=config['CREDENCIAIS']['USUARIO'], \
                            text='🚨 Bom dia, houve um erro ao fazer o backup da ' + \
                                nome_olt + ', verifique por favor!\nErro: ' + str(alerta))

        if erro == 0 :
            bot = telegram.Bot(config['CREDENCIAIS']['TOKEN'])
            bot.send_message(chat_id=config['CREDENCIAIS']['USUARIO'], \
                     text='💾 Bom dia, os backups das ' + str(lista) + ', foram realizado com sucesso!')
            nome_olt = []
            





