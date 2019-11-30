import socket
import paho.mqtt.client as mqtt

HOST = 'localhost'
PORT = 8080

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp.connect((HOST,PORT))

print ('Para sair, use Control X\n')

mensagem = input()
tcp.sendall (mensagem.encode()) #sendall precisa que seja em bytes, funcao encode resolve isso




tcp.close()
print ('Conexão finalizada.\n', cliente)
