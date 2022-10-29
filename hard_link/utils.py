import pathlib
import shelve
import dbm


def gen_path(path):
    paths = pathlib.Path(path).iterdir()
    # for _ in paths:
    #     print(_)
    # print(paths)
    return paths


def is_linked(filename):
    with dbm.open('linked', flag='c') as data:
        flag = data.get(filename)
        if not flag:
            data[filename] = "true"
            return False
        else:
            return True


def not_linked(filename):
    with shelve.open('linked', flag='c') as data:
        del data[filename]


if __name__ == '__main__':
    f = r'C:\Users\fanof\Desktop\TMP\Ariana Grande\folder.jpg'
    # print(gen_md5(f))

    gen_path(r'C:\Users\fanof\Desktop\TMP\Ariana Grande')
    # gen_path(r'Z:\video2\music')
