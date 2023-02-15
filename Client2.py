import socket
import threading


def send_message():
    while True:
        input_message = 'Alena: ' + input('> ')

        if input_message == "exit":
            chat_socket.close()
            exit(0)
        chat_socket.send(input_message.encode(encoding='ascii'))


def receive_message():
    while True:
        received_message = chat_socket.recv(1024)
        print(received_message)


chat_socket = socket.socket()
address = ('127.0.0.1', 65432)
chat_socket.connect(address)

name = b"Alena"
chat_socket.send(name)

send_thread = threading.Thread(target=send_message)
send_thread.start()

recieve_thread = threading.Thread(target=receive_message)
recieve_thread.start()
