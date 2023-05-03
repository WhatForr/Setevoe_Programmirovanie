# Импортируем модуль ftplib для работы с FTP-сервером

from ftplib import FTP

# Устанавливаем соединение с FTP-сервером ftp.gnu.org

ftp = FTP('ftp.gnu.org')

# Авторизуемся на FTP-сервере

ftp.login()

# Задаем путь и имя файла, который мы будем получать с FTP-сервера

out = '/root/recieve/tree.json.gz'

# Открываем файл на запись в бинарном режиме
# Выполняем получение файла с FTP-сервера с помощью метода retrbinary
# Если файл успешно получен, то записываем его содержимое в открытый файл

with open(out, 'wb') as f:
    ftp.retrbinary('RETR ' + 'tree.json.gz', f.write).
