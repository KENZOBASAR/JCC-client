import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"╔════════════════════════════╗")
            print(f"<IP-NETWORK-USER> : {message}")
            print(f"╚════════════════════════════╝")
            print("                                        L C        R")
            print('                                       ═══○○○○○○○○○█')
            broadcast(message, client_socket)
        except:
            print(f"╔═════════════════════════════╗")
            print(f"<ERROR> : Another instance found!")
            print(f"╚═════════════════════════════╝")
            print(f" Enter anything to exit...")
            input(">")
            client_socket.close()
            break

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 19132))
server.listen(5)
print('JCC (J8gho commuinication client) Client')
print('══════════════════════════════════════════════════')
print(' Server is listening...')
print("Server listening on port 19132")
print(" L=Listening C=Connected R=Recieved")
print("                                        L C        R")
print('                                       ═█═○○○○○○○○○○')
clients = []

while True:
    client_socket, addr = server.accept()
    print(f"╔═════════════════════════════════╗")
    print(f"Connection established with {addr}")
    print(f"╚═════════════════════════════════╝")
    print("                                        L C        R")
    print('                                       ═══█○○○○○○○○○')
    clients.append(client_socket)
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
