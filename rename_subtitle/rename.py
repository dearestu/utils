from rename_subtitle.utils import gen_path
from multiprocessing import Pool


def rename_sub(r_data):
    sub_path, v_path = r_data
    root_path = v_path.parent
    name = v_path.stem
    suffix = sub_path.suffix
    print('rename file', v_path)
    print('rename subtitle is: ', str(root_path / name) + suffix)
    sub_path.rename(str(root_path / name) + suffix)


def handle_rename(rename_data):
    with Pool() as p:
        p.map(rename_sub, rename_data)


if __name__ == '__main__':
    path = r'Z:\video2\link\tv\Pantheon.S01.1080p.AMZN.WEB-DL.DD+5.1.H.264-NTb'
    sub, video = gen_path(path)
    data = list(zip(sub, video))
    print(data)
    handle_rename(data)
