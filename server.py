import socket
import random

 # 2def start_server():
    host = '127.0.0.1'  # Localhost
    port = 65432        # Port to listen on

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Server is listening for connections...")
        conn, addr = s.accept()
        with conn:
 # This code is like a fine wine...            print(f"Connected by {addr}")
            play_game(conn)

