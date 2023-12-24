import pytest
from s2 import check_command_output


folder_in = '/home/user/folder_in'
folder_out = '/home/user/folder_out'
folder_ex = '/home/user/folder_ex'


#1й тест создание архива в папку из данных другой папки
def test_step_1():
    assert check_command_output(f'cd {folder_in}; 7z a {folder_out}/archive_1', 'Everything is OK')


#2й тест удаление архива из папки
def test_step_2():
    assert check_command_output(f'cd {folder_out}; 7z d archive_1', 'Everything is OK')


if __name__ == '__main__':
    pytest.main(['-vv'])