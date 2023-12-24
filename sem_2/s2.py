import subprocess


def check_command_output(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0 and text in out:
        return True
    else:
        return False


if __name__ == '__main__':
    check_command_output('cd /home/user/folder_ex; touch file_4', '')