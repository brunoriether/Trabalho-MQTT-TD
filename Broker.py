import socket
import time

HOST = 'localhost'
PORT = 8080



def receber(con):
    mensagem = b'' 
    while True:
        buffer = con.recv(1) #recebe de 1 em 1 byte (unica maneira que consegui)
        if not buffer or buffer == b'\n': break
        mensagem += buffer
    return mensagem


def erro():
    print ('ERROR')



tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Valores padrões do socket

tcp.bind((HOST, PORT))
tcp.listen(10) #numero max de conexoes

topicos = dict() #Faz mapeamento do topico para cada cliente

def conexao(con, cliente):
    connect = receber(con)
    print(connect)
    if connect == b'CONNECT':
        print('Conectado por:', cliente,'\n')
        con.sendall(b'CONNACK\n') #tem que lembrar de colocar tudo como byte qnd for mandar algo


        tipo = receber (con)
            
        if tipo == b'SUBSCRIBE':
            topico = receber(con)
            print ('Topico:', topico,'Cliente:', cliente,'\n')
            if not topico in topicos:
                topicos[topico] = []

            topicos[topico].append((cliente, con))
            con.sendall(b'SUBACK\n')

        else:
            erro()



    while connect == b'PUBLISH':
        pub_topico = receber(con) 
        info = receber(con)
        if pub_topico in topicos:
            for _, conn in topicos[pub_topico]:
                try:                 #sem isso, dava crash em tudo quando encerrava um cliente 
                    conn.sendall(b'PUBLISH\n')
                    conn.sendall(pub_topico + b'\n')
                    conn.sendall(info + b'\n')
                except:
                    pass
        con.sendall(b'PUBACK\n')

        connect = receber(con)




while True:     #foi o jeito que achei no stackoverflow pra ter cliente simultaneos
    con, cliente = tcp.accept()
    import threading
    threading.Thread(target=conexao, args=(con, cliente)).start()


#muito massa fazer esse trabalho, curti! Podia só ter tido um acompanhamento durante as aulas talvez.
#muito da matéria vista não tinha tanta ligação assim com o que teve que ser aprendiddo durante esse trabalho
#teria sido muito legal uma conexão maior! :D