#Recebe as informações de acordo com as tags em que se cadastrou

import socket

HOST = 'localhost'
PORT = 8080


def receber(con):
    mensagem = b''
    while True:
        buffer = con.recv(1)
        if not buffer or buffer == b'\n': break
        mensagem += buffer
    return mensagem

def erro():
    print ('ERROR')



print ('Deseja conectar? (1- sim / 2-nao)\n') #isso foi só pra 'formalizar' o uso do CONNECT/ACK mesmo, não tinha necessidade

if(input() == '1'):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((HOST,PORT))
    tcp.sendall(b'CONNECT\n')

    if receber(tcp) == b'CONNACK':  
        print ('Deseja cadastrar em qual Topico? (Humidade - Temp/C - Temp/F)\n')
        tcp.sendall (b'SUBSCRIBE\n')
        sub_topico = input() + '\n'
        tcp.sendall (sub_topico.encode()) #sendall precisa que seja em bytes, funcao encode resolve isso


        if receber(tcp) == b'SUBACK':
            print('Cadastrado com sucesso.')
            while receber(tcp) == b'PUBLISH':
                pub_topico = receber(tcp) 
                info = receber(tcp)
                print("Topico: ",pub_topico.decode(),' / Info: ', info.decode())



    else:
        erro()




        tcp.close()

print ('Conexão finalizada.\n')
