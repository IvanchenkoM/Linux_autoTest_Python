# Задание 1.
#
# Условие:
# Дополнить проект тестами, проверяющими команды вывода
# списка файлов (l) и разархивирования с путями (x).
#
# *Задание 2. *
#
# • Установить пакет для расчёта crc32
# sudo apt install libarchive-zip-perl
# • Доработать проект, добавив тест команды расчёта хеша (h).
# Проверить, что хеш совпадает с рассчитанным командой crc32.
import pytest
from s2 import check_command_output


folder_in = '/home/user/folder_in'
folder_out = '/home/user/folder_out'
folder_ex = '/home/user/folder_ex'


#1й тест создание архива в папку из данных другой папки
def test_step_1():
    assert check_command_output(f'cd {folder_in}; 7z a {folder_out}/archive_1', 'Everything is Ok')


#2й тест список содержимого файла(l)
def test_step_2():
    assert check_command_output(f'cd {folder_out}; 7z x archive_1', '3 files')

#3й тест разархивировать файлы с полными путями(x)
def test_step_3():
    assert check_command_output(f'cd {folder_out}; 7z x archive_1', 'Everything is Ok')


#4й тест удаление архива из папки
def test_step_4():
    assert check_command_output(f'cd {folder_out}; 7z d archive_1', 'Everything is Ok')


if __name__ == '__main__':
    pytest.main(['-vv'])