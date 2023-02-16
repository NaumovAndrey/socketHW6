# После того как соединение произошло, первое сообщение будет ником пользователя, а далее, любое отправленное сообщение будет транслироваться другим клиентам.

import socket
import threading


def send_mess():
    while True:
        mes = input("> ")
        ya_socet.send(mes.encode(encoding='ascii'))


def get_mess():
    while True:
        text = ya_socet.recv(1024)
        print(text)


ya_socet = socket.socket()
addr = ("127.0.0.1", 65432)
ya_socet.connect(addr)

rec_thread = threading.Thread(target=send_mess)
get_thread = threading.Thread(target=get_mess)

rec_thread.start()
get_thread.start()
