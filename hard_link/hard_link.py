import subprocess
import sys

from utils import gen_path, is_linked, not_linked
from multiprocessing import Pool


def file_paths(source):
    new_file_paths = gen_path(source)
    return new_file_paths


def call_pool(file_path):
    try:
        if not is_linked(file_path):
            print(f'start hard link {file_path}')
            # 在群晖系统创建硬链接
            subprocess.run(['cp', '-r', '-l', str(file_path), '/volume4/video2/link/music'])
    except Exception as _:
        print(f'hard link failed: {file_path}')
        not_linked(file_path)


if __name__ == '__main__':
    path = sys.argv[1]
    pool = Pool()
    pool.map(call_pool, file_paths(path))
