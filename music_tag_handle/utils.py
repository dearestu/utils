import pathlib


def gen_path(path):
    file_path = []
    paths = pathlib.Path(path).iterdir()
    for _ in paths:
        if _.is_dir():
            file_path.extend(gen_path(_))
        else:
            if str(_).split('.')[-1] in ['mp3', 'flac', 'ape', 'm4a', 'dsf']:
                file_path.append(_)
    return file_path


if __name__ == '__main__':
    p = gen_path(r'C:\Users\fanof\Desktop\TMP\Ariana Grande')
    print(p)
    print(len(p))
