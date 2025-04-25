import os
import json
import makeHost
import connection
import shareKey
import makeKey

def outLogin():
    userInput = input('> ')

    match userInput:
        case ".new":
            allowedIPs = ""
            newChatName = input("Chat Name -> ")
            if (newChatName in os.listdir(".\\chats")):
                print('ERROR - Chat Already Exists')
                pass

            newChatUsername = input("Chat Username -> ")
            hostOrConnection = int(input("[0]Host Or [1]Connection"))

            hostIP = input("Host IP -> ")
            hostPort = int(input("Host Port -> "))

            if (hostOrConnection == 0):
                allowedIPs = input("Allowed IPs (Split with ';' | Empty for Allow All) -> ")

            hasKey = int(input("Has Key? [0/1] -> "))

            if not hasKey in [0, 1]:
                hasKey = 0


            jsonMaker = {"HostName": newChatName, "HostIP": hostIP, "HostPort": hostPort, "Username": newChatUsername, "AllowedIPs": [], "Type": hostOrConnection, "HasKey": hasKey}

            if (allowedIPs):
                jsonMaker["AllowedIPs"] = allowedIPs.split(';') if len(allowedIPs.split(';')) > 0 else []


            os.system(f'mkdir .\\chats\\{newChatName}')

            with open(f'.\\chats\\{newChatName}\\{newChatName}.config.json', 'w', encoding='utf-8') as nJson:
                json.dump(jsonMaker, nJson, indent=4, ensure_ascii=False)

        case ".open":
            chatName = input("Chat Name -> ")

            if (not chatName in os.listdir('.\\chats')):
                print('ERROR - Chat Not Exists')
                pass

            with open(f'.\\chats\\{chatName}\\{chatName}.config.json', 'r', encoding='utf-8') as jsn:
                data = json.load(jsn)

                if (data["Type"] == 0):
                    makeHost.startServer(data['HostIP'], data['HostPort'], data['AllowedIPs'], data['Username'], data['HasKey'], data['HostName'])

                elif (data["Type"] == 1):
                    connection.startClient(data['HostIP'], data['HostPort'], data['Username'], data['HasKey'], data['HostName'])

        case ".del":
            chatName = input('Chat Name -> ')

            if chatName in os.listdir('.\\chats'):
                ask = input('[->!WARNING!<-]Are You Sure? ')
                
                if (ask.lower() in ['yes', 'y']):
                    os.system(f'del .\\chats\\{chatName}')

            else:
                print('ERROR - Chat Not Found')

        case ".help":
            print('.new - Create a New Chat')
            print('.open - Open a Existent Chat')
            print('.del - Delete a Chat')
            print('.chats - Show All Existent Chats')
            print('.help - Help')
            print('.share_key - Open a Connection to Share the Key')
            print('.get_key - Connect to a Host to Get a Key')
            print('.make_key - Create a New Key')

        case ".chats":
            for e, i in enumerate(os.listdir('.\\chats')):
                print(f'({e}) -> {i}')

        case ".share_key":
            chatName = input('Chat Name -> ')
            if chatName in os.listdir('.\\chats'):
                hostIP = input('Host IP -> ')
                hostPort = int(input('Host Port -> '))
                shareKey.shareKey(hostIP, hostPort, chatName)

            else:
                print('ERROR - Chat Not Exists')

        case ".get_key":
            chatName = input('Chat Name -> ')
            if chatName in os.listdir('.\\chats'):
                hostIP = input('Host IP -> ')
                hostPort = int(input('Host Port -> '))
                shareKey.getKey(hostIP, hostPort, chatName)

            else:
                print('ERROR - Chat Not Exists')

        case ".make_key":
            chatName = input('Chat Name -> ')
            makeKey.makeKey(chatName)
            print(f'New Key To : {chatName}')

        case _:
            print("Type '.help' to help")

    outLogin()


if __name__ == "__main__":
    print('Welcome to Cheat Chat')
    outLogin()