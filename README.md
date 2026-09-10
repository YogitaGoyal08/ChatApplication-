# Python Real-Time Chat Application

A beginner-friendly real-time chat application built using Python sockets and threading. The application allows multiple clients to connect to a local server and exchange messages in real time.

## Features

* Real-time bidirectional messaging
* Multiple client connections
* Username support
* Timestamped messages
* Graceful client disconnection
* Server-side connection handling
* Runs on localhost
* Built using Python socket programming and threading

## Technologies Used

* Python
* Socket Programming
* TCP/IP
* Threading
* Datetime

## Project Structure

```text
ChatApplication/
│
├── server.py
├── client.py
└── README.md
```

## How to Run

### 1. Start the Server

Open a terminal in the project folder and run:

```bash
python server.py
```

The server will start on:

```text
127.0.0.1:5555
```

### 2. Start the Client

Open another terminal and run:

```bash
python client.py
```

Enter your username when prompted.

### 3. Connect Another Client

Open a third terminal and run:

```bash
python client.py
```

Enter another username.

The connected users can now exchange messages in real time.

## Example

```text
[18:30] Alice: Hello Bob!
[18:31] Bob: Hi Alice!
```

## How It Works

The server creates a TCP socket and listens for incoming client connections. Each connected client is handled using a separate thread so that multiple clients can communicate simultaneously.

When a client sends a message, the server adds the username and timestamp and broadcasts the message to the other connected clients.

## Security Note

This beginner version is designed for learning purposes and runs on localhost. Messages are transmitted through a normal TCP socket and are **not end-to-end encrypted**. The application should not be used to transmit sensitive or confidential information.

## Future Improvements

* GUI chat interface using Tkinter
* User registration and login
* SQLite database
* Multiple chat rooms
* Persistent message history
* Emoji support
* Desktop notifications
* Password hashing
* End-to-end encryption

## Learning Outcome

This project demonstrates practical understanding of:

* Python socket programming
* TCP client-server architecture
* Multithreading
* Real-time communication
* Exception handling
* Client connection management
"# ChatApplication-" 
