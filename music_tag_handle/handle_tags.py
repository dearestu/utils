import sys
from multiprocessing import Pool
import music_tag
from utils import gen_path


def handle_music_tag(path):
    music_file_paths = gen_path(path)
    with Pool() as p:
        p.map(handle_tag, music_file_paths)


def handle_tag(path):
    print(f'start change file {str(path)}')
    f = music_tag.load_file(path)
    # artist = f['artist']
    # print(f'the artist {artist}')
    # f['album'] = '唐朝'
    f['albumartist'] = "OneRepublic"
    # f['artist'] = '谢天笑'
    # f['title'] = ''
    # f['year'] = '1992'
    f.save()


if __name__ == '__main__':
    path = r'Z:\video2\link\music\OneRepublic-Native-Deluxe_Edition-CD-FLAC-2013-PERFECT'
    handle_music_tag(path)
