import socket

def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5555))
    return client_socket

if __name__ == "__main__":
    player_socket = connect_to_server()

    while True:
        move = input("Escolha pedra, papel ou tesoura: ")
        player_socket.send(move.encode())

        result = player_socket.recv(1024).decode()
        print(result)
