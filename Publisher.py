
import socket
import time

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

def publish(topico, info, tcp):
    tcp.sendall(b'PUBLISH\n')
    tcp.sendall( topico + b'\n' )
    tcp.sendall( info + b'\n' )

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((HOST,PORT))

file = open ('htDHT11.txt')
i = 0
for linha in file: #pega a linha inteira ja
    s = linha.split() #separa termos por espaco
    publish(b'Humidade', s[1].encode(), tcp)  #uma implementacao mais versatil seria pegar o nome dos topicos de acordo com o nome das colunas (e ja cadastrar novos topicos automaticamente)
    publish(b'Temp/C', s[3].encode(), tcp)
    publish(b'Temp/F', s[4].encode(), tcp)

    time.sleep(1) #zzzzz
file.close()
