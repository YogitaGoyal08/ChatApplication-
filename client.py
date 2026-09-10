import socket
import threading

HOST = "127.0.0.1"
PORT = 5555


def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")

            if not message:
                print("Disconnected from server.")
                break

            print("\n" + message)
            print("You: ", end="", flush=True)

        except:
            print("\nConnection closed.")
            break


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((HOST, PORT))

    print("=" * 45)
    print("        PYTHON CHAT APPLICATION")
    print("=" * 45)

    username = input("Enter your username: ")

    client.send(username.encode("utf-8"))

    receive_thread = threading.Thread(
        target=receive_messages,
        args=(client,)
    )

    receive_thread.daemon = True
    receive_thread.start()

    print("You are connected!")
    print("Type your message and press Enter.")
    print("Type 'exit' to leave the chat.")
    print()

    while True:
        try:
            message = input("You: ")

            if message.lower() == "exit":
                print("Leaving chat...")
                break

            if message.strip():
                client.send(message.encode("utf-8"))

        except:
            break

    client.close()


if __name__ == "__main__":
    start_client()