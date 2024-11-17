import socket



def start_client():

    host = '127.0.0.1'  # The server's hostname or IP address

    port = 65432        # The port used by the server



    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((host, port))

        print("Connected to the server!")

        play_game(s)



def play_game(s):

    while True:

        guess = get_guess()

        if guess is not None:

            s.sendall(str(guess).encode())

            response = s.recv(1024)

            print('Server response:', response.decode())

            if "Correct!" in response.decode():

                break



def get_guess():

    guess = input("Enter your guess (1-100): ")

    if guess.isdigit():

        return int(guess)

    else:

        print("Please enter a valid number.")

        return None



if __name__ == "__main__":

    start_client()



