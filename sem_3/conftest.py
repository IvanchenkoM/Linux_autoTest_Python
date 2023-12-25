import pytest
import yaml
from s3 import check_command, getout
from datetime import datetime

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture(scope='class')
def make_folders():
    return check_command(f'mkdir -p {data.get("folder_in")} {data.get("folder_out")} {data.get("folder_ex")}', '')


@pytest.fixture(scope='class')
def delete_folders():
    yield
    return check_command(f'rm -rf {data.get("folder_in")} {data.get("folder_out")} {data.get("folder_ex")}', '')


@pytest.fixture(scope='class')
def make_files():
    return check_command(f'cd {data.get("folder_in")}; touch file_1.txt file_2.txt file_3.txt', '')


@pytest.fixture(autouse=True)
def print_time():
    print(f'Start: {datetime.now().strftime("%H:%M:%s.%f")}')
    yield
    print(f'\nFinish: {datetime.now().strftime("%H:%M:%s.%f")}')


@pytest.fixture(autouse=True)
def stat_log():
    yield
    time = datetime.now().strftime("%H:%M:%s.%f")
    stat = getout('cat /proc/loadavg')
    check_command(f"echo 'time:{time} count:{data['count']} size;{data['bs']} stat:{stat}' >> stat.txt", '')