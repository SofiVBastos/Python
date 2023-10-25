import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5555))
    server_socket.listen(2)
    print("Aguardando jogadores...")

    player1, addr1 = server_socket.accept()
    print("Jogador 1 conectado de", addr1)

    player2, addr2 = server_socket.accept()
    print("Jogador 2 conectado de", addr2)

    return player1, player2

def play_game(player1, player2):
    choices = {'pedra': 'tesoura', 'tesoura': 'papel', 'papel': 'pedra'}

    while True:
        move1 = player1.recv(1024).decode()
        move2 = player2.recv(1024).decode()

        if move1 == move2:
            result = "Empate!"
        elif choices[move1] == move2:
            result = "Jogador 1 vence!"
        else:
            result = "Jogador 2 vence!"

        player1.send(result.encode())
        player2.send(result.encode())

if __name__ == "__main__":
    player1, player2 = start_server()
    play_game(player1, player2)
