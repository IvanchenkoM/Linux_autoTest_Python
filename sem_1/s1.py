# Написать автотест на bash, который читает содержимое файла
# /etc/os-release (в нем хранится информация о версии системы)
# и выведет на экран “SUCCESS” если в нем содержатся версия
# 22.04.1, кодовое имя jammy и команда чтения файла выполнена
# без ошибок. В противном случае должно выводится “FAIL”.
# Переписать тест на Python c использованием модуля subprocess.

import subprocess
result = subprocess.run('cat /etc/os-release', shell=True, stdout=subprocess.PIPE, encoding='utf-8')
out = result.stdout

if result.returncode == 0:
    if '22.04.1' in out and 'jammy' in out:
        print('SUCCESS')
    else:
        print('FAIL')
#1 print(result)
#2 print(out)