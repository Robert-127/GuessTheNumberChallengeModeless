import socket

import random



def start_server():

    host = '127.0.0.1'  # Localhost

    port = 65432        # Port to listen on



    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((host, port))

        s.listen()

        print("Server is listening for connections...")

        conn, addr = s.accept()

        with conn:

            print(f"Connected by {addr}")

            play_game(conn)



def play_game(conn):

    number_to_guess = random.randint(1, 100)

    print(f"Number to guess (for debugging): {number_to_guess}")

    attempts = 0



    while True:

        guess = receive_guess(conn)

        attempts += 1

        response = check_guess(guess, number_to_guess, attempts)

        conn.sendall(response.encode())

        if "Correct!" in response:

            break



def receive_guess(conn):

    data = conn.recv(1024)

    if not data:

        return None

    return int(data.decode())



def check_guess(guess, number_to_guess, attempts):

    if guess < number_to_guess:

        return "Too low!"

    elif guess > number_to_guess:

        return "Too high!"

    else:

        return f"Correct! It took you {attempts} attempts."



if __name__ == "__main__":

    start_server()

