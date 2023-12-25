import pytest
import yaml
from sshcheckers import upload_files, ssh_checkout

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture(scope='class')
def make_folders():
    return ssh_checkout(f'{data.get("host")}', f'{data.get("login")}',
                        f'{data.get("password")}',
                        f'mkdir -p {data.get("folder_user")}folder_in {data.get("folder_user")}folder_out '
                        f'{data.get("folder_user")}folder_ex',
                        '')


@pytest.fixture(scope='class')
def make_files():
    return ssh_checkout(f'{data.get("host")}', f'{data.get("login")}',
                        f'{data.get("password")}',
                        f'cd {data.get("folder_user")}folder_in; touch file_1.txt file_2.txt file_3.txt',
                        '')


@pytest.fixture(scope='class')
def delete_folders():
    yield
    return ssh_checkout(f'{data.get("host")}', f'{data.get("login")}',
                        f'{data.get("password")}',
                        f'rm -rf {data.get("folder_user")}folder_in {data.get("folder_user")}folder_out '
                        f'{data.get("folder_user")}folder_ex',
                        '')


@pytest.fixture(scope='class')
def deploy():
    res = []
    upload_files(f'{data.get("host")}', f'{data.get("login")}',
                 f'{data.get("password")}',
                 f'{data.get("folder_in")}{data.get("file")}.deb',
                 f'{data.get("folder_user")}{data.get("file")}.deb')
    res.append(ssh_checkout(f'{data.get("host")}', f'{data.get("login")}',
                            f'{data.get("password")}',
                            f'echo {data.get("password")} | sudo -S dpkg -i {data.get("folder_user")}{data.get("file")}.deb',
                            "Настраивается пакет"))
    res.append(ssh_checkout(f'{data.get("host")}', f'{data.get("login")}',
                            f'{data.get("password")}',
                            f'echo {data.get("password")} | sudo -S dpkg -s {data.get("file")}',
                            "Status: install ok installed"))
    return all(res)


@pytest.fixture(scope='class')
def deploy_delete():
    yield
    return ssh_checkout(f'{data.get("host")}', f'{data.get("login")}',
                        f'{data.get("password")}',
                        f'echo {data.get("password")} | sudo -S dpkg -r {data.get("file")}',
                        "Удаляется")