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



tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Valores padrões

tcp.bind((HOST, PORT))
tcp.listen(10)

topicos = dict() #Faz mapeamento

def conexao(con, cliente):
    connect = receber(con)
    print(connect)
    if connect == b'CONNECT':
        print('Conectado por:', cliente,'\n')
        con.sendall(b'CONNACK\n')


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



    print ('Finalizando conexao do cliente\n', cliente)
    con.close()

while True:
    con, cliente = tcp.accept()
    import threading
    threading.Thread(target=conexao, args=(con, cliente)).start()


