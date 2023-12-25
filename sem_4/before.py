# Установить пакет openssh-server командой
# sudo apt install openssh-server
# Включить сервис
# sudo systemctl enable sshd
# в нашем случае sudo systemctl start sshd
# Создать пользователя
# sudo useradd user2 -m
# Задать ему пароль
# sudo passwd user2
# установлен пароль: user!234
# Выдать пользователю права суперпользователя
# sudo usermod -aG sudo user2


# pip install paramiko
# pip install pytest