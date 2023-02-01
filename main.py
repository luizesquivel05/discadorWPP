import os
import pywhatkit as wpp
import time as tm

caminho = open('dados.csv', 'a')
print("Salve, salve caros usuários. Vamos hoje para discador Whatsapp. \n\nNesse programa você irá enviar automaticamente mensagens para vários destinatários. \n\nPara começar, nos conte se quer fazer upload de um .csv ou se quer importar manualmente as informações. \n\nAtenção: é pedido as informações telefone com WPP/nome da pessoa/mensagem a ser enviada.")
extensao = str(input('Digite M para MANUAL e C para upload CSV: ')).lower()
while extensao == "":
    extensao = str(input('OPS, você deve digitar algo válido: ')).lower()
if extensao == "m":
    print("Vamos lá, você escolheu a opção manual.")
    nome = str(input('Digite o nome da pessoa: '))
    tel = str(input('Digite o telefone da pessoa: '))
    msn = str(input('Digite a mensagem que deseja enviar para pessoa: '))
    caminho.write(f'\n{nome};{tel};{msn}')
    try:
        os.system('cls')
    except:
        os.system("clear")
    print("Dados salvos! Deseja fazer uma nova verificação?")
    while str(input('S para CONTINUAR e N para FECHAR ARQUIVO: ')) == "S":
        nome = str(input('Digite o nome da pessoa: '))
        tel = str(input('Digite o telefone da pessoa: '))
        msn = str(input('Digite a mensagem que deseja enviar para pessoa: '))
        caminho.write(f'\n{nome};{tel};{msn}')
        try:
            os.system('cls')
        except:
            os.system("clear")
        print("Dados salvos! Deseja fazer uma nova verificação?")
caminho.close()
try:
    os.system('cls')
except:
    os.system("clear")
cont = 0
for i in open('dados.csv', 'r'):
    if cont == 0:
        cont += 1
        continue
    aux = i.split(';')
    nome = aux[0]
    tel = aux[1]
    msn = aux[2]
    wpp.sendwhatmsg(f'+55{tel}', f'{msn}')
    tm.sleep(10)