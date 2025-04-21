import socket
import json

def shareKey(host="0.0.0.0", port=12345, chatName=""):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print(f"Listening to Share Key at {host}:{port}")

    connection, address = server.accept()
    
    print(f'[*] Connected to {address[0]}:{address[1]}')

    with open(f".\\chats\\{chatName}\\key.json", 'r', encoding='utf-8') as key:
        content = json.load(key)
        txtKey = json.dumps(content, indent=2, ensure_ascii=False)
        txtKey += ';'

    with open(f".\\chats\\{chatName}\\reverse.key.json", 'r', encoding='utf-8') as rkey:
        content = json.load(rkey)
        txtKey += json.dumps(content, indent=2, ensure_ascii=False)
        print(txtKey)
        connection.sendall(txtKey.encode())

    connection.close()


def getKey(host="0.0.0.0", port=12345, chatName=""):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    str_key = client.recv(1024).decode()

    keys = str_key.split(';')

    with open(f'.\\chats\\{chatName}\\key.json', 'w', encoding='utf-8') as keyjson:
        json.dump(json.loads(keys[0]), keyjson, indent=4, ensure_ascii=False)

    with open(f'.\\chats\\{chatName}\\reverse.key.json', 'w', encoding='utf-8') as revKeyJson:
        json.dump(json.loads(keys[1]), revKeyJson, indent=4, ensure_ascii=False)

    client.close()