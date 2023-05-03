# Импортируем модуль socket
import socket

# Создаем TCP-сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Пользователь вводит IP-адрес сервера
print ('Write IP address of Server: ')
ips = input ()

# Пользователь вводит порт сервера
print ('Write Port of Server: ')
port = (int(input()))

# Устанавливаем соединение с сервером
sock.connect((ips, port))

# Пользователь вводит сообщение для отправки на сервер
print ('Write the massage you want to send: ')
ms = input()

# Кодируем сообщение в байты с использованием кодировки UTF-8 и отправляем через сокет
sock.send(bytes(ms, encoding = 'UTF-8'))

# Закрываем сокет
sock.close()
