import socket
import makeKey

def startClient(host='0.0.0.0', porta=12345, username='client', hasKey=False, chatName=None):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, porta))

    print(f"[Client] Linked at : {host}:{porta}")

    try:
        while True:
            mensagem = input(f"<{username}> -> ")
            if hasKey == 1:
                mensagem = makeKey.executeKey(chatName, mensagem)
            sender_msg = f"<{username}> -> " + mensagem
            cliente.send(sender_msg.encode())
            if mensagem.lower() == '.exit':
                print("[Client] You Leave.")
                break

            resposta = cliente.recv(1024).decode()
            if hasKey == 1:
                resposta = makeKey.reverseKey(chatName, resposta)
            if resposta.lower() == '.exit':
                print("[Client] Host Leave.")
                break
            print(f"{resposta}")
    finally:
        cliente.close()
        