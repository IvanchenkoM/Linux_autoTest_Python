from s3 import check_command, get_hash
import pytest
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.mark.usefixtures('make_folders', 'make_files', 'delete_folders')
class TestSeminar:

    def test_step_1(self):
        assert check_command(f'cd {data.get("folder_in")}; 7z a {data.get("folder_out")}/archive_1', 'Everything is Ok')

    def test_step_2(self):
        assert check_command(f'cd {data.get("folder_out")}; 7z rn archive_1 file_1.txt file_100.txt', 'Everything is Ok')

    def test_step_3(self):
        assert check_command(f'cd {data.get("folder_out")}; 7z i archive_1', '0  ED  6F00181 AES256CBC')

    def test_step_4(self):
        output = str(get_hash(f'{data.get("folder_out")}/archive_1.7z')).upper()[2:]
        assert check_command(f'cd {data.get("folder_out")}; 7z h archive_1.7z', output)

    def test_step_5(self):
        assert check_command(f'cd {data.get("folder_out")}; 7z x archive_1.7z', 'Everything is Ok')


if __name__ == '__main__':
    pytest.main(['-vv'])