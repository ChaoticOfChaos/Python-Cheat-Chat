import socket
import makeKey


def startServer(host='0.0.0.0', porta=12345, AllowedList=[], username="host", hasKey=0, chatName=None):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen(1)

    print(f"[Server] Listening on : {host}:{porta}...")

    while True:
        conexao, endereco = servidor.accept()
        print(f"[Server] Trying Connection to : {endereco}")

        if (len(AllowedList) > 0 and not endereco[0] in AllowedList):
            print(f'[Server] Connection {endereco[0]} Failed')
            conexao.send("Forbidden Access".encode())
            conexao.close()
            continue

        print(f"[Server] Connected to {endereco[0]}:{endereco[1]}")


        try:
            while True:
                mensagem = conexao.recv(1024).decode()
                if hasKey == 1:
                    mensagem = makeKey.reverseKey(chatName, mensagem)
                if mensagem.lower() == '.exit':
                    print("[Server] Client Leave.")
                    break
                print(f"{mensagem}")

                resposta = input(f"<{username}> -> ")
                if hasKey == 1:
                    resposta = makeKey.executeKey(chatName, resposta)
                sender_resp = f"<{username}> -> " + resposta
                conexao.send(sender_resp.encode())
                if resposta.lower() == '.exit':
                    print("[Server] You Leave.")
                    break
        finally:
            conexao.close()
            servidor.close()