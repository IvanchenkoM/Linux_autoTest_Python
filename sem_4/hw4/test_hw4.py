from sshcheckers import ssh_checkout
import pytest
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.mark.usefixtures('make_folders', 'make_files', 'delete_folders', 'deploy', 'deploy_delete')
class TestSeminar:

    def test_step1(self):
        assert ssh_checkout(f'{data.get("host")}', f'{data.get("login")}',
                            f'{data.get("password")}',
                            f'cd {data.get("folder_user")}folder_in; 7z a {data.get("folder_user")}folder_out/archive_1',
                            'Everything is Ok')

    def test_step_2(self):
        assert ssh_checkout(f'{data.get("host")}', f'{data.get("login")}',
                            f'{data.get("password")}',
                            f'cd {data.get("folder_user")}folder_out; 7z rn archive_1 file_1.txt file_100.txt',
                            'Everything is Ok')

    def test_step_3(self):
        assert ssh_checkout(f'{data.get("host")}', f'{data.get("login")}',
                            f'{data.get("password")}',
                            f'cd {data.get("folder_user")}folder_out; 7z i archive_1',
                            '0  ED  6F00181 AES256CBC')

    def test_step_4(self):
        assert ssh_checkout(f'{data.get("host")}', f'{data.get("login")}',
                            f'{data.get("password")}',
                            f'cd {data.get("folder_user")}folder_out; 7z x archive_1.7z',
                            'Everything is Ok')


if __name__ == '__main__':
    pytest.main(['-vv'])