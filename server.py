import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5555

clients = []
usernames = []


def get_time():
    return datetime.now().strftime("%H:%M")


def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode("utf-8"))
            except:
                remove_client(client)


def remove_client(client):
    if client in clients:
        index = clients.index(client)

        clients.remove(client)

        username = usernames[index]
        usernames.remove(username)

        client.close()

        message = f"[{get_time()}] {username} left the chat."
        print(message)

        broadcast(message)


def handle_client(client):
    try:
        username = client.recv(1024).decode("utf-8")

        clients.append(client)
        usernames.append(username)

        print(f"{username} joined the chat.")

        join_message = f"[{get_time()}] {username} joined the chat."
        broadcast(join_message, client)

        client.send(
            f"[{get_time()}] Welcome {username}! You are connected to the chat.".encode(
                "utf-8"
            )
        )

        while True:
            message = client.recv(1024).decode("utf-8")

            if not message:
                break

            formatted_message = f"[{get_time()}] {username}: {message}"

            print(formatted_message)

            broadcast(formatted_message, client)

    except:
        pass

    finally:
        remove_client(client)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen()

    print("=" * 45)
    print("      PYTHON CHAT SERVER")
    print("=" * 45)
    print(f"Server running on {HOST}:{PORT}")
    print("Waiting for clients...")
    print()

    while True:
        client, address = server.accept()

        print(f"New connection from {address}")

        thread = threading.Thread(
            target=handle_client,
            args=(client,)
        )

        thread.start()


if __name__ == "__main__":
    start_server()